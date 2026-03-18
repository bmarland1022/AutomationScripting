import pyautogui as pa
import time
import pytesseract as pt
import random
import AudioTest as at
import AudioTestFollower1 as at1
import AudioTestFollower2 as at2
import AudioTestFollower3 as at3
import AudioTestFollower4 as at4
import FollowerBot1 as fb1
import FollowerBot2 as fb2
import FollowerBot3 as fb3
import FollowerBot4 as fb4
import datetime

# This program contains most of the main bot functions
# Responsible for locating a giveaway, calling follower bot functions to join the giveaway, and determining the winner of the giveaway

# Determines if a giveaway is going on right now or the streamer is currently selling something based upon text
def read_givvy():
    global h
    h = 0
    global k
    k = 0
    flag1 = False
    flag = 0
    f = 0
    g = 0
    start_time = time.time()
    end_time = start_time + .35  # 5 seconds
    result_int_show_left = 0  # For Checking if int_show is called
    while time.time() < end_time:
        screenshot = pa.screenshot(region=(304, 2315, 270, 35))
        grayscale_image = screenshot.convert('L')
        givvy_text = pt.image_to_string(grayscale_image)
        screenshot.save('function1_screenshot.png')
        if ('Enter' in givvy_text or 'Follow' in givvy_text or 'Giveaway' in givvy_text) and 'How' not in givvy_text:
            flag1 =True
            flag = 1
            break
        time.sleep(.1)
    if flag1:
        pa.moveTo(420, 2326, 1)
        pa.click()
        time.sleep(1)
        givvy_name()
        k = 5
    if flag == 0:
        pa.moveTo(571, 136, 1)
        pa.click()
        time.sleep(1)
        h = 4

# Public flags set for use in every function
flagg = True
pa.FAILSAFE = False

# Common popup check to determine if the program is at the right stage in the script, for the international streamer show popup
def int_show():
    result10 = 0
    p41 = pa.pixel(502, 1102)
    p42 = pa.pixel(506, 1354)
    p43 = pa.pixel(107, 1346)
    p44 = pa.pixel(195, 1117)
    p45 = pa.pixel(96, 1172)
    if all(color == (255, 255, 255) for color in [p41, p42, p43, p44, p45]):
        start_time = time.time()
        end_time = start_time + 1.5  # 5 seconds
        while time.time() < end_time:
            screenshot = pa.screenshot(region=(195, 1188, 217, 37))
            grayscale_image = screenshot.convert('L')
            int_text = pt.image_to_string(grayscale_image)
            screenshot.save('int_show.png')
            if 'International' in int_text or 'Show' in int_text:
                pa.moveTo(204, 1290,.5)
                pa.click()
                result10 = 2
                return result10
            time.sleep(.3)

# Scrolls down a set amount on the main select a streamer to view page
def scroll_third_down():
    pa.moveTo(303, 1146, .5)
    pa.mouseDown()
    time.sleep(.5)
    pa.moveTo(304, 961, .5)
    pa.mouseUp()
    time.sleep(.5)

# Scrolls down a set amount on the main select a streamer to view page
def scroll_one_down():
    pa.moveTo(306, 1610, .5)
    pa.mouseDown()
    time.sleep(.5)
    pa.moveTo(307, 1057, .5)
    pa.mouseUp()
    time.sleep(.5)

# Scrolls down a set amount on the main select a streamer to view page
def scroll_two_down():
    pa.moveTo(303, 2150, .7)
    pa.mouseDown()
    time.sleep(.6)
    pa.moveTo(304, 1050, .7)
    pa.mouseUp()
    time.sleep(.6)

# Pulls up scroll page after from main page when loaded in
# Fail safe checking on right screen halfway through
# If not reopens whatnot
def pull_up_scroll_page():
    global flagg
    flag = False
    pa.moveTo(59, 2330, 1.1)
    pa.click()
    time.sleep(2.5)  # Need to change time here when underway potential lag
    pa.moveTo(333, 314, 1)
    pa.click()
    time.sleep(2.5)
    pa.moveTo(106, 369, 1)
    pa.click()
    time.sleep(1)
    pa.moveTo(293, 1437, 1)
    pa.click()
    time.sleep(1)
    screenshot16 = pa.screenshot(region=(276, 2249, 150, 35))
    grayscale_image16 = screenshot16.convert('L')
    future_text16 = pt.image_to_string(grayscale_image16)
    if 'Show Results' not in future_text16:
        pa.moveTo(569, 137, 1)
        pa.click()
        time.sleep(3)
        reopen()
    pa.moveTo(336, 2264, 1)
    pa.click()
    time.sleep(1)
    scroll_one_down()
    scroll_two_down()
    scroll_two_down()
    check_time()
    flagg = True

