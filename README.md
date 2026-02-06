# CampaignHub

CampaignHub is a Flask-based web application designed to help businesses, startups, and individuals manage advertising, consultation requests, and growth support.  
It includes a public-facing site with service pages and forms, plus an admin dashboard for managing submissions.

---

## 🚀 Features

- **Home, Services, About, Contact pages** with clean navigation.
- **Consultation form** where users can request guidance on:
  - Digital Advertising
  - Television Advertising
  - Offline Advertising
  - Business Consultation
  - Business Ideas & Growth Support
  - Combined Advertising & Promotion package
- **Contact form** for general inquiries.
- **SQLite database integration** to store:
  - Contact messages
  - Consultation requests
- **Admin workflow**:
  - Login/logout system (simple hardcoded credentials for now).
  - Protected admin dashboard.
  - Ability to view all contact and consultation submissions.

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite (via Python’s built-in `sqlite3`)
- **Frontend**: HTML, CSS (with separate `main.css` and `admin.css`)
- **Templates**: Jinja2 (extends `base.html` for consistent layout)

---

## 📂 Project Structure

campaignhub/
├── app.py                                # Main Flask app
├── campaignhub.db                # SQLite database
├── static/               # Public static files
│   ├── css/
│   │   ├── main.css
│   │   └── admin.css
│   └── images/
├── templates/
│   ├── base.html
│   ├── pages/
│   │   ├── home.html
│   │   ├── services.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   ├── consultation.html
│   │   ├── login.html
│   │   └── admin.html
└── README.md

Code

---

## ⚙️ Setup & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/karthi1329/campaignhub.git
   cd campaignhub
Install dependencies:

bash
pip install -r requirements.txt
Run the app:

bash
python app.py
The app will start at http://127.0.0.1:5000/.

Access the admin dashboard:

Visit /login

Use credentials:
Username: admin  
Password: admin123
