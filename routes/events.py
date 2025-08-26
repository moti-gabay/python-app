from flask import Blueprint, request, jsonify
from extensions import mongo
from models.event import Event
from utils.decorators import token_required, admin_required
from datetime import datetime
import json
from bson import ObjectId

events_bp = Blueprint('events', __name__)

@events_bp.route('/events', methods=['POST'])
@token_required
def create_event(current_user):
    try:
        data = request.get_json()
        date_obj = datetime.strptime(data['date'], '%Y-%m-%d').date()
        time_obj = datetime.strptime(data['time'], '%H:%M:%S').time()

        new_event = Event(
            title=data['title'],
            date=date_obj,
            time=time_obj,
            location=data['location'],
            needed_volunteers=data['needed_volunteers'],
            description=data.get('description'),
            registered_users=[],
            is_approved=False,
            created_by=current_user._id
        )

        result = mongo.db.events.insert_one(new_event.to_dict())
        new_event._id = str(result.inserted_id)

        return jsonify(new_event.to_dict()), 201

    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500


@events_bp.route('/events', methods=['GET'])
@token_required
@admin_required
def get_events(current_user):
    try:
        docs = mongo.db.events.find()
        events = [Event.from_mongo(doc).to_dict() for doc in docs]
        return jsonify(events), 200
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500


@events_bp.route('/events/<string:event_id>', methods=['GET'])
@admin_required
def get_event(current_user, event_id):
    try:
        doc = mongo.db.events.find_one({"_id": ObjectId(event_id)})
        if not doc:
            return jsonify({"message": "Event not found"}), 404
        event = Event.from_mongo(doc)
        return jsonify(event.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@events_bp.route('/events/<string:event_id>', methods=['PUT'])
@admin_required
def update_event(current_user, event_id):
    try:
        data = request.get_json()
        update_data = {}
        for key in ['title','date','time','location','needed_volunteers','description']:
            if key in data:
                update_data[key] = data[key]

        if 'date' in update_data:
            update_data['date'] = datetime.strptime(update_data['date'], '%Y-%m-%d').date()
        if 'time' in update_data:
            update_data['time'] = datetime.strptime(update_data['time'], '%H:%M:%S').time()

        result = mongo.db.events.update_one({"_id": ObjectId(event_id)}, {"$set": update_data})
        if result.matched_count == 0:
            return jsonify({"message": "Event not found"}), 404

        doc = mongo.db.events.find_one({"_id": ObjectId(event_id)})
        event = Event.from_mongo(doc)
        return jsonify({"message": "Event updated successfully", "event": event.to_dict()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@events_bp.route('/events/<string:event_id>', methods=['DELETE'])
@token_required
@admin_required
def delete_event(current_user, event_id):
    try:
        result = mongo.db.events.delete_one({"_id": ObjectId(event_id)})
        if result.deleted_count == 0:
            return jsonify({"message": "Event not found"}), 404
        return jsonify({"message": "Event deleted successfully"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@events_bp.route('/events/<string:event_id>/register', methods=['POST'])
@token_required
def register_to_event(current_user, event_id):
    try:
        doc = mongo.db.events.find_one({"_id": ObjectId(event_id)})
        if not doc:
            return jsonify({'message': 'Event not found'}), 404

        event = Event.from_mongo(doc)
        if current_user._id in event.registered_users:
            return jsonify({'message': 'You are already registered'}), 400

        event.registered_users.append(current_user._id)
        mongo.db.events.update_one({"_id": ObjectId(event_id)}, {"$set": {"registered_users": event.registered_users}})

        return jsonify({'message': 'Registered successfully', 'registered_users': event.registered_users}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@events_bp.route('/events/<string:event_id>/unregister', methods=['POST'])
@token_required
def unregister_from_event(current_user, event_id):
    try:
        doc = mongo.db.events.find_one({"_id": ObjectId(event_id)})
        if not doc:
            return jsonify({'message': 'Event not found'}), 404

        event = Event.from_mongo(doc)
        if current_user._id not in event.registered_users:
            return jsonify({'message': 'You are not registered'}), 400

        event.registered_users.remove(current_user._id)
        mongo.db.events.update_one({"_id": ObjectId(event_id)}, {"$set": {"registered_users": event.registered_users}})

        return jsonify({'message': 'Unregistered successfully', 'registered_users': event.registered_users}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@events_bp.route('/events/<string:event_id>/approve', methods=['PUT'])
@token_required
@admin_required
def approve_event(current_user, event_id):
    try:
        result = mongo.db.events.update_one({"_id": ObjectId(event_id)}, {"$set": {"is_approved": True}})
        if result.matched_count == 0:
            return jsonify({"message": "Event not found"}), 404

        doc = mongo.db.events.find_one({"_id": ObjectId(event_id)})
        event = Event.from_mongo(doc)
        return jsonify({"message": "Event approved", "event": event.to_dict()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@events_bp.route('/events/<string:event_id>/unapprove', methods=['PUT'])
@token_required
@admin_required
def unapprove_event(current_user, event_id):
    try:
        result = mongo.db.events.update_one({"_id": ObjectId(event_id)}, {"$set": {"is_approved": False}})
        if result.matched_count == 0:
            return jsonify({"message": "Event not found"}), 404

        doc = mongo.db.events.find_one({"_id": ObjectId(event_id)})
        event = Event.from_mongo(doc)
        return jsonify({"message": "Event unapproved", "event": event.to_dict()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@events_bp.route('/events/approved', methods=['GET'])
@token_required
def get_approved_events(current_user):
    try:
        docs = mongo.db.events.find({"is_approved": True})
        events = [Event.from_mongo(doc).to_dict() for doc in docs]
        return jsonify(events)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
