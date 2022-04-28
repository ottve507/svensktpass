from pass_booking import PassBooking
import time
import traceback
import json
from datetime import datetime

         
#Info required
email_text = "YOUR@EMAIL.COM"
tel = "07213371337"
early_time = datetime.strptime("2022-04-29 08:20:00", '%Y-%m-%d %H:%M:%S')
late_time = datetime.strptime("2022-05-20 08:20:00", '%Y-%m-%d %H:%M:%S')
location_of_driver = r"C:\Users\my_user\Documents\chromedriver.exe" # Might neeed to redo for mac.
start_page_to_look_for_time_slots = "https://bokapass.nemoq.se/Booking/Booking/Index/stockholm"


def main():
    booker.go_to_police()


#Initialize booker class
booker = PassBooking(early_time, late_time, email_text, tel, location_of_driver, start_page_to_look_for_time_slots)

#Start program
main()