#Reopen Whatnot and then also runs
# function pull_up_page
# This is called to get back to the main page of the app
def reopen():
    global flagg
    flagg = False
    zz = 0 #Temp Fix
    zz = givvy_name()
    ddddd = 0
    ddddd = reopen_check()
    if 'Search' not in zz and len(zz) > 1 and ddddd != 100:
        pa.moveTo(309, 1019, 1)
        pa.click()
        pa.moveTo(571, 137, 1)
        pa.click()
    pa.moveTo(645,2317,1)
    pa.click()
    time.sleep(2)
    pa.moveTo(520, 130, 1)
    pa.click()
    time.sleep(3)
    pa.moveTo(140, 890,1) #Make sure all bots have whatnot in same spot on home screen
    pa.click()
    p11 = pa.pixel(139, 396)
    p12= pa.pixel(527, 1888)
    p13 = pa.pixel(47, 1881)
    p14 = pa.pixel(282, 375)
    p15 = pa.pixel(288, 1916)
    loading_screen_color = (0, 0, 0)
    time.sleep(.5)
    while not p11 and p12 and p13 and p14 and p15 == loading_screen_color:
        time.sleep(20)
    time.sleep(6)
    #pa.moveTo(145,2303,1)
    #pa.click()
    pull_up_scroll_page()

# Click on left stream location
# If it starts loading black screen then initiate giveaway test
# If it doesn't possibly out of loop so restart app
def click_stream_left():
    d = 0
    e = 0
    jjj = 0
    hhh = 0
    dddd = 0
    mmm = 0
    future_text30 = 0
    fghh1 = 0
    pa.moveTo(142, 1620, 1)
    pa.click()
    start_time = time.time()
    end_time = start_time + 3.5  # seconds
    result_int_show_left = 0  # For Checking if int_show is called
    while time.time() < end_time:
        p26 = pa.pixel(287, 1372)
        p27 = pa.pixel(540, 519)
        p28 = pa.pixel(317, 420)
        p29 = pa.pixel(24, 1110)
        p30 = pa.pixel(376, 1209)
        result_int_show_left = int_show()
        if result_int_show_left == 2:
            click_stream_right()
            return
        if all(color == (0, 0, 0) for color in [p26, p27, p28, p29, p30]):
            time.sleep(.5)
            pa.moveTo(294, 1148, .5)
            pa.click()
            time.sleep(1)
            jjj = ver_buy()
            if jjj == 4:
                return
            fghh1 = show_starts()
            if fghh1 == 1:
                time.sleep(2)
                reopen()
                return
            screenshot30 = pa.screenshot(region=(140, 238, 360, 80))
            grayscale_image30 = screenshot30.convert('L')
            future_text30 = pt.image_to_string(grayscale_image30)
            if 'Show starts in' in future_text30 or 'Show starting in' in future_text30 or 'Show starts soon' in future_text30:
                pa.moveTo(570,138,1)
                pa.click()
                d = 2
                return d
            else:
                read_givvy()
                e = 3
                return e
        time.sleep(.1)
    misclick()
    time.sleep(.5)
    lkmm = misclick2()
    if lkmm == 1:
        scroll_third_down()
        scroll_one_down()
        click_stream_right()
    dddd = list_an_item()
    if dddd == 1:
        return
    p101 = pa.pixel(413, 256)
    p102 = pa.pixel(520, 212)
    p103 = pa.pixel(566, 258)
    mmm = crash_prev()
    if mmm == 5:
        reopen()
        return
    if all(color != (255, 255, 255) for color in [p101, p102, p103]):
        pa.moveTo(570, 136)
        pa.click()
    list_an_item()
    scroll_third_down()

