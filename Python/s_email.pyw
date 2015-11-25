def send_email():
            import smtplib 
			
            gmail_user = "santiago@susqu.edu"
            gmail_pwd = "Navicula115"
            FROM = 'santiago@susqu.edu'
            TO = ['santiago@susqu.edu'] #must be a list
            SUBJECT = "Annie Social"
            TEXT = open('log_file.txt', 'r').read()

            # Prepare actual message
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:
                #server = smtplib.SMTP(SERVER) 
                server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                #server.quit()
                server.close()
                print 'successfully sent the mail'
            except:
                print "failed to send mail"

send_email()