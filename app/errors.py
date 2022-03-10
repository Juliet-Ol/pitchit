from app import app, db
from flask import render_template


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    db.sessions.rollback()
    return render_template('500.html'), 500    