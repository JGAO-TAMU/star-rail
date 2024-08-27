import pyautogui
import pydirectinput
import time
from PIL import Image
from PIL import ImageChops
from pywinauto import application
from pywinauto import timings

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def click_image(image_path, confidence=0.8, timeout=30, xoff=0, yoff=0, find_domain=False, searchtime=0.2, grayscale=False, movecamera=False, in_overworld=False):
    print(f"")
    print(f"click image called: image_path={image_path}, confidence={confidence}, timeout={timeout}, xoff={xoff}, yoff={yoff}, find_domain={find_domain}, searchtime={searchtime}, grayscale={grayscale}, movecamera={movecamera}")

    start_time = time.time()
    while True:

        try:
            location = pyautogui.locateCenterOnScreen(image_path, minSearchTime=searchtime, confidence=confidence, grayscale=grayscale)
            if location:
                #print("location")
                x, y = location
                #found_confidence = location.confidence   -----------   *problem line*
                x += xoff
                y += yoff
                print(f"found image={image_path} and clicking offset x={xoff} y={yoff}")
                if(in_overworld):
                    pyautogui.keyDown('altleft')
                    time.sleep(0.5)
                pyautogui.click(x, y)
                if(in_overworld):
                    pyautogui.keyUp('altleft')
                return True
            
        except Exception as e:
            #print(f"Exception occurred")
            
            if(find_domain):
                
                try:
                    temp = pyautogui.locateCenterOnScreen('railing_time\\railing_images\\enter.png', grayscale=True, confidence=0.8)
                
                except Exception as e:
                    print("enter not found")
                    try:
                        temp = pyautogui.locateCenterOnScreen('railing_time\\railing_images\\teleport.png', grayscale=True, confidence=0.8)
                    except Exception as e:
                        temp=None
                        print("teleport not found")    

                if temp:
                    pyautogui.moveTo(temp)
                    pyautogui.scroll(-1)
                    pyautogui.scroll(-1)
                    pyautogui.scroll(-1)
                    pyautogui.scroll(-1)
                    pyautogui.scroll(-1)
                    print("scrolled down")
                
                
            if(movecamera):
                pyautogui.FAILSAFE = False #Danger
                pyautogui.moveRel(yOffset=100, duration=0.5)
                pyautogui.FAILSAFE = True
                print(f"moved camera y={100}") #change with yOffset

            continue        

        if time.time() - start_time > timeout:
            print("click image timeout")
            return False
        
        time.sleep(0.5)  

def wait_for_screen(image_path, timeout=240, confidence=0.8, period=5):
    start_time = time.time()
    while True:
        try:
            print(f"waiting for image {image_path}...")
            if pyautogui.locateCenterOnScreen(image_path, confidence=confidence):
                return True
        except Exception as e:
            #print(f"Exception occurred: {e}")
            elapsed_time = time.time() - start_time
            print(f"Elapsed time: {elapsed_time}")
        if elapsed_time > timeout:
            print("screen timeout")
            return False
        time.sleep(period)
        continue
        
        
        

def restart(): # call when the restart button appears
    
    print("Restarting...")
    click_image('railing_time\\railing_images\one_more_time.png')
    time.sleep(1)   # Wait for restart to complete


app_path = "D:\HSR\Star Rail\Games\StarRail.exe" #path for my installation.  

def star_rail_dailies(path, mode, material):
    print(path, mode, material)
    
    ############ start game ############
    application.Application().start(path)
    #main_window = app.window(title=window_title)
    count = 1

    click_image('railing_time\\railing_images\start_game_small.png',confidence=.9)
    click_image('railing_time\\railing_images\\click_to_start.png',confidence=.9)

    ############ overworld #############
    #movecamera will happen while game is loading
    click_image('railing_time\\railing_images\\daily_icon_unclaimed.png',confidence=.8, grayscale=True, movecamera=False, in_overworld=True) #set movecamera true when it works

    time.sleep(1.5)
    click_image('railing_time\\railing_images\\arrow_icon.png',confidence=.8)

    ############# domain select ############
    click_image(f'railing_time\\railing_images\\domain_select\\{mode}.png',confidence=.7)
    click_image(f'railing_time\\railing_images\\domain_select\\{material}.png',confidence=.7, xoff=450, find_domain=True)

    if(mode == 'crimson'):
        click_image('railing_time\\railing_images\\add_runs.png',confidence=.97)
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()

    click_image('railing_time\\railing_images\\challenge.png',confidence=.9, searchtime=10)

    ################ team select ##############
    ### skip for now ###
    """    
    click_image('railing_time\\railing_images\\support_button.png',confidence=.9)
    click_image('railing_time\\railing_images\\souqence_jingliu.png',confidence=.9)
    click_image('railing_time\\railing_images\\add_button.png',confidence=.9)
    
    """
    click_image('railing_time\\railing_images\\start_challenge.png',confidence=.9)

    ################ in combat ###############
    time.sleep(1)
    click_image('railing_time\\railing_images\\auto_button.png',confidence=.5, grayscale=True)


    while True:
        
        if wait_for_screen('railing_time\\railing_images\\one_more_time.png'):
            print("one more time found...")
            restart()
            if wait_for_screen('railing_time\\railing_images\\replenish.png', timeout=3, confidence=0.6):
                print("add resin found...")
                break
            #print("going again")
            
            print(f"Cycle {count} completed.\n")
            count += 1

        else:
            print("Screen not found, program stopped")

    #done spending resin

    ############## claim rewards ##############
    click_image('railing_time\\railing_images\cancel.png')
    print("clicked cancel...")
    time.sleep(1)
    click_image('railing_time\\railing_images\exit.png')
    print("clicked exit...")
    #wait_for_screen('railing_time\\railing_images\\bud.png',confidence=.5)
    time.sleep(3) #wait for game to load. replace with something better later
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    time.sleep(1)
    pyautogui.keyDown('altleft')
    click_image('railing_time\\railing_images\daily_icon_unclaimed.png', confidence=0.8, grayscale=True)
    pyautogui.keyUp('altleft')
    #click_image('railing_time\\railing_images\daily_icon.png')
    time.sleep(0.2)
    click_image('railing_time\\railing_images\daily_claim.png')
    time.sleep(0.2)
    click_image('railing_time\\railing_images\daily_claim.png')
    time.sleep(0.2)
    click_image('railing_time\\railing_images\daily_claim.png')
    time.sleep(0.2)
    click_image('railing_time\\railing_images\daily_claim.png')
    time.sleep(0.2)
    click_image('railing_time\\railing_images\daily_claim.png')


    print("all done :)")
    # all done :)
    return