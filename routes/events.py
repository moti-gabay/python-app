from flask import Blueprint, request, jsonify,Response
from extensions import db
from models.event import Event
from models.user import User
from utils.decorators import token_required , admin_required,token_required
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
            registered_users=json.dumps([]),  # כך תאפס מראש את המערך
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
@token_required
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
@token_required
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

import json

@events_bp.route('/events/<int:event_id>/register', methods=['POST'])
@token_required
def register_to_event(current_user, event_id):
    try:
        event = Event.query.get(event_id)
        if not event:
            return jsonify({'message': 'Event not found'}), 404

        # המרת המחרוזת לרשימה
        registered_users = json.loads(event.registered_users) if event.registered_users else []

        # מניעת רישום כפול
        if current_user.id in registered_users:
            return jsonify({'message': 'You are already registered for this event'}), 400

        # הוספת המשתמש לרשימה
        registered_users.append(current_user.id)

        # המרת הרשימה חזרה למחרוזת JSON לשמירה במסד הנתונים
        event.registered_users = json.dumps(registered_users)

        db.session.commit()

        return jsonify({
            'message': 'You have successfully registered for the event',
            'registered_users': registered_users
        }), 200

    except Exception as e:
        db.session.rollback()
        print(f"Error registering user to event: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@events_bp.route('/events/<int:event_id>/unregister', methods=['POST'])
@token_required
def unregister_from_event(current_user, event_id):
    try:
        event = Event.query.get(event_id)
        if not event:
            return jsonify({'message': 'Event not found'}), 404

        registered_users = json.loads(event.registered_users) if event.registered_users else []

        # בדוק אם המשתמש בכלל רשום
        if current_user.id not in registered_users:
            return jsonify({'message': 'You are not registered for this event'}), 400

        # הסר את המשתמש מהרשימה
        registered_users.remove(current_user.id)

        # שמור את הרשימה המעודכנת
        event.registered_users = json.dumps(registered_users)

        db.session.commit()

        return jsonify({
            'message': 'You have successfully unregistered from the event',
            'registered_users': registered_users
        }), 200

    except Exception as e:
        db.session.rollback()
        print(f"Error unregistering user from event: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500



@events_bp.route('/events/<int:event_id>/approve', methods=['PUT'])
@token_required
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


@events_bp.route('/events/<int:event_id>/unapprove', methods=['PUT'])
@token_required
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

@events_bp.route('/events/approved', methods=['GET'])
@token_required
def get_approved_events(current_user):
    try:
        approved_events = Event.query.filter_by(is_approved=True).all()
        return jsonify([event.to_dict() for event in approved_events]), 200
    except Exception as e:
        print(f"Error fetching approved events: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500