# Click on right stream location
# If it starts loading black screen then initiate giveaway test
# If it doesn't possibly out of loop so restart app
def click_stream_right():
    d = 0
    e = 0
    lll = 0
    lkmmm = 0
    dddd = 0
    mmm = 0
    fghh1 = 0
    future_text31 = 0
    pa.moveTo(441, 1619, 1)
    pa.click()
    start_time = time.time()
    end_time = start_time + 3.5  # 5 seconds
    result_int_show_right = 0 # For Checking if int_show is called
    while time.time() < end_time:
        p31 = pa.pixel(287, 1372)
        p32 = pa.pixel(540, 519)
        p33 = pa.pixel(317, 420)
        p34 = pa.pixel(24, 1110)
        p35 = pa.pixel(376, 1209)
        result_int_show_right = int_show()
        if result_int_show_right == 2:
            scroll_one_down()
            return
        if all(color == (0, 0, 0) for color in [p31, p32, p33, p34, p35]):
            time.sleep(.5)
            pa.moveTo(282, 1141, .5)
            pa.click()
            time.sleep(1)
            lll = ver_buy()
            if lll == 4:
                return
            fghh1 = show_starts()
            if fghh1 == 1:
                time.sleep(2)
                reopen()
                return
            screenshot31 = pa.screenshot(region=(140, 238, 360, 80))
            grayscale_image31 = screenshot31.convert('L')
            future_text31 = pt.image_to_string(grayscale_image31)
            if 'Show starts in' in future_text31 or 'Show starting in' in future_text31 or 'Show starts soon' in future_text31:
                pa.moveTo(319, 1066, 2.5)
                pa.click()
                pa.moveTo(570, 138, 1)
                pa.click()
                d = 2
                return d
            else:
                read_givvy()
                e = 3
                return e
        time.sleep(.1)
    misclick()
    time.sleep(.5)
    lkmmm = misclick2()
    if lkmmm == 1:
        scroll_third_down()
        scroll_one_down()
        click_stream_left()
    dddd = list_an_item()
    if dddd == 1:
        return
    p104 = pa.pixel(413, 256)
    p105 = pa.pixel(520, 212)
    p106 = pa.pixel(566, 258)
    mmm = crash_prev()
    if mmm == 5:
        reopen()
        return
    if all(color != (255, 255, 255) for color in [p104, p105, p106]):
        pa.moveTo(570, 136)
        pa.click()
    list_an_item()
    scroll_third_down()
# Runs finding stream and analyzing givvy or not until
# One is found

# Random selector to scroll along main page, this is called based upon what time of day it is. Based upon, what how many streamers are active
def rand_gen():
    num_scroll = random.randint(6,13)
    for x in range(num_scroll):
        choose_scroll = random.choice([scroll_one_down, scroll_two_down])
        choose_scroll()

# Screenshots and gets giveaway winner at location on screen, then converts that name to a string, and checks if it's any of my accounts
def test_givvy_win():
    global qq
    global tt
    global ttt
    global tttt
    global ttttt
    global tttttt
    ttt = 0
    tttt = 0
    ttttt = 0
    tttttt = 0
    tt = 0
    qq = 0
    start_time100 = time.time()
    while True:
        p61 = pa.pixel(50, 1148)
        p62 = pa.pixel(50, 1311)
        p63 = pa.pixel(560, 1311)
        p64 = pa.pixel(560, 1148)
        end_time100 = time.time() - start_time100
        if all(color == (255, 255, 255) for color in [p61, p62, p63, p64]) or end_time100 > 301:
            start_time = time.time()
            end_time = start_time + 5  # 5 seconds
            while time.time() < end_time:
                p65 = pa.pixel(300, 1171) #Goat Pixel
                white = (255,255,255)
                if p65 != white:
                    start1_time = time.time()
                    end1_time = start1_time + 5  # 5 seconds
                    while time.time() < end1_time:
                        while True:
                            screenshot = pa.screenshot(region=(180, 1229, 225, 70))
                            grayscale_image = screenshot.convert('L')
                            winner_text = pt.image_to_string(grayscale_image)
                            screenshot.save('winner_name.png')
                            time.sleep(.5)
                            if len(winner_text) > 1:
                                break  # Exit the loop if the length is greater than 1
                            crash_prev()
                        if 'big_fudge98' in winner_text:
                            print('I win')
                            tt = 7
                            return tt
                        elif 'kingloony1' in winner_text:
                            print('Follower 1 win')
                            ttt = 8
                            return ttt
                        elif 'pokefandom23' in winner_text:
                            print('Follower 2 win')
                            tttt = 9
                            return tttt
                        elif 'bigbenpoke' in winner_text:
                            print('Follower 3 win')
                            ttttt = 10
                            return ttttt
                        elif 'zardfan3' in winner_text:
                            print('Follower 4 win')
                            tttttt = 10
                            return tttttt
                        else:
                            print("I lose")
                            while True:
                                p65 = pa.pixel(50, 1148)
                                p66 = pa.pixel(50, 1311)
                                p67 = pa.pixel(560, 1311)
                                p68 = pa.pixel(560, 1148)
                                time.sleep(.5)
                                if all(color != (255, 255, 255) for color in [p65, p66, p67, p68]):
                                    time.sleep(2)
                                    qq = 6
                                    pa.moveTo(269, 1038, .3)
                                    pa.click()
                                    pa.moveTo(571, 139)
                                    pa.click()
                                    return qq
                                #End
                    time.sleep(.5)
                time.sleep(.5)
        time.sleep(2.7)

