import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("malathidevara", "password")
message = "hello"
problems = server.sendmail("malathidevara@gmail.com","targetreciever" , message)
server.quit()

