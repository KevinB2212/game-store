# 🎮 Game Store

> Full-stack e-commerce web app for browsing and purchasing games

## About

A Django-based game store application with product listings, shopping cart, user authentication, and an admin panel for managing inventory. Built as part of DCU's Web Development module.

## Features

- 🛒 Browse and search game catalogue
- 🛍️ Shopping cart with add/remove functionality
- 🔐 User registration and authentication
- 👤 Admin panel for managing products
- 📱 Responsive design

## Project Structure

```
├── examapp/
│   ├── models.py       # Database models (Games, Cart, Users)
│   ├── views.py        # View logic & request handling
│   ├── forms.py        # User forms (registration, login)
│   ├── admin.py        # Admin panel configuration
│   ├── templates/      # HTML templates
│   ├── static/         # CSS, JS, images
│   └── migrations/     # Database migrations
├── ca298exam/          # Django project settings
├── db.sqlite3          # SQLite database
└── manage.py           # Django management script
```

## Getting Started

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

Then open `http://localhost:8000` in your browser.

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** SQLite

## Author

**Kevin** — Dublin City University

---

*DCU CA298 — Web Development*