# Runs the code in a loop, directing all traffic
# Variable names were just random 
def find_givvy_loop():
    for i in range(20000):
        result = 0
        result1 = 0
        global h
        global qq
        global tt
        global ttt
        global tttt
        global ttttt
        global tttttt
        global tht1
        global tht2
        global tht3
        global tht4
        global tht5
        global tht6
        global fix1
        global fix2
        global fix3
        global fix4
        fix1 = 0
        fix2 = 0
        fix3 = 0
        fix4 = 0
        tht1 = 0
        tht2 = 0
        tht3 = 0
        tht4 = 0
        tht5 = 0
        tht6 = 0
        ttt = 0
        tttt = 0
        ttttt = 0
        tttttt = 0
        tt = 0
        qq = 0
        h = 0
        screenshot = pa.screenshot(region=(48, 960, 200, 80))  # Update Range
        grayscale_image = screenshot.convert('L')
        crash_text = pt.image_to_string(grayscale_image)
        p222 = pa.pixel(143, 892)
        p223 = pa.pixel(295, 1263)
        if 'Whatnot' in crash_text and all(color == (255, 243, 81) for color in [p222]) and all(color == (2, 6, 35) for color in [p223]):
            reopen()
        scroll_one_down()
        result = click_stream_left()
        if result == 2:
            reopen()
            #Could potentially loop if reopen leads to show
        elif result == 3:
            #Go from read_givvy
            if h == 4:
                click_stream_right()
            if k == 5:
                run_followers_randomly()
                time.sleep(.5)
                check_followers_joined()
                test_givvy_win()
                if qq == 6:
                    fix_leaving()
                    if fix1 != 15:
                        fb1.leaving()
                    if fix2 != 15:
                        fb2.leaving()
                    if fix3 != 15:
                        fb3.leaving()
                    if fix4 != 15:
                        fb4.leaving()
                    leave_fail()
                    reopen()
                if tt == 7:
                    f0w()
                    pa.moveTo(312, 1581, 1.5)
                    pa.click()
                    at.run_audio()
                    fix_leaving()
                    if fix1 != 15:
                        fb1.leaving()
                    if fix2 != 15:
                        fb2.leaving()
                    if fix3 != 15:
                        fb3.leaving()
                    if fix4 != 15:
                        fb4.leaving()
                    leave_fail()
                    pa.moveTo(269, 1038, 1)
                    pa.click()
                    pa.moveTo(571, 138, 1)
                    pa.click()
                    time.sleep(2.5)
                    reopen()
                if ttt == 8:
                    f1w()
                    pa.moveTo(984, 1581, 1.5)
                    pa.click()
                    at1.run_audio()
                    fix_leaving()
                    if fix1 != 15:
                        fb1.leaving()
                    if fix2 != 15:
                        fb2.leaving()
                    if fix3 != 15:
                        fb3.leaving()
                    if fix4 != 15:
                        fb4.leaving()
                    leave_fail()
                    pa.moveTo(269, 1038, 1)
                    pa.click()
                    pa.moveTo(571, 138, 1)
                    pa.click()
                    time.sleep(2.5)
                    reopen()
                if tttt == 9:
                    f2w()
                    pa.moveTo(1594, 1581, 1.5)
                    pa.click()
                    at2.run_audio()
                    fix_leaving()
                    if fix1 != 15:
                        fb1.leaving()
                    if fix2 != 15:
                        fb2.leaving()
                    if fix3 != 15:
                        fb3.leaving()
                    if fix4 != 15:
                        fb4.leaving()
                    leave_fail()
                    pa.moveTo(269, 1038, 1)
                    pa.click()
                    pa.moveTo(571, 138, 1)
                    pa.click()
                    time.sleep(2.5)
                    reopen()
                if ttttt == 10:
                    f3w()
                    pa.moveTo(2204, 1581, 1.5)
                    pa.click()
                    at3.run_audio()
                    fix_leaving()
                    if fix1 != 15:
                        fb1.leaving()
                    if fix2 != 15:
                        fb2.leaving()
                    if fix3 != 15:
                        fb3.leaving()
                    if fix4 != 15:
                        fb4.leaving()
                    leave_fail()
                    pa.moveTo(269, 1038, 1)
                    pa.click()
                    pa.moveTo(571, 138, 1)
                    pa.click()
                    time.sleep(2.5)
                    reopen()
                if tttttt == 11:
                    f4w()
                    pa.moveTo(2814, 1581, 1.5)
                    pa.click()
                    at4.run_audio()
                    fix_leaving()
                    if fix1 != 15:
                        fb1.leaving()
                    if fix2 != 15:
                        fb2.leaving()
                    if fix3 != 15:
                        fb3.leaving()
                    if fix4 != 15:
                        fb4.leaving()
                    leave_fail()
                    pa.moveTo(269, 1038, 1)
                    pa.click()
                    pa.moveTo(571, 138, 1)
                    pa.click()
                    time.sleep(2.5)
                    reopen()
        else:
            fix1 = 0
            fix2 = 0
            fix3 = 0
            fix4 = 0
            result1 = click_stream_right()
            if result1 == 2:
                reopen()
            if result1 == 3:
                # Go from read_givvy
                if h == 4:
                    scroll_one_down()
                if k == 5:
                    run_followers_randomly()
                    time.sleep(.5)
                    check_followers_joined()
                    test_givvy_win()
                    if qq == 6:
                        fix_leaving()
                        if fix1 != 15:
                            fb1.leaving()
                        if fix2 != 15:
                            fb2.leaving()
                        if fix3 != 15:
                            fb3.leaving()
                        if fix4 != 15:
                            fb4.leaving()
                        leave_fail()
                        reopen()
                    if tt == 7:
                        f0w()
                        pa.moveTo(312, 1581, 1.5)
                        pa.click()
                        at.run_audio()
                        fix_leaving()
                        if fix1 != 15:
                            fb1.leaving()
                        if fix2 != 15:
                            fb2.leaving()
                        if fix3 != 15:
                            fb3.leaving()
                        if fix4 != 15:
                            fb4.leaving()
                        leave_fail()
                        pa.moveTo(269, 1038, 1)
                        pa.click()
                        pa.moveTo(571, 138, 1)
                        pa.click()
                        time.sleep(2.5)
                        reopen()
                    if ttt == 8:
                        f1w()
                        pa.moveTo(984, 1581, 1.5)
                        pa.click()
                        at1.run_audio()
                        fix_leaving()
                        if fix1 != 15:
                            fb1.leaving()
                        if fix2 != 15:
                            fb2.leaving()
                        if fix3 != 15:
                            fb3.leaving()
                        if fix4 != 15:
                            fb4.leaving()
                        leave_fail()
                        pa.moveTo(269, 1038, 1)
                        pa.click()
                        pa.moveTo(571, 138, 1)
                        pa.click()
                        time.sleep(2.5)
                        reopen()
                    if tttt == 9:
                        f2w()
                        pa.moveTo(1594, 1581, 1.5)
                        pa.click()
                        at2.run_audio()
                        fix_leaving()
                        if fix1 != 15:
                            fb1.leaving()
                        if fix2 != 15:
                            fb2.leaving()
                        if fix3 != 15:
                            fb3.leaving()
                        if fix4 != 15:
                            fb4.leaving()
                        leave_fail()
                        pa.moveTo(269, 1038, 1)
                        pa.click()
                        pa.moveTo(571, 138, 1)
                        pa.click()
                        time.sleep(2.5)
                        reopen()
                    if ttttt == 10:
                        f3w()
                        pa.moveTo(2204, 1581, 1.5)
                        pa.click()
                        at3.run_audio()
                        fix_leaving()
                        if fix1 != 15:
                            fb1.leaving()
                        if fix2 != 15:
                            fb2.leaving()
                        if fix3 != 15:
                            fb3.leaving()
                        if fix4 != 15:
                            fb4.leaving()
                        leave_fail()
                        pa.moveTo(269, 1038, 1)
                        pa.click()
                        pa.moveTo(571, 138, 1)
                        pa.click()
                        time.sleep(2.5)
                        reopen()
                    if tttttt == 11:
                        f4w()
                        pa.moveTo(2814, 1581, 1.5)
                        pa.click()
                        at4.run_audio()
                        fix_leaving()
                        if fix1 != 15:
                            fb1.leaving()
                        if fix2 != 15:
                            fb2.leaving()
                        if fix3 != 15:
                            fb3.leaving()
                        if fix4 != 15:
                            fb4.leaving()
                        leave_fail()
                        pa.moveTo(269, 1038, 1)
                        pa.click()
                        pa.moveTo(571, 138, 1)
                        pa.click()
                        time.sleep(2.5)
                        reopen()

