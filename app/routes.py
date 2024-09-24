from flask import Blueprint, render_template, request, redirect, url_for
from .models import JobApplication
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    search_query = request.args.get('search')
    if search_query:
        applications = JobApplication.query.filter(
            (JobApplication.company.like(f'%{search_query}%')) |
            (JobApplication.position.like(f'%{search_query}%'))
        ).all()
    else:
        applications = JobApplication.query.all()
    
    # Create a flag for no results
    no_results = len(applications) == 0
    
    return render_template('index.html', applications=applications, no_results=no_results)

@main.route('/add', methods=['GET', 'POST'])
def add_application():
    if request.method == 'POST':
        company = request.form['company']
        position = request.form['position']
        date_applied = request.form['date_applied']
        status = request.form['status']
        notes = request.form['notes']

        new_application = JobApplication(company=company, position=position, date_applied=date_applied, status=status, notes=notes)
        db.session.add(new_application)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('add_application.html')

@main.route('/update/<int:application_id>', methods=['GET', 'POST'])
def update_application(application_id):
    application = JobApplication.query.get_or_404(application_id)

    if request.method == 'POST':
        application.company = request.form['company']
        application.position = request.form['position']
        application.date_applied = request.form['date_applied']
        application.status = request.form['status']
        application.notes = request.form['notes']

        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('update_application.html', application=application)

@main.route('/delete/<int:application_id>', methods=['GET', 'POST'])
def delete_application(application_id):
    application = JobApplication.query.get_or_404(application_id)
    db.session.delete(application)
    db.session.commit()
    return redirect(url_for('main.index'))
