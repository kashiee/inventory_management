# Inventory Management Tool

Welcome! 👋

This project is a **beautiful, simple, and modern inventory management system**. It’s designed to be easy to use, easy to set up, and easy to extend. Whether you’re a developer, a small business owner, or just curious, you’ll find it a breeze to get started.

---

## 🌟 What We Built
- **A secure backend** using FastAPI (Python) and SQLite, with JWT authentication for safe logins.
- **A gorgeous, minimal frontend** using only HTML, CSS, and JavaScript—no frameworks, no build tools, just open and go!
- **A seamless experience:** Register, log in, add products, update inventory, and view your stock—all in a few clicks.
- **Clean, modular code** that’s easy to read, learn from, and extend.
- **Ready for demo, learning, or real-world use.**

---

## ✨ Features
- **User Registration & Login:** Secure JWT-based authentication.
- **Product Management:**
  - Add new products (name, type, SKU, image, description, quantity, price)
  - Update product quantity
  - View all products in a beautiful table
- **Responsive, modern UI:** Looks great on desktop and mobile.
- **No React, Node, or build tools needed for the frontend!**
- **API docs:** Explore and test the backend at [http://localhost:8000/docs](http://localhost:8000/docs)
- **Quick API testing:** Use the included bash script for instant backend checks.

---

## 🗂️ Project Structure
```
backend/
│
├── app/                # FastAPI backend code
├── inventory.db        # SQLite database
├── frontend-static/    # Static HTML/CSS/JS frontend
│   ├── index.html
│   ├── style.css
│   └── app.js
├── requirements.txt    # Python dependencies
├── test_api.sh         # Bash script to test API
├── README.md           # This file
└── ...
```

---

## 🚀 Getting Started

### 1. **Backend (FastAPI + SQLite)**
- Create and activate a Python virtual environment:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Start the backend server:
  ```bash
  uvicorn app.main:app --reload
  ```
- Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API docs.

### 2. **Frontend (HTML/CSS/JS, No Build Tools!)**
- Go to the `frontend-static` folder
- Double-click `index.html` to open in your browser
- Or right-click and choose "Open with..." your browser
- Register, log in, and manage your inventory!

---

## 🧪 API Testing (Optional, but fun!)
- Run the provided bash script to test the backend API:
  ```bash
  bash test_api.sh
  ```

---

## 🛠️ Troubleshooting & Tips
- **Backend not running?**
  - Make sure you activated your virtual environment and ran `uvicorn app.main:app --reload`
- **Frontend not working?**
  - Make sure the backend is running first
  - Open `frontend-static/index.html` in your browser (no need for npm or node)
- **CORS errors?**
  - If you open the HTML file directly and see CORS errors, you can serve it with Python:
    ```bash
    cd frontend-static
    python3 -m http.server 8080
    ```
    Then visit [http://localhost:8080](http://localhost:8080)
- **Database issues?**
  - Delete `inventory.db` and restart the backend to reset

---

## 💡 How it Works (in plain English)
- **Backend:** FastAPI handles all the logic, SQLite stores your data, and JWT keeps your login secure.
- **Frontend:** Pure HTML, CSS, and JS—no frameworks! It talks to the backend using fetch and shows you everything in a clean, modern UI.
- **Authentication:** When you log in, you get a token. The frontend uses this token to prove who you are for every action.

---

## 🏗️ Want to Extend or Customize?
- Add more features (admin, analytics, etc.)—the code is clean and ready for it!
- Switch to PostgreSQL by updating the DB URL in `app/database.py`
- Deploy the backend anywhere Python runs, and the frontend anywhere static files are served

---

## 🙏 Thanks & License
- Built with FastAPI, SQLite, and a love for clean code
- MIT License