# Common timing issue check to determine if the program is at the right stage in the script, based on all bots leaving the stream
def leave_fail():
    p401 = pa.pixel(1010, 141)
    p402 = pa.pixel(1121, 139)
    p403 = pa.pixel(1613, 142)
    p404 = pa.pixel(1733, 137)
    p405 = pa.pixel(2225, 139)
    p406 = pa.pixel(2344, 141)
    p407 = pa.pixel(2835, 139)
    p408 = pa.pixel(2954, 141)
    if all(color != (255, 255, 255) for color in [p401, p402]):
        fb1.leaving()
    if all(color != (255, 255, 255) for color in [p403, p404]):
        fb2.leaving()
    if all(color != (255, 255, 255) for color in [p405, p406]):
        fb3.leaving()
    if all(color != (255, 255, 255) for color in [p407, p408]):
        fb4.leaving()

# Common popup check to determine if the program is at the right stage in the script
def fix_leaving():
    global fix1
    global fix2
    global fix3
    global fix4
    fix1 = 0
    fix2 = 0
    fix3 = 0
    fix4 = 0
    p201 = pa.pixel(1010, 141)
    p202 = pa.pixel(1121, 139)
    p203 = pa.pixel(1613, 142)
    p204 = pa.pixel(1733, 137)
    p205 = pa.pixel(2225, 139)
    p206 = pa.pixel(2344, 141)
    p207 = pa.pixel(2835, 139)
    p208 = pa.pixel(2954, 141)
    if all(color == (255, 255, 255) for color in [p201, p202]):
        pa.moveTo(975, 144, 1)
        pa.click()
        time.sleep(.5)
        pa.moveTo(1155, 145, 1)
        pa.click()
        fix1 = 15
    if all(color == (255, 255, 255) for color in [p203, p204]):
        pa.moveTo(1586, 144, 1)
        pa.click()
        time.sleep(.5)
        pa.moveTo(1766, 145, 1)
        pa.click()
        fix2 = 15
    if all(color == (255, 255, 255) for color in [p205, p206]):
        pa.moveTo(2188, 144, 1)
        pa.click()
        time.sleep(.5)
        pa.moveTo(2375, 145, 1)
        pa.click()
        fix3 = 15
    if all(color == (255, 255, 255) for color in [p207, p208]):
        pa.moveTo(2798, 144, 1)
        pa.click()
        time.sleep(.5)
        pa.moveTo(2985, 145, 1)
        pa.click()
        fix4 = 15

