from flask_app import app
from flask import render_template, redirect, request, session
from flask import flash
from flask_app.models.user import User

@app.route('/dashboard')
def Beats_dashboard():
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect('/')
    return 'Main menu'
