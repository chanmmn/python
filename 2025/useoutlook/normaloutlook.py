import win32com.client as win32

def send_outlook_email(to, subject, body, cc=None, attachments=None):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject
    mail.Body = body
    if cc:
        mail.CC = cc
    if attachments:
        for file in attachments:
            mail.Attachments.Add(file)
    mail.Send()

# Example usage:
if __name__ == "__main__":
    send_outlook_email(
        to="anyemail@gmail.com",
        subject="Test Email from Python",
        body="This is a test email sent from Python using Outlook.",
        cc=None,
        attachments=None
    )
