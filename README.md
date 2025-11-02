# Django To-Do List App 📃

Features
- Add daily tasks with deadline and mark tasks completed.
- Display completed and pending tasks separately.
- CRUD operations for tasks.
- Mix of Function-Based Views (FBV) and Class-Based Views (CBV).
- Styled with CSS only (animations included).
- SQLite database (default for Django).

Run locally
1. Create virtualenv and install requirements:
   ```
   python -m venv venv
   source venv/bin/activate         # mac/linux
   venv\Scripts\activate            # windows
   pip install -r requirements.txt
   ```
2. Apply migrations and run server:
   ```
   python manage.py migrate
   python manage.py runserver
   ```
3. Open http://127.0.0.1:8000/
