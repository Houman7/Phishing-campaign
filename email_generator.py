import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SMTP_SERVER = 'Your.smtp_service.net' # replace with smtp service
SMTP_PORT = 587
SMTP_USERNAME = 'apikey'  # replace with smtp service username
SMTP_PASSWORD = 'Actual_api_key'  # replace with smtp service api key
FROM_EMAIL = 'you@YourDomain.com'  # replace with verified sender from smtp service
SUBJECT = 'ѕесuritу Аlert'


HTML_TEMPLATE = """
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6;">
<p>Hello,</p>

<p>Your account will be terminated in 14 days if necessary action is not taken.</p>

<p>To continue, please verify via the secure portal:  
<a href="{link}">https://login.amazon.com/security</a></p>


<p>Thanks,<br>
IT Support Team</p>

<hr>
<small>This is an automated message from our security operations center.</small>
</body>
</html>
"""


def send_simulation_email(to_email, link):
    msg = MIMEMultipart('alternative')
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = SUBJECT
    html_content = HTML_TEMPLATE.format(link=link)
    msg.attach(MIMEText(html_content, 'html'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, to_email, msg.as_string())
        server.quit()
        print(f" Sent to {to_email}")
    except Exception as e:
        print(f" Failed to send to {to_email}: {e}")





if __name__ == "__main__":
    emails = ['targets@gmail.com'] # replace with target emails
    link = 'Your_domain.com' # replace with landing page url
    for email in emails:
        send_simulation_email(email, link)

