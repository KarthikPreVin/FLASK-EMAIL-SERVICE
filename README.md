## Flask Mail Dispatcher

A streamlined Flask web application that allows users to send emails through Gmail's SMTP server using a simple web interface.

---

### Setting up this in your local machine

Follow these steps to set up the project on your local machine.

#### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <repository-folder>

```

#### 2. Install Dependencies

Ensure you have Python installed, then install the required packages:

```bash
pip install -r requirements.txt

```

#### 3. Environment Configuration

Create a `.env` file in the **root folder** of the project to store your credentials securely:

```env
MAIL_USERNAME = "your_email@gmail.com"
MAIL_PASSWORD = "your_16_character_app_password"

```

---

### Gmail SMTP Setup (App Passwords)

Since Google does not allow using your primary password for third-party apps, you must generate an **App Password**.

1. **Enable 2-Step Verification:** Go to your [Google Account Security](https://myaccount.google.com/security) and ensure 2-Step Verification is turned **ON**.
2. **Generate App Password:** Go to the [App Passwords](https://myaccount.google.com/apppasswords) section.
3. **Create:** Select 'Mail' and 'Other (Custom name)', then click **Generate**.
4. **Copy:** Copy the **16-character string** provided.
5. **Configure:** Paste this string into the `MAIL_PASSWORD` value in your `.env` file.
* *Note: The password should be 16 characters with no spaces.*



---

### Running the App

1. Run the application:
```bash
python app.py

```

2. Open your browser and navigate to `http://127.0.0.1:5000`.
3. Fill out the form (To Address, Subject, and Content) and click submit to send your email.

---

### Project Structure

* `app.py`: The main Flask application logic.
* `.env`: Secret environment variables (ignored by git).
* `templates/index.html`: The frontend form for user input.
