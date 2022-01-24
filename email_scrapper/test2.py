import imaplib
import email
import traceback
import datetime

ORG_EMAIL = "@inspecthoa.com"
FROM_EMAIL = "ajit" + ORG_EMAIL
FROM_PWD = "A1j2i3t45s"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993


def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id, first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)')
            # print(data)
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1], 'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    # body = msg['message']
                    # print(body)
                    # file = msg['filename']
                    # print(msg)
                    # print('From : ' + email_from + '\n')
                    # print('Subject : ' + email_subject + '\n')
                    print("Body : ")
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain" or part.get_content_type() == 'test/html':
                            body = part.get_payload(decode=True)
                            print(body)
                            # body_lines = part.as_string().split("\n")
                            # print("\n".join(body_lines[:12]))

                        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
                            filename = str(round(datetime.datetime.now().timestamp()))
                            open(filename + '.pdf', 'wb').write(part.get_payload(decode=True))

    except Exception as e:
        traceback.print_exc()
        print(str(e))


read_email_from_gmail()
