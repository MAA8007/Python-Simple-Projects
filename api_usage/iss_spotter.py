#This code will alert me when the ISS is directly above (or near) my house.

from time import time
import requests, smtplib
from datetime import datetime
lats= []
longs = []
ye = 0 
yea=1
MY_LAT = 24.815193
 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

iss_latitude= int(iss_latitude)
iss_longitude=int(iss_longitude)
#Your position is within +5 or -5 degrees of the ISS position.
my_lat_range_min= int(MY_LAT-5)
my_lat_range_max= int(MY_LAT+5)

my_long_range_min= int(MY_LONG-5)
my_long_range_max= int(MY_LONG+5)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunset)
time_now = datetime.now()
print(time_now)

for x in range(my_lat_range_min,my_lat_range_max+1):
    lats.append(x)
for x in range(my_long_range_min,my_long_range_max+1):
    longs.append(x)

if iss_latitude in range(my_lat_range_min,my_lat_range_max+1) and iss_longitude in range(my_long_range_min,my_long_range_max+1):
    ye = 1

if time_now>sunset and time_now<sunrise:
    yea= 1

if ye==1 and yea==1:
    my_email = "xyz@gmail.com"
    my_password = "xyz"
    time.sleep(60)
    with smtplib.SMTP("smpt.mail.gmail.com") as connection:
        connection.starttls()
        connection.tls(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="xyz@yahoo.com",
            msg="Hey, the ISS is now visible at your location!"
        )



