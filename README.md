The purpose of this project is to interact with a web platform and handle event-based participation systems utilizing Python Scripts.

The main python modules used were pyautogui, pytesseract, Google's speech_recognition, and Python's email module

The project contains 4 main Python scripts

1.) MainBotFunctions.py
- Responsible for locating a giveaway, calling follower bot functions to join the giveaway, and determining the winner of the giveaway

2.) AudioTest.py 
- Responsible for capturing the audio after a giveaway win. Loops the output audio back into the computer, then uses Google's speech recognition module to translate the text every few seconds. Then will respond with a random prewritten response prompt based upon a few select keywords.
- Captures audio for the duration, and every few seconds during that capture will translate the text and search for the keywords.
- (Not included, AudioTestFollower scripts, which are the same as the AudioTest script except a different location for the response text is chosen, which is based upon the app location on the computer screen.)

3.) FollowerBot.py
- Responsible for directing a follower bot to join the giveaway when the main bot has found a giveaway and entered. The follower bot joins and also monitors if it wins the giveaway.
- The code for each follower bot is the same, just with different pixel location, thus this is the only follower bot code shown.

4.) Email_Monitor.py
- Responsible for monitoring if MainBotFunction is running. Checks every couple seconds and will send an email to my phone if an error has occured, so I can come manually restart the script.

** Note: this was written for personal gain with no thought given into variable names or code conciseness at the time.
