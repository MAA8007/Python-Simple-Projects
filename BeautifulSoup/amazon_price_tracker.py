from curses.ascii import isdigit
import bs4, requests, smtplib
from bs4 import BeautifulSoup
headers = { 'Accept-Language' : "en-US,en;q=0.9",
            'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
link = input("enter the link")
response = requests.get(link, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
price = str(soup.find(class_="a-price-whole"))
digits=[]


targetprice= int(input('Enter target price'))

def emailalert():
    my_email = "xyz@gmail.com"
    my_password = "xyz"

    with smtplib.SMTP("smpt.mail.gmail.com") as connection:
        connection.starttls()
        connection.tls(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="xyz@yahoo.com",
            msg="hello"
        )



for x in price:
    if x.isdigit():
        digits.append(x)
print(digits)
finalprice=int(''.join(digits))
if finalprice < targetprice:
    emailalert()
print(finalprice)

