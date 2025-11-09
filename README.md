# 🧹 CleanText

A simple and elegant **Django web application** that lets you clean and analyze your text.
Perform multiple operations like removing punctuation, removing extra spaces, capitalizing letters, counting characters, and more — all from one clean and responsive interface.

---

## 🚀 Features

* Remove Punctuations
* Uppercase All Letters
* Lowercase All Letters
* Capitalize First Letter
* Remove New Lines
* Remove Extra Spaces
* Count Characters

---

## 🧩 Tech Stack

* **Python 3.13+**
* **Django 5+**
* **HTML5 + CSS3 + Bootstrap 5**

---

## ⚙️ Installation and Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/VaibhaoHatwar/cleantext.git
   cd cleantext
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**

   * **Windows (PowerShell):**

     ```bash
     env\Scripts\activate
     ```
   * **macOS/Linux:**

     ```bash
     source env/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install django
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

6. **Open your browser** and visit 👉
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📁 Project Structure

```
cleantext/
│
├── cleantext_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── textutils/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── admin.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── analyze.html
│
├── manage.py
├── .gitignore
└── README.md
```

---

## 🔒 Security & Form Handling

* All forms use **POST** method.
* **CSRF token** is included for protection.
* Text input is sanitized using utility functions before analysis.

---

## 👤 Author

**Vaibhao Hatwar**
🖥️ Full Stack Developer (MERN + Django)
📧 [vaibhaohatwar.works@gmail.com](mailto:vaibhaohatwar.works@gmail.com)

---

## ⭐ Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.

---

## 🧘 Inspiration

> “Clean code is a reflection of a clean mind.”
> – Inspired by simplicity and precision.

---

### 🏷️ License

This project is licensed under the **MIT License**.