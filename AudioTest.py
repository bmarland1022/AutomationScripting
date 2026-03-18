import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyautogui as pa
import time
import random
import pytesseract as pt

# Responsible for capturing the audio after a giveaway win. Loops the output audio back into the computer, then uses Google's speech recognition module to
# translate the text every few seconds. After will respond with a random prewritten response prompt based upon a few select keywords.
# Captures audio for the duration, and every few seconds during that capture will translate the text and search for the keywords.

# Set the total duration for capturing audio (in seconds)
duration = 40

def speech_to_text(duration):
    global text
    global aa
    global bb
    global cc
    global dd
    global top
    global y
    reset_val()
    rt = location()
    if rt == 200:
        return

    device_index = 1  # Loopback audio device index
    chunk_duration = duration // 8
    
    # Runs the translation for the duration broken up into 5 second segments. 
    # Allows responses to be given in between the live translation
    # Threading would have been a more optimal option, but was beyond my capabilities at the time
    for _ in range(8):
        
        # Code taken from YouTube tutorials for audio capture, this part. I found out to loop audio back into computer,
        # Needed some assistance figuring out how to capture the audio for translation
        audio = sd.rec(int(chunk_duration * 44100), samplerate=44100, channels=2, blocking=True, dtype="float32",
                       device=device_index)
        output_file = "captured_audio.wav"
        sf.write(output_file, audio, 44100)
        
        # Run givvy_responses() once in the loop
        if _ == 0:
            def_givvy_responses()
        r = sr.Recognizer()
        with sr.AudioFile(output_file) as source:
            audio_data = r.record(source)
        try:
            # Perform speech recognition on the captured audio
            text = r.recognize_google(audio_data, show_all=False)
            poke_responses()
        except sr.UnknownValueError:
            pass
# Call the speech_to_text function with the specified duration

# Responses based upon on keywords 
def poke_responses():
    global top
    global text
    global aa
    global bb
    global cc
    global dd
    if aa == 0:
        if 'rip or ship' in text or 'or ship' in text or 'ship or rip' in text or 'or ripped' in text or 'or shipped' in text or 'ripped or' in text or 'shipped or' in text or 'ripping or' in text or 'shipping or' in text or 'or ripping' in text or 'or shipping' in text or 'rip it' in text or 'ship it' in text or 'ripping it' in text or 'shipping it' in text or 'rip' in text:
            aaa = rip_ship()
            location_still()
            pa.moveTo(75, top, 1)
            pa.click()
            pa.typewrite(aaa)
            time.sleep(1)
            aa = 1
            print('ripship initiated')
    if bb == 0:
        if 'pick a number' in text or 'number between' in text or 'number from' in text or 'choose a number' in text:
            bbb = pick_num()
            location_still()
            pa.moveTo(75, top, 1)
            pa.click()
            pa.typewrite(bbb)
            time.sleep(1.5)
            bb = 1
            print('number initiated')
    if cc == 0:
        if 'bulk' in text or 'just hits' in text or 'only hits' in text:
            ccc = bulk()
            location_still()
            pa.moveTo(75, top, 1)
            pa.click()
            pa.typewrite(ccc)
            time.sleep(1.5)
            cc = 1
            print('bulk initiated')
            
# Prewritten responses that will get randomly selected
def rip_ship():
    choose_resp1 = random.choice(['Ship please', 'Can I get that shipped', "Ship if you don't mind", "Ship, thank you", "Ship thanks", "Please ship ty", 'ship please', 'Ship', 'Ship ty'])
    return choose_resp1

# Random number selector
def pick_num():
    pick_a_num = random.randint(1, 10)
    return pick_a_num

# Prewritten responses that will get randomly selected
def bulk():
    choose_resp2 = random.choice(['Bulk too please', 'Bulk please :)','Bulk ty','Send bulk please ty','Can I get the bulk','Bulk thanks', 'Bulk thank you'])
    return choose_resp2

# Runs the audio for the specified duration
def run_audio():
    speech_to_text(duration)

# Runs default response if none of keywords are selected
def def_givvy_responses():
    global top
    time.sleep(2)
    location_still()
    pa.moveTo(75, top, 1)
    pa.click()
    time.sleep(1.5)
    zzzzz = default_response()
    pa.typewrite(zzzzz)
    pa.press('enter')
    print('Default Response')

#  Prewritten responses that will get randomly selected
def default_response():
    choose_resp3 = random.choice(['Lfg thanks','Omg thank you wow','Wow lfg thanks','Thank you :)','Awesome thanks','Awesome thank you','Awesome ty','Lfg thank you','Lfg ty','Omg thanks','Omg tysm awesome', 'LFG','LFG thanks','Gg thanks','Gg thank you'])
    return choose_resp3

# Resets global variables, which are updated in loop
def reset_val():
    global text
    global aa
    global bb
    global cc
    global dd
    global top
    text = 0
    aa = 0
    bb = 0
    cc = 0
    dd = 0
    
#Finds location of the text chat, which can vary based upon length of streamer description.
def location():
    global y
    global top
    y = 2080
    start_time = time.time()
    end_time = start_time + 120  # 120 seconds
    while time.time() < end_time:
        for _ in range(68):  # Adjust the number of iterations as needed
            screenshot = pa.screenshot(region=(18, y, 135, 30))
            grayscale_image = screenshot.convert('L')
            main_text = pt.image_to_string(grayscale_image)
            if 'Say Something' in main_text:
                top = y + 16
                return top
            y += 10
        pa.moveTo(260, 1017, 1)
        pa.click()
        time.sleep(.5)
        pa.click()
        location()
    return 200

# Checks if location of text chat is at the same location
def location_still():
    global y
    screenshot2 = pa.screenshot(region=(18, y, 135, 30))
    grayscale_image2 = screenshot2.convert('L')
    main_text2 = pt.image_to_string(grayscale_image2)
    if 'Say Something' in main_text2:
        pass
    else:
        location()
