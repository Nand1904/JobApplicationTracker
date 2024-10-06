# Job Application Tracker

$\[
\text{Job Application Tracker}
\]$

Welcome to the **Job Application Tracker**! This web-based application helps you keep track of your job applications, manage their statuses, and stay organized throughout your job search process.

## Features

1. **User Authentication:**
   - Registration and Login system for secure access.
   - Each user has their personalized dashboard to manage applications.
   
2. **Add and Update Applications:**
   - Ability to add new job applications with details like company name, position, status, etc.
   - Update or modify application details as the process progresses.

3. **Job Application Overview:**
   - A list of all your job applications with filters to quickly find specific ones.
   - Dynamic statistics about your application statuses (e.g., pending, rejected, etc.).

4. **Interactive Interface:**
   - Clean and intuitive UI to enhance user experience.
   - Error handling, status updates, and logout functionality.

5. **Responsive Design:**
   - Fully responsive across different devices with advanced styling.
   - Features a 3D scrolling page and modern, sleek design.

## Technology Stack

The following technologies were used to build this project:

- **Backend:** Python (Flask framework)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Version Control:** GitHub
- **Tools:** VS Code, Flask, SQLAlchemy

## Project Structure

```latex
.
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── add_application.html
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── update_application.html
│   ├── static/
│   │   ├── css/
│   │   └── js/
├── instance/
│   ├── job_applications.db
├── migrations/
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── venv/
├── config.py
├── README.md
├── requirements.txt
└── run.py
