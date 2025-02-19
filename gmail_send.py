import smtplib, ssl
from email.mime.text import MIMEText
#上で作成したpyファイルから、account情報を読み込みます
import my_gmail_account as gmail

# 送信先のアドレスを登録します
send_address = ""

# メインの関数になります
def send_test_email(text):
  msg = make_mime_text(
    mail_to = send_address,
    subject = text,
    body = text
  )
  send_gmail(msg)

# 件名、送信先アドレス、本文を渡す関数です
def make_mime_text(mail_to, subject, body):
  msg = MIMEText(body, "html")
  msg["Subject"] = subject
  msg["To"] = mail_to
  msg["From"] = gmail.account
  return msg

# smtp経由でメール送信する関数です
def send_gmail(msg):
  server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context = ssl.create_default_context())
  server.set_debuglevel(0)
  server.login(gmail.account, gmail.password)
  server.send_message(msg)