# Common popup check to determine if the program is at the right stage in the script
def ver_buy():
    time.sleep(1)
    screenshot = pa.screenshot(region=(100, 1800, 550, 450)) #Update Range
    grayscale_image = screenshot.convert('L')
    future_text = pt.image_to_string(grayscale_image)
    screenshot.save('function2_screenshot.png')
    if 'Become' in future_text or 'verified' in future_text or 'buyer' in future_text:
        time.sleep(1)
        pa.moveTo(317, 1066, .5)
        pa.click()
        time.sleep(.5)
        pa.moveTo(572, 139, .7)
        pa.click()
        return 4

# Determines if a streamer is selling an item, not doing a giveaway
def list_an_item():
    screenshot20 = pa.screenshot(region=(69, 2216, 110, 30))
    grayscale_image20 = screenshot20.convert('L')
    list_text = pt.image_to_string(grayscale_image20)
    if 'List an item' in list_text:
        pa.moveTo(306, 1117)
        pa.click()
        scroll_third_down()
        return 1

# Determines if a streamer isn't live, but has a schedule stream. Prevents the scraper from waiting for a giveaway that isn't occuring
def show_starts():
    global fgh
    fgh = 0
    screenshot10o = pa.screenshot(region=(140, 238, 360, 80))
    grayscale_image00 = screenshot10o.convert('L')
    show_text00 = pt.image_to_string(grayscale_image00)
    if 'Show starts in' in show_text00 or 'Show starting in' in show_text00 or 'Show starts soon' in show_text00:
        pa.moveTo(300, 1000, .25)
        pa.click()
        pa.moveTo(570, 138, 1)
        pa.click()
        time.sleep(.5)
        fgh = 1
        return fgh

