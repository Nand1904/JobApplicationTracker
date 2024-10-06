from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import JobApplication, User  # Ensure your User model is imported
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db

main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']  # Add this line
        password = request.form['password']
        
        # Check if the username or email already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('main.register'))

        if User.query.filter_by(email=email).first():  # Check email uniqueness
            flash('Email already exists. Please choose a different one.', 'danger')
            return redirect(url_for('main.register'))

        new_user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form['username_or_email']  # Renamed for clarity
        password = request.form['password']
        
        # Find user by either username or email
        user = User.query.filter(
            (User.username == username_or_email) | 
            (User.email == username_or_email)
        ).first() 
        
        if user and user.check_password(password):  # Check the password using the method from User model
            login_user(user)
            return redirect(url_for('main.index'))

        flash('Login failed. Check your username/email and password.', 'danger')

    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')  # Optional: flash message for logout confirmation
    return redirect(url_for('main.login'))  # Redirect to the login page after logout

@main.route('/', methods=['GET', 'POST'])
@login_required  # Ensure this route is only accessible to logged-in users
def index():
    search_query = request.args.get('search')
    
    if search_query:
        applications = JobApplication.query.filter(
            (JobApplication.user_id == current_user.id) &  # Filter by user_id
            ((JobApplication.company.like(f'%{search_query}%')) |
             (JobApplication.position.like(f'%{search_query}%')))
        ).all()
    else:
        applications = JobApplication.query.filter_by(user_id=current_user.id).all()  # Filter by user_id
    
    no_results = len(applications) == 0  # Flag for no results
    return render_template('index.html', applications=applications, no_results=no_results)

@main.route('/add_application', methods=['GET', 'POST'])
@login_required
def add_application():
    if request.method == 'POST':
        company = request.form['company']
        position = request.form['position']
        date_applied_str = request.form['date_applied']  # Get the date as string
        date_applied = datetime.strptime(date_applied_str, '%Y-%m-%d').date()  # Convert to date object
        status = request.form['status']
        notes = request.form['notes']
        user_id = current_user.id

        new_application = JobApplication(
            user_id=user_id,
            company=company,
            position=position,
            date_applied=date_applied,  # Use the date object
            status=status,
            notes=notes
        )

        db.session.add(new_application)
        db.session.commit()
        flash('Application added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('add_application.html')

@main.route('/update_application/<int:application_id>', methods=['GET', 'POST'])
@login_required
def update_application(application_id):
    application = JobApplication.query.get_or_404(application_id)

    if request.method == 'POST':
        # Get the data from the form
        company = request.form['company']
        position = request.form['position']
        date_applied_str = request.form['date_applied']  # Get the date as string
        date_applied = datetime.strptime(date_applied_str, '%Y-%m-%d').date()  # Convert to date object
        status = request.form['status']
        notes = request.form['notes']

        # Update the application fields
        application.company = company
        application.position = position
        application.date_applied = date_applied  # Ensure this is a date object
        application.status = status
        application.notes = notes

        try:
            db.session.commit()
            flash('Application updated successfully!', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while updating the application.', 'danger')

    return render_template('update_application.html', application=application)

@main.route('/delete/<int:application_id>', methods=['GET', 'POST'])
@login_required
def delete_application(application_id):
    application = JobApplication.query.get_or_404(application_id)

    # Check if the current user is the owner of the application
    if application.user_id != current_user.id:
        flash('You are not authorized to delete this application.', 'danger')
        return redirect(url_for('main.index'))

    db.session.delete(application)
    db.session.commit()
    flash('Application deleted successfully!', 'success')
    return redirect(url_for('main.index'))
