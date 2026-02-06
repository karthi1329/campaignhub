import sqlite3
from flask import Flask, render_template, request, flash, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # required for flash messages and sessions

# --- Database setup ---
def init_db():
    conn = sqlite3.connect("campaignhub.db")
    c = conn.cursor()

    # Table for contact messages
    c.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    """)

    # Table for consultation requests
    c.execute("""
        CREATE TABLE IF NOT EXISTS consultations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            details TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

# Initialize database when app starts
init_db()


@app.route("/")
def home():
    return render_template("pages/home.html")


@app.route("/services")
def services():
    return render_template("pages/services.html")


@app.route("/about")
def about():
    return render_template("pages/about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Save to SQLite
        conn = sqlite3.connect("campaignhub.db")
        c = conn.cursor()
        c.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        conn.commit()
        conn.close()

        flash("We received your message. Our team will get back to you soon!")
        return redirect(url_for("contact"))

    return render_template("pages/contact.html")


@app.route("/consultation", methods=["GET", "POST"])
def consultation():
    if request.method == "POST":
        service = request.form.get("service")
        details = request.form.get("details")

        # Save to SQLite
        conn = sqlite3.connect("campaignhub.db")
        c = conn.cursor()
        c.execute("INSERT INTO consultations (service, details) VALUES (?, ?)", (service, details))
        conn.commit()
        conn.close()

        flash(f"We received your request for {service}. Our team will contact you soon!")
        return redirect(url_for("consultation"))

    return render_template("pages/consultation.html")


# --- Admin workflow ---
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Simple hardcoded login (replace with secure auth later)
        if username == "admin" and password == "admin123":
            session["is_admin"] = True
            return redirect(url_for("admin"))
        else:
            flash("Invalid credentials")
            return redirect(url_for("login"))

    return render_template("pages/login.html")


@app.route("/logout")
def logout():
    session.pop("is_admin", None)
    flash("You have been logged out.")
    return redirect(url_for("login"))


@app.route("/admin")
def admin():
    if not session.get("is_admin"):
        flash("Please log in to access the admin dashboard.")
        return redirect(url_for("login"))

    # Fetch data from database
    conn = sqlite3.connect("campaignhub.db")
    c = conn.cursor()

    c.execute("SELECT id, name, email, message FROM contacts ORDER BY id DESC")
    contacts = c.fetchall()

    c.execute("SELECT id, service, details FROM consultations ORDER BY id DESC")
    consultations = c.fetchall()

    conn.close()

    return render_template("pages/admin.html", contacts=contacts, consultations=consultations)


if __name__ == "__main__":
    app.run(debug=True)
