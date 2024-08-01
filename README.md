# College Curriculum System
# Go to website: https://prajwalrangari.pythonanywhere.com/
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Introduction
The College Curriculum System is a comprehensive platform designed to enhance the academic experience for students, faculty, and administrators. This system provides an efficient way to manage courses, track student progress, and facilitate communication within an educational institution.

## Features
- **User Authentication**: Secure login and registration for students and teachers.
- **Course Management**: Teachers can add, edit, and delete courses along with detailed syllabi.
- **Student Enrollment**: Students can enroll in available courses and track their progress.
- **Syllabus Tracking**: Students can mark syllabus subtopics as pending, done, or revisit.
- **Branch-Specific Courses**: Courses displayed specific to different engineering branches.
- **Notifications and Reminders**: Set reminders for important academic events and deadlines.
- **Responsive Design**: Ensures a seamless experience across devices.

## Technologies Used
- **Backend**: Django, SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Security**: Django's built-in authentication system
- **Styling**: Bootstrap

## Installation

### Prerequisites
- HTML, CSS, JavaScript
- Python 3.8+
- SQLite (default)

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/prajwalr2003/college-curriculum-system.git
2. Create and Activate Virtual Environment
   ```bash
   pip install virtualenv
   cd college-curriculum-system
   virtualenv env
   cd env\Scripts
   activate
   cd ../../college-curriculum-system
3. Install Django in your System
   ```bash
   pip install django
   python manage.py createsuperuser

## Usage
### Start the server
```bash
python manage.py runserver
