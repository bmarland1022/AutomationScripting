import pyautogui as pa
import time
import pytesseract as pt

# Responsible for directing a follower bot to join the giveaway when the main bot has found a giveaway and entered. The follower bot joins and also monitors if it wins the giveaway.
# The code for each follower bot is the same, just with different pixel location, thus this is the only follower bot code shown.

# The follower bots function to join the giveway
def joining_givvy1():
    global topf1
    global start_time17
    global end_time17
    p2000 = pa.pixel(1092, 143)
    p2001 = pa.pixel(1152, 140)
    if all(color != (255, 255, 255) for color in [p2000, p2001]):
        leaving()
    with open("streamer.txt", "r") as file:
        streamer_name1 = file.read()
    pa.moveTo(970, 144, 1)
    pa.click()
    check1 = test_givvy_winner()
    if check1 == 15:
        return 15
    time.sleep(.5)
    streamer_name = streamer_name1.rstrip('\n')
    pa.typewrite(streamer_name, interval=0)
    check2 = test_givvy_winner()
    if check2 == 15:
        return 15
    time.sleep(3)
    check3 = test_givvy_winner()
    if check3 == 15:
        return 15
    ghj = location_click()
    check4 = test_givvy_winner()
    if check4 == 15:
        return 15
    if ghj == 15:
        return 15
        #Fail Safe if not found
        #Hit x and skip to next bot and wait for next givvy
        #Could need restart so throw in there
    if ghj == 10:
        time.sleep(1)
        pa.moveTo(963, 276, 1)
        pa.click()
    else:
        pa.moveTo(833, 482, 1)
        pa.click()
    check5 = test_givvy_winner()
    if check5 == 15:
        return 15
    start1_time = time.time()
    end1_time = start1_time + 5  # 5 seconds
    while time.time() < end1_time:
        pf101 = pa.pixel(988, 1180)
        pf102 = pa.pixel(994, 1163)
        pf103 = pa.pixel(1022, 1895)
        if all(color == (0, 0, 0) for color in [pf101, pf102, pf103]):
            time.sleep(1.5)
            check7 = test_givvy_winner()
            if check7 == 15:
                return 15
            pa.moveTo(997, 991, 1)
            pa.click()
            time.sleep(1)
            check8 = test_givvy_winner()
            if check8 == 15:
                return 15
            thy = active()
            if thy == 15:
                return 15
            return
        check6 = test_givvy_winner()
        if check6 == 15:
            return 15
    time.sleep(.1)

# Routing check to make sure the follower bot is at the right stage of the script, makes sure the
# app didn't crash at some point.
def location_click():
    global topf1
    global checkfound
    global f
    global start_time18
    global end_time18
    screenshotpic = pa.screenshot(region=(752, 283, 40, 18))
    grayscale_pic = screenshotpic.convert('L')
    follow1_text = pt.image_to_string(grayscale_pic)
    if 'Live' in follow1_text:
        return 10
    else:
        checkfound = 0
        y = 251
        start_time18 = time.time()
        end_time18 = start_time18 + 10  # 5 seconds
        while time.time() < end_time18:
            for _ in range(12):  # Adjust the number of iterations as needed
                screenshot15 = pa.screenshot(region=(693, y, 221, 47))
                grayscale_image15 = screenshot15.convert('L')
                loc_text = pt.image_to_string(grayscale_image15)
                if 'View all' in loc_text or 'results for' in loc_text or 'all results' in loc_text:
                    topf1 = y + 20
                    time.sleep(5)
                    pa.moveTo(1000, topf1, 1)
                    pa.click()
                    time.sleep(1)
                    return topf1
                check15 = test_givvy_winner()
                if check15 == 15:
                    return 15
                y += 62
        checkfound = 1
    #If gets to this point then skip to next bot

# Determines if the giveaway is still active while the bots are all attempting to join the giveaway
def active():
    global start_time19
    global end_time19
    pa.moveTo(1000,1000,1)
    pa.click()
    p001 = pa.pixel(964, 2329)
    p002 = pa.pixel(1259, 2327)
    start_time19 = time.time()
    end_time19 = start_time19 + 4  # 5 seconds
    while time.time() < end_time19:
        check10 = test_givvy_winner()
        if check10 == 15:
            return 15
        screenshot = pa.screenshot(region=(945, 2312, 338, 38))
        grayscale_image = screenshot.convert('L')
        givvy_text = pt.image_to_string(grayscale_image)
        if 'Enter' in givvy_text or 'Follow' in givvy_text or 'Giveaway' in givvy_text:
            pa.moveTo(1109, 2325, .5)
            pa.click()
            return

# The follower bot's function to leave the giveaway
def leaving():
    pa.moveTo(987, 1064, 1)
    pa.click()
    time.sleep(1)
    pa.click()
    pa.moveTo(1261, 137, 1)
    pa.click()
    start_time = time.time()
    end_time = start_time + 8  # 5 seconds
    while time.time() < end_time:
        p1000 = pa.pixel(1054, 142)
        p1001 = pa.pixel(1150, 2216)
        if all(color == (255, 255, 255) for color in [p1000, p1001]):
            time.sleep(1.7)
            break
        time.sleep(.25)
    pa.moveTo(996, 142, 1)
    pa.click()
    pa.moveTo(1157, 142, 1)
    pa.click()
    p301 = pa.pixel(1116, 145)
    p302 = pa.pixel(833, 890)
    p303 = pa.pixel(777, 1570)
    p304 = pa.pixel(1202, 1535)
    if all(color == (255, 243, 81) for color in [p302]) and all(color == (2, 6, 35) for color in [p303, p304]):
        time.sleep(3.5)
        pa.moveTo(829, 877, 1)
        pa.click()
        time.sleep(10)
        pa.moveTo(838, 2302, 1)
        pa.click()
        pa.moveTo(933, 143, 2.5)
        pa.click()
    if all(color != (255, 255, 255) for color in [p301]):
        leaving()

# Determines if this bot won the giveaway based upon a popup that would occur
def test_givvy_winner():
    p61 = pa.pixel(50, 1148)
    p62 = pa.pixel(50, 1311)
    p63 = pa.pixel(560, 1311)
    p64 = pa.pixel(560, 1148)
    if all(color == (255, 255, 255) for color in [p61, p62, p63, p64]):
        return 15

# Check that the follower bot joined
def check_join1():
    screenshot = pa.screenshot(region=(709, 2179, 567, 73))
    grayscale_image = screenshot.convert('L')
    checktext = pt.image_to_string(grayscale_image)
    if 'To purchase in lives we need your payment' in checktext:
        pa.moveTo(983, 1118, 1)
        pa.click()
        active()