# Common misclick check to determine if the program is at the right stage in the script
def misclick():
    xlm = 0
    xlm = main_page()
    if xlm == 1:
        return
    elif xlm == 2:
        pa.moveTo(28, 133, 1)
        pa.click()
        time.sleep(1)
        return
    p81 = pa.pixel(517, 294)
    p82 = pa.pixel(584, 285)
    if all(color == (255, 255, 255) for color in [p81, p82]):
        pa.moveTo(27, 131, 1)
        pa.click()
        time.sleep(1)

# Determines if the program is currently on the main page of the website
def main_page():
    screenshot = pa.screenshot(region=(271, 197, 144, 28))
    grayscale_image = screenshot.convert('L')
    main_text = pt.image_to_string(grayscale_image)
    screenshot1 = pa.screenshot(region=(61, 117, 154, 5130))
    grayscale_image1 = screenshot1.convert('L')
    main_text1 = pt.image_to_string(grayscale_image1)
    if 'Pokemon' in main_text or 'Cards' in main_text:
        return 1
    elif 'Pokemon' in main_text1 or 'Cards' in main_text1:
        return 2

# Screenshot and get the text of the winner of the giveaway
def givvy_name():
    global person_text
    screenshot15 = pa.screenshot(region=(57, 119, 250, 24))
    grayscale_image15 = screenshot15.convert('L')
    person_text1 = pt.image_to_string(grayscale_image15)
    person_text2 = person_text1.replace("@", "")
    person_text = person_text2.replace(" ", "")
    with open("streamer.txt", "w") as file:
        file.write(person_text)
    return person_text

# Runs the reopen script if the app crashed
def crash_prev():
        screenshot15 = pa.screenshot(region=(56, 963, 177, 66))
        grayscale_image15 = screenshot15.convert('L')
        crash_text = pt.image_to_string(grayscale_image15)
        screenshot16 = pa.screenshot(region=(60, 575, 170, 60))
        grayscale_image16 = screenshot16.convert('L')
        crash_text2 = pt.image_to_string(grayscale_image16)
        if 'Whatnot' in crash_text and 'App' in crash_text2 and flagg:
            reopen()
            return 5

# Common misclick check to determine if the program is at the right stage in the script
def misclick2():
    screenshot16 = pa.screenshot(region=(532, 132, 70, 30))
    grayscale_image16 = screenshot16.convert('L')
    misclick2 = pt.image_to_string(grayscale_image16)
    if 'Cancel' in misclick2 or 'cancel' in misclick2:
        pa.moveTo(561, 151)
        pa.click()

# Pixel check (white) for follower bot 1 at various locations on screen to make sure the program is at the correct stage in the script, otherwise a reset is needed
def f1w():
    while True:
        p65 = pa.pixel(743, 1148)
        p66 = pa.pixel(743, 1311)
        p67 = pa.pixel(1253, 1311)
        p68 = pa.pixel(1253, 1148)
        if all(color != (255, 255, 255) for color in [p65, p66, p67, p68]):
            return
        time.sleep(.15)

