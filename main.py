from pass_booking import PassBooking
import time
import traceback
import json
from datetime import datetime

         
######Info required######
email_text = "mailforthe@booking.com"
tel = "0721234567"
early_time = datetime.strptime("2022-04-29 08:20:00", '%Y-%m-%d %H:%M:%S')
late_time = datetime.strptime("2022-05-20 08:20:00", '%Y-%m-%d %H:%M:%S')
location_of_chrome_driver = r"C:\Users\otto.velander\Documents\scrapefun\chromedriver.exe" # Might neeed to redo for mac.
start_page_to_look_for_time_slots = "https://bokapass.nemoq.se/Booking/Booking/Index/stockholm"
number_of_people = 3 #minimum one person

#Additional people (excluding person who is using the bank ID)                                         
person2 = {'firstname': "EXTRA #1 (FIRST NAME)", 'lastname': "EXTRA #1 (LAST NAME)", 'personnummer': 'EXTRA #1 (PERSONNUMMER)'}
person3 = {'firstname': "EXTRA #2 (FIRST NAME)", 'lastname': "EXTRA #2 (LAST NAME)", 'personnummer': 'EXTRA #2 (PERSONNUMMER)'}
personarray = [person2, person3] #put all the additional people in. If no additional people set to: personarray = []
######Info required (END)######

def main():
    booker.go_to_police()


#Initialize booker class
booker = PassBooking(early_time, late_time, email_text, tel, location_of_chrome_driver, start_page_to_look_for_time_slots, number_of_people, personarray)

#Start program
main()