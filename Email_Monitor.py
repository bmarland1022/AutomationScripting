import pyautogui as pa
import pytesseract as pt
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Responsible for monitoring if MainBotFunction is running. 
# Checks every couple seconds and will send an email to my phone if an error has occured, so I can come manually restart the script.

# Send an email to my phone
def send_email():
    sender_email = 'emailmonitorpy@gmail.com'
    receiver_email = 'AlertBenMarland@outlook.com'
    password = '******************'

    subject = 'RED ALERT: FIX NOW - COMPUTER 2'
    body = 'Computer 2 Code has stopped running.'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(message)
    server.quit()

# Monitors the main bot function based upon a pixel screen grab. If the script is currently running do nothing, otherwise send an email.
def monitor_main_bot():
    error_occurred = False
    email_sent = False  # Flag to track if email has been sent
    time.sleep(25)
    while True:
        screenshot31 = pa.screenshot(region=(3458, 122, 309, 143))
        grayscale_image31 = screenshot31.convert('L')
        monitor_text = pt.image_to_string(grayscale_image31)
        if 'MainBotCode' in monitor_text:
            pass
        else:
            send_email()
            break  # End the script after sending the email

        # Sleep for 5 seconds before checking again
        time.sleep(10)

# Call the monitor_main_bot function to start monitoring
monitor_main_bot()