# Pixel check (white) for follower bot 2 at various locations on screen to make sure the program is at the correct stage in the script, otherwise a reset is needed
def f2w():
    while True:
        p65 = pa.pixel(1353, 1148)
        p66 = pa.pixel(1353, 1311)
        p67 = pa.pixel(1863, 1311)
        p68 = pa.pixel(1863, 1148)
        if all(color != (255, 255, 255) for color in [p65, p66, p67, p68]):
            return
        time.sleep(.15)


# Pixel check (white) for follower bot 3 at various locations on screen to make sure the program is at the correct stage in the script, otherwise a reset is needed
def f3w():
    while True:
        p65 = pa.pixel(1963, 1148)
        p66 = pa.pixel(1963, 1311)
        p67 = pa.pixel(2473, 1311)
        p68 = pa.pixel(2473, 1148)
        if all(color != (255, 255, 255) for color in [p65, p66, p67, p68]):
            return
        time.sleep(.15)


# Pixel check (white) for follower bot 4 at various locations on screen to make sure the program is at the correct stage in the script, otherwise a reset is needed
def f4w():
    while True:
        p65 = pa.pixel(2573, 1148)
        p66 = pa.pixel(2573, 1311)
        p67 = pa.pixel(3083, 1311)
        p68 = pa.pixel(3083, 1148)
        if all(color != (255, 255, 255) for color in [p65, p66, p67, p68]):
            return
        time.sleep(.15)


# Pixel check (white) for main bot at various locations on screen to make sure the program is at the correct stage in the script, otherwise a reset is needed
def f0w():
    while True:
        p65 = pa.pixel(50, 1148)
        p66 = pa.pixel(50, 1311)
        p67 = pa.pixel(560, 1311)
        p68 = pa.pixel(560, 1148)
        if all(color != (255, 255, 255) for color in [p65, p66, p67, p68]):
            return
        time.sleep(.15)

# Check the current time to determine which rand_gen function to run based on how approximately how many streamers are currently live
def check_time():
    start_time_a = datetime.time(2, 30)  # 2:00 AM
    end_time_a = datetime.time(15, 30)  # 3:30 PM
    start_time_b_friday = datetime.time(2, 30)  # 2:30 AM
    end_time_b_friday = datetime.time(12, 0)  # 12:00 PM
    current_day = datetime.datetime.now().date().weekday()
    current_time = datetime.datetime.now().time()
    if ((start_time_a <= current_time <= end_time_a and current_day != 4 and current_day != 5 and current_day != 6) or (current_day == 4 and start_time_b_friday <= current_time <= end_time_b_friday) or (current_day == 5 and start_time_b_friday <= current_time <= end_time_b_friday) or (current_day == 6 and start_time_b_friday <= current_time <= end_time_b_friday)):
        rand_gen1()
    else:
        rand_gen()

# Scroll down a random amount using either of the two defined scroll functions
def rand_gen1():
    num_scroll = random.randint(4,8)
    for x in range(num_scroll):
        choose_scroll = random.choice([scroll_one_down, scroll_two_down])
        choose_scroll()

# Followers join in random order to avoid repetition
def run_followers_randomly():
    functions = [fb1.joining_givvy1, fb2.joining_givvy1, fb3.joining_givvy1, fb4.joining_givvy1]
    random.shuffle(functions)  # Shuffle the list of functions
    for function in functions:
        result = function()
        if result == 15:
            break

# Run the check if follower bots joined
def check_followers_joined():
    fb1.check_join1()
    fb2.check_join2()
    fb3.check_join3()
    fb4.check_join4()

# Check if crash occured and reopen app
def reopen_check():
    screenshot = pa.screenshot(region=(48, 960, 200, 80))  # Update Range
    grayscale_image = screenshot.convert('L')
    crash_text = pt.image_to_string(grayscale_image)
    p222 = pa.pixel(143, 892)
    p223 = pa.pixel(295, 1263)
    if 'Whatnot' in crash_text and all(color == (255, 243, 81) for color in [p222]) and all(color == (2, 6, 35) for color in [p223]):
        return 100
