from flask import Flask,render_template,request
from flask_mail import Mail,Message
import os
import dotenv

dotenv.load_dotenv()

app=Flask(__name__)

app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=465
app.config["MAIL_USERNAME"]=os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"]=os.getenv("MAIL_PASSWORD")
app.config["MAIL_USE_TLS"]=False
app.config["MAIL_USE_SSL"]=True

mail=Mail(app)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    to_address = request.form.get("to")
    subject = request.form.get("subject")
    content = request.form.get("content")

    msg = Message(
        subject=subject,
        sender = os.getenv("MAIL_USERNAME"), 
        recipients=[to_address],
        body=content
    )

    mail.send(msg)
    return render_template("index.html")


app.run(debug=True)