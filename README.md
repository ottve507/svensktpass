# Svenskt pass
A python webscraper that supports in booking a time to renew your Swedish passport. It is a simple scripts that goes through all the steps of the booking for you. It continuously looks for time slots and books the first best time. The only input required from the user is the log-in with mobile bank ID. Just scan the QR code that will be shown by the browser and the script will take care of the rest.

## Required software:
1. Python3
2. Selenium for python
3. Chromium driver for your chrome browser (check your version of chrome, then download the correct version here: https://chromedriver.chromium.org/downloads)

## Explanation of files
chromedriver.exe - Example of a chromedriver - should be replaced
main.py - The start of software and where you input information about you and your booking
pass_booking.py - File contains all the logic to perform the booking

## Set up
Change the values in "main.py":
1) E-mail
2) Phone number
3) The earliest time you want to book your passport
4) The latest time you want to book your pasport
5) Location of your downloaded chromedriver
6) Optional: Location of region where you would like to book a time (E.g. https://bokapass.nemoq.se/Booking/Booking/Index/stockholm for Stockholm, https://bokapass.nemoq.se/Booking/Booking/Index/gotland for Gotland)

## Run the damn thing
Prepare your mobile ID so that you can scan the QR code.

Start the booking process by running in the terminal:
```python
python3 main.py
```

Scan the QR code and let the script look for a time. Once it finds a time, an e-mail will be sent to you confirming the booking. A print screen of the booking will also be saved in the folder where you ran the script.
