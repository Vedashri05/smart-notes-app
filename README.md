# Smart Notes Application

A Flask-based notes management web application that uses Machine Learning to automatically predict note categories. Users can edit the predicted category while editing the note. The application also includes user authentication and category-based note filtering.

---

## Features

- User login and registration using WTForms
- Add, edit, view, and delete notes
- Automatic note category prediction using ML
- Editable category on edit page
- Filter notes by category
- MySQL database integration
- Clean and simple UI
- Modular Flask structure using routes (Blueprints)

---

## Machine Learning

- The ML model predicts the note category based on the note content
- Prediction happens when a note is saved
- The predicted category can be changed by the user later
- Supported Categories: `Personal`, `Study Notes`, `Reminder`

---

## Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL
- **Machine Learning:** Scikit-learn (NLP)
- **Forms & Validation:** Flask-WTF (WTForms)
- **Frontend:** HTML, CSS, Jinja Templates
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
project/
├── run.py 
├── app/
│ ├── init.py 
│ ├── models.py  
│ ├── routes/
│ │ ├── auth.py  # Login, register, logout
│ │ └── notes.py  # Notes CRUD & filtering
│ ├── ml/
│ └── forms.py 
├── templates/
├── static/
│
├── screenshots/ 
├── requirements.txt
├── README.md
└── .gitignore

```

## 📸 Screenshots

### Login Page
<p>
  <img src="screenshots/login_page.png" alt="Login Page" width="400">
</p>

### Notes Dashboard
<p>
  <img src="screenshots/home_page.png" alt="Notes Dashboard" width="500">
</p>

### Edit Note
<p>
  <img src="screenshots/edit_note.png" alt="Edit Note" width="400">
</p>

### View Note
<p>
  <img src="screenshots/view_note.png" alt="View Note" width="400">
</p>

---

## ⚙️ Setup Instructions

#### 1. Clone the Repository
```bash
git clone https://github.com/Vedashri05/smart-notes-app.git
cd smart-notes-app
```

#### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
```
Activate:
```bash
# For Windows:
venv\Scripts\activate
```
```bash
# For macOS / Linux:
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Create .env File
Create a .env file in the project root and add:

```env
SECRET_KEY=your_secret_key
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_NAME=notes_db
```

#### 5. Create MySQL Database
```bash
CREATE DATABASE notes_db;
```

#### 6. Run the Application
```bash
python run.py
```
Open your browser and visit:
http://127.0.0.1:5000/
