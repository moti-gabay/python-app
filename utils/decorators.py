# utils/decorators.py
from functools import wraps
from flask import request, jsonify
import jwt
from models.user import User # וודא שאתה מייבא את מודל המשתמש שלך
from dotenv import load_dotenv
import os

# טען משתני סביבה מקובץ .env
load_dotenv()
# וודא ש-TOKEN_KEY מוגדר בקובץ .env שלך ושהוא משמש כמפתח סוד ל-JWT
token_key = os.getenv('TOKEN_KEY')

def token_required(f):
    """
    דקורטור שדורש טוקן JWT חוקי בעוגיות הבקשה (cookie).
    אם הטוקן חוקי, הוא מפענח אותו, מוצא את המשתמש המתאים
    ומעביר את אובייקט המשתמש (current_user) כארגומנט הראשון
    לפונקציה המקושטת.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        # נסה לקבל את הטוקן מהעוגיות
        token = request.cookies.get(token_key)

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            # פענוח הטוקן באמצעות מפתח הסוד (token_key)
            # וודא ש-token_key הוא אכן מפתח הסוד של JWT, ולא רק שם העוגייה
            data = jwt.decode(token, token_key, algorithms=['HS256'])
            # מציאת המשתמש לפי ה-user_id מהטוקן
            current_user = User.query.get(data['user_id'])
            if not current_user:
                return jsonify({'message': 'User not found!'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired!'}), 401
        except jwt.InvalidTokenError:
            # טיפול בשגיאות פענוח טוקן (לדוגמה, טוקן פגום או לא חוקי)
            return jsonify({'message': 'Invalid token!'}), 401
        except Exception as e:
            # טיפול בשגיאות כלליות אחרות במהלך פענוח או מציאת משתמש
            return jsonify({'message': 'An error occurred during token processing', 'error': str(e)}), 500
        
        # העבר את אובייקט המשתמש הנוכחי (current_user) כארגומנט הראשון
        # לפונקציה המקושטת, יחד עם כל שאר הארגומנטים שהיא עשויה לקבל.
        return f(current_user, *args, **kwargs)
    return decorated

def admin_required(f):
    """
    דקורטור שדורש שהמשתמש הנוכחי יהיה בעל הרשאות אדמין.
    הוא מניח ש-token_required כבר רץ והעביר את אובייקט המשתמש
    כארגומנט הראשון לפונקציה המקושטת.
    """
    @wraps(f)
    def decorated_function(current_user, *args, **kwargs): # מצפה לקבל את current_user
        # אין צורך לפענח את הטוקן שוב, current_user כבר אמור להיות מועבר.
        # אם current_user אינו קיים או שאין לו תפקיד 'admin', החזר שגיאת 403.
        if not current_user or current_user.role != 'admin':
            # אם current_user קיים, נכלול את התפקיד שלו בהודעה.
            user_role = current_user.role if current_user else 'None'
            return jsonify({'message': 'Unauthorized – admin only', "role": user_role}), 403
        
        # אם למשתמש יש הרשאות אדמין, המשך לקרוא לפונקציה המקורית
        # עם כל הארגומנטים שהועברו ל-decorated_function.
        return f(current_user, *args, **kwargs)
    return decorated_function


def member_required(f):
    """
    דקורטור לוודא שלמשתמש המאומת יש תפקיד 'member' או 'admin'.
    דורש שהדקורטור token_required ירוץ לפניו ויעביר את אובייקט המשתמש.
    """
    @wraps(f)
    def decorated_function(current_user, *args, **kwargs): # מצפה לקבל את current_user
        if not current_user:
            # במקרה זה, token_required אמור היה לטפל בחוסר אימות,
            # אבל זו בדיקה בטיחותית נוספת.
            return jsonify({'message': 'Authentication required for role check.'}), 401

        # תפקיד 'member' כולל גם תפקיד 'admin' (היררכיה)
        if current_user.role not in ['member', 'admin']:
            print(f"גישה אסורה: משתמש {current_user.email} (תפקיד: {current_user.role}) אינו חבר או מנהל.")
            return jsonify({'message': 'Forbidden: Member access required.', 'role': current_user.role}), 403
        
        # אם למשתמש יש תפקיד מתאים, המשך לקרוא לפונקציה המקורית.
        return f(current_user, *args, **kwargs)
    return decorated_function
