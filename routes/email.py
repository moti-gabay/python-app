# routes/email_bp.py
from flask import Blueprint, request, jsonify, current_app
from flask_mail import Message
from extensions import mail
from utils.decorators import token_required ,admin_required # אם תרצה להגן על נקודת קצה זו
import os # לייבוא os כדי לגשת למשתני סביבה
from dotenv import load_dotenv

load_dotenv()  

email_bp = Blueprint('email', __name__)

@email_bp.route('/send-donation-confirmation', methods=['POST'])
@token_required
def send_donation_confirmation():
    data = request.get_json()
    recipient_email = data.get('recipient_email')
    payer_name = data.get('payer_name', 'תורם יקר')
    amount = data.get('amount')
    currency = data.get('currency', 'ILS')
    transaction_id = data.get('transaction_id', 'N/A')

    if not recipient_email or not amount:
        return jsonify({'message': 'Missing recipient email or amount'}), 400

    try:
        msg = Message(
            subject="תודה על תרומתך לאתר מיניאן!",
            recipients=[recipient_email],
            html=f"""
            <div style="direction:rtl; text-align:right; font-family: Arial, sans-serif; line-height: 1.6;">
                <h2>תודה רבה על תרומתך, {payer_name}!</h2>
                <p>קיבלנו בהצלחה תרומה בסך <b>{amount} {currency}</b>.</p>
                <p>מספר עסקה: <b>{transaction_id}</b></p>
                <p>תרומתך חשובה לנו מאוד ועוזרת לנו להמשיך ולספק תוכן ושירותים איכותיים לקהילה.</p>
                <p>בברכה,</p>
                <p>צוות אתר מיניאן</p>
                <p style="font-size: 0.8em; color: #777;">
                    זוהי הודעה אוטומטית, נא לא להשיב להודעה זו.
                </p>
            </div>
            """
        )
        mail.send(msg)
        print(f"אימייל אישור נשלח בהצלחה ל: {recipient_email} עבור תרומה של {amount} {currency}")
        return jsonify({'message': 'Confirmation email sent successfully'}), 200
    except Exception as e:
        print(f"שגיאה בשליחת אימייל: {e}")
        return jsonify({'message': 'Failed to send confirmation email', 'error': str(e)}), 500

@email_bp.route('/send-contact-email', methods=['POST'])
@token_required
def send_contact_email(current_user):
    data = request.get_json()
    sender_name = data.get('name')
    sender_email = data.get('email')
    subject = data.get('subject', 'פנייה כללית')
    message_body = data.get('message')

    # כתובת האימייל של בעלי האתר מתוך משתני הסביבה
    owner_email = os.getenv('SITE_OWNER_EMAIL')
    if not owner_email:
        print("SITE_OWNER_EMAIL is not set in .env")
        return jsonify({'message': 'Server configuration error: Owner email not set'}), 500

    if not sender_name or not sender_email or not message_body:
        return jsonify({'message': 'Missing required fields: name, email, or message'}), 400



    try:
        msg = Message(
            subject=f"פנייה חדשה מאתר מיניאן: {subject} (מאת: {sender_name})",
            recipients=[owner_email], # שליחה לבעלי האתר
            reply_to=sender_email, # כדי שבעל האתר יוכל להשיב ישירות לשולח
            html=f"""
            <div style="direction:rtl; text-align:right; font-family: Arial, sans-serif; line-height: 1.6;">
                <h2>פנייה חדשה מדף יצירת קשר</h2>
                <p><b>שם השולח:</b> {sender_name}</p>
                <p><b>אימייל השולח:</b> {sender_email}</p>
                <p><b>נושא:</b> {subject}</p>
                <hr style="border-top: 1px solid #eee; margin: 20px 0;">
                <h3>ההודעה:</h3>
                <p>{message_body}</p>
                <hr style="border-top: 1px solid #eee; margin: 20px 0;">
                <p style="font-size: 0.8em; color: #777;">
                    זוהי הודעה אוטומטית שנשלחה מטופס יצירת הקשר באתר.
                </p>
            </div>
            """
        )
        mail.send(msg)
        print(f"אימייל יצירת קשר נשלח בהצלחה לבעלי האתר מ: {sender_email}")
        return jsonify({'message': 'Contact email sent successfully'}), 200
    except Exception as e:
        print(f"שגיאה בשליחת אימייל יצירת קשר: {e}")
        return jsonify({'message': 'Failed to send contact email', 'error': str(e)}), 500

@email_bp.route('/send-event-approved-email', methods=['POST'])
@admin_required # ניתן להוסיף הגנה אם רק שרת/אדמין יכול להפעיל
def send_event_approved_email(current_user):
    data = request.get_json()
    recipient_email = data.get('recipient_email')
    event_title = data.get('event_title')
    event_date = data.get('event_date')
    event_time = data.get('event_time')
    event_location = data.get('event_location')
    creator_name = data.get('creator_name', 'יוצר האירוע')

    if not recipient_email or not event_title or not event_date or not event_time or not event_location:
        return jsonify({'message': 'Missing required event details or recipient email'}), 400

    try:
        msg = Message(
            subject=f"אירועך '{event_title}' אושר באתר מיניאן!",
            recipients=[recipient_email],
            html=f"""
            <div style="direction:rtl; text-align:right; font-family: Arial, sans-serif; line-height: 1.6;">
                <h2>שלום {creator_name},</h2>
                <p>אנו שמחים להודיע לך שהאירוע שיצרת, <b>"{event_title}"</b>, אושר על ידי מנהלי האתר!</p>
                <p>פרטי האירוע:</p>
                <ul>
                    <li><b>שם האירוע:</b> {event_title}</li>
                    <li><b>תאריך:</b> {event_date}</li>
                    <li><b>שעה:</b> {event_time}</li>
                    <li><b>מיקום:</b> {event_location}</li>
                </ul>
                <p>האירוע שלך זמין כעת לצפייה ולהרשמה באתר.</p>
                <p>תודה על תרומתך לקהילה!</p>
                <p>בברכה,</p>
                <p>צוות אתר מיניאן</p>
                <p style="font-size: 0.8em; color: #777;">
                    זוהי הודעה אוטומטית, נא לא להשיב להודעה זו.
                </p>
            </div>
            """
        )
        mail.send(msg)
        print(f"אימייל אישור אירוע נשלח בהצלחה ל: {recipient_email} עבור האירוע '{event_title}'")
        return jsonify({'message': 'Event approved email sent successfully'}), 200
    except Exception as e:
        print(f"שגיאה בשליחת אימייל אישור אירוע: {e}")
        return jsonify({'message': 'Failed to send event approved email', 'error': str(e)}), 500