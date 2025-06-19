from flask import Blueprint, request, jsonify,Response
from extensions import db
from models.event import Event
from models.user import User
from utils.decorators import token_required , admin_required
from utils.util import json_response

from datetime import datetime
import json

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
            description=data['description'],
            registered_count=0,
            is_approved=False,
            created_by=current_user.id
        )
        db.session.add(new_event)
        db.session.commit()
        return jsonify(new_event.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@events_bp.route('/events', methods=['GET'])
@admin_required
def get_events(current_user):
    try:
        events = Event.query.all()
        event_list = [event.to_dict() for event in events]
        return json_response(event_list)
    except Exception as e:
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@events_bp.route('/events/<int:event_id>', methods=['GET'])
@admin_required
def get_event(current_user ,event_id):
    event = Event.query.get(event_id)
    if event:
        return jsonify(event.to_dict())
    else:
        return jsonify({"message": "Event not found"}), 404

@events_bp.route('/events/<int:event_id>', methods=['PUT'])
@admin_required
def update_event(current_user, event_id):
    try:
        event = Event.query.get(event_id)
        if not event:
            return jsonify({"message": "Event not found"}), 404

        data = request.get_json()
        event.date = data.get('date', event.date)
        event.time = data.get('time', event.time)
        event.location = data.get('location', event.location)
        event.needed_volunteers = data.get('needed_volunteers', event.needed_volunteers)
        event.description = data.get('description', event.description)

        db.session.commit()
        return jsonify({"message": "Event updated successfully", "event": event.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@events_bp.route('/events/<int:event_id>', methods=['DELETE'])
@admin_required
def delete_event(current_user, event_id):
    try:
        event = Event.query.get(event_id)
        if not event:
            return jsonify({"message": "Event not found"}), 404

        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "Event deleted successfully"})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@events_bp.route('/events/<int:event_id>/register', methods=['POST'])
@token_required
def register_volunteer(current_user ,event_id):
    try:
        event = Event.query.get(event_id)
        if not event:
            return jsonify({"message": "Event not found"}), 404

        if event.registered_count >= event.needed_volunteers:
            return jsonify({"message": "Event is full"}), 400

        event.registered_count += 1
        db.session.commit()
        return jsonify({"message": "Volunteer registered", "current_registered": event.registered_count})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@events_bp.route('/events/<int:event_id>/approve', methods=['POST'])
# @token_required  # ✅ רק מנהל יכול
@admin_required
def approve_event(current_user, event_id):
    try:
        event = Event.query.get(event_id)
        if not event:
            return jsonify({"message": "Event not found"}), 404

        event.is_approved = True
        db.session.commit()
        return jsonify({"message": "Event approved", "event": event.to_dict()})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500


    event = Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'Event not found'}), 404

    event.is_approved = True
    db.session.commit()
    return jsonify({"message": "Event approved", "event": event.to_dict()})

@events_bp.route('/events/<int:event_id>/unapprove', methods=['POST'])
@admin_required
def unapprove_event(current_user, event_id):
    # רק מנהל יכול לבטל אישור
    if current_user.role != 'admin':
        return jsonify({"message": "Unauthorized – admin only"}), 403

    event = Event.query.get(event_id)
    if not event:
        return jsonify({"message": "Event not found"}), 404

    event.is_approved = False
    db.session.commit()

    return jsonify({"message": "Event unapproved", "event": event.to_dict()})
