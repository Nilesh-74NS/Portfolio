from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# =========================
# Gmail Configuration
# =========================

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sonavanenilesh7499@gmail.com'
app.config['MAIL_PASSWORD'] = 'ubyrgcrmosjszyri'

mail = Mail(app)

# =========================
# Routes
# =========================

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/certificates')
def certificates():
    return render_template('certificates.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# =========================
# Contact Form Submit
# =========================

@app.route('/send', methods=['POST'])
def send():

    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    msg = Message(
        subject=f'Portfolio Contact: {subject}',
        sender=app.config['MAIL_USERNAME'],
        recipients=['yourgmail@gmail.com']
    )

    msg.body = f"""
Name: {name}

Email: {email}

Subject: {subject}

Message:
{message}
"""

    mail.send(msg)

    return "Message Sent Successfully"

# =========================
# Run App
# =========================

if __name__ == '__main__':
    app.run(debug=True)