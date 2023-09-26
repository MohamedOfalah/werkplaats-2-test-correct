from functools import wraps
from flask import request, redirect, url_for

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if the user is an admin (you need to implement this logic)
        if not current_user.is_admin:
            return redirect(url_for('unauthorized'))  # Redirect to an unauthorized page
        return f(*args, **kwargs)
    return decorated_function

