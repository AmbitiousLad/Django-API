# 🚀 Django-API Task Manager

Welcome to **Django-API**, a simple yet powerful **Task Manager API server** built with **Django** and **Django REST Framework**. This project demonstrates how to build custom RESTful APIs, integrate a database, create a clean frontend, and write robust tests with high code coverage.

---

## 📌 **Features**

✅ Custom RESTful API endpoints (CRUD operations)  
✅ SQLite database integration  
✅ Stylish frontend with Django templates and Bootstrap  
✅ Admin dashboard for managing tasks  
✅ Unit, Integration, and API tests  
✅ Test coverage report

---

## ⚙️ **Tech Stack**

- **Backend:** Python, Django, Django REST Framework  
- **Database:** SQLite (default, easy to switch)  
- **Frontend:** Django Templates + Bootstrap 5  
- **Testing:** Django TestCase, DRF APIClient, `coverage.py`

---

## 📂 **Project Structure**

```
   .
├── config/ # Django project settings
├── api/ # App with models, views, serializers, tests
│ ├── migrations/
│ ├── templates/ # Frontend templates
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ ├── tests.py
├── db.sqlite3 # SQLite database
├── manage.py
└── README.md

```


---

## 🚀 **Setup Instructions**

### 1️⃣ Clone the Repo

```
git clone https://github.com/<your-username>/Django-API.git
cd Django-API
```


### 2️⃣ Create Virtual Environment & Install Dependencies

```
python -m venv venv

Activate:
On Mac/Linux:
source venv/bin/activate

On Windows:
venv\Scripts\activate

pip install -r requirements.txt
```


### 3️⃣ Apply Migrations & Create Superuser

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```


### 4️⃣ Run the Server

` python manage.py runserver `

---

## 🌐 **How to Access**

| URL                          | Description                |
|------------------------------|----------------------------|
| http://127.0.0.1:8000/       | Frontend UI (task list)    |
| http://127.0.0.1:8000/admin/ | Django admin panel         |
| http://127.0.0.1:8000/api/tasks/ | API endpoint for tasks  |

---

## 🔗 **API Endpoints**

| Endpoint               | Method | Description            |
|------------------------|--------|------------------------|
| /api/tasks/            | GET    | List all tasks         |
| /api/tasks/            | POST   | Create a new task      |
| /api/tasks/<id>/       | GET    | Retrieve a task by ID  |
| /api/tasks/<id>/       | PUT    | Update a task          |
| /api/tasks/<id>/       | DELETE | Delete a task          |

- ✅ Content-Type: application/json

**Sample POST Body:**
```
{
"title": "Learn Django",
"description": "Build custom APIs",
"completed": false
}
```

---

## ✅ **Testing**

**🧪 Tests Included:**

- Unit Tests: Model logic and serializer validation
- Integration Tests: Database interactions + CRUD flow
- API Tests: End-to-end API request and response checks

---

### 🚀 Run Tests with Coverage

```
Run all tests
coverage run manage.py test

Show coverage in terminal
coverage report

Generate HTML report
coverage html
```
### Screenshot
![image](https://github.com/user-attachments/assets/b0d56cc1-5a01-400c-acf6-347c6678d728)


---

## 📊 **Test Coverage**

| File              | Statements | Miss | Coverage |
|-------------------|------------|------|----------|
| api/models.py     | ✅         | ✅   | ✅       |
| api/serializers.py| ✅         | ✅   | ✅       |
| api/views.py      | ✅         | ✅   | ✅       |
| **TOTAL**         | ✅         | ✅   | ✅       |

---

## ❤️ **Thanks**

Special thanks to Keploy for inspiring robust API development and testing best practices. 🚀✨

---

## 📌 **Author**

**Name:** Sanket Kumar Rout  
**Project:** Django Custom API Server

---

## 🏷️ **License**

This project is open source — feel free to fork and build on top of it!

---

## 💬 **Feedback**

If you have suggestions, feel free to open an issue or a pull request. Happy coding! 🚀

---

## ✅ **What to do next:**

- Replace `<your-username>` in `git clone` with your GitHub username.
- Add coverage screenshot path after running coverage and taking a screenshot.
- Add `requirements.txt`:
`pip freeze > requirements.txt`
