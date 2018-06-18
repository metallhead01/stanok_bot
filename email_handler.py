import imaplib
import email
import smtplib
import time


# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

# Just enable 2-step verification on your account.
# Then generate one App-Specific-Password and use that to connect instead of your original password.

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "jamies.italian.it" + ORG_EMAIL
FROM_PWD    = "zpjfzquiexnbnzau"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()

        for i in reversed(id_list):
            typ, data = mail.fetch(i, '(RFC822)')

            for response_part in data:
                if isinstance(response_part, tuple):
                    print(email.message_from_string)
                    msg = email.message_from_string(response_part[1].decode('utf-8'))
                    # print
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')

    except Exception as e:
        print(str(e))


read_email_from_gmail()
