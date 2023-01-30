import smtplib

my_email = "testemail123@gmail.com"
password = "Password123^&*"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="testemail123@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of email")
