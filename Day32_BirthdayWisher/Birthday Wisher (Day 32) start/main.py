import smtplib

my_email = "testemail123@gmail.com"
password = "Password123^&*"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= my_email, password = password)
connection.sendmail(from_addr=my_email, to_addrs="testemail123@gmail.com", msg="Hello")
connection.close()