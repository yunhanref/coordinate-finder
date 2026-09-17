import mss
import os
import time
def screenshot():
    with mss.mss() as sct:
        pygame_window = {
            "top":190,
            "left":320,
            "width": 1280,
            "height": 688 
            }
        
        sct_img = sct.grab(pygame_window)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output="imgs/pygame_check.png")
        time.sleep(2)
        '''
        print("type c to capture, q to quit")
        while True:
            userin = str(input()).lower()
            if userin == "c":
                sct_img = sct.grab(pygame_window)
                mss.tools.to_png(sct_img.rgb, sct_img.size, output="imgs/pygame_check.png")
                keep = str(input("want to keep? y/n:   ")).lower()
                if keep == "y":
                    print("keeping files")
                    break
                elif keep == "n":
                    for deletedimg in os.listdir("imgs"):
                        os.remove(os.path.join("imgs", deletedimg))
                    break
            elif userin == "q":
                print("quitting...")
                break
            else:
                print("unknown")
                break
        '''

'''
    #! THIS IS WHERE THE PLAYER ANIMATION IN DIALOGUE ANIMATIONS (MOST OF THE TIME) 
    #! MAIN FRAME: [(0,0),(0,1300)] + height range: [(0,0),(698,0)]
    undivided_frame = {
        "top":0,
        "left":0,
        "width": 1300,
        "height": 698
    }
    #sct_img = sct.grab(undivided_frame)
    #mss.tools.to_png(sct_img.rgb, sct_img.size, output="main_frame.png")
    #! IDEA: DIVIDING MAIN FRAME TO FOUR. REASONS:
    #!  To save memory by not looking at the bigger part of the screen.
    #!  I want to practice my own way. 
    # Dividing the mainframe
    frame1 = {
            "top":0,
            "left":0,
            "width": 600,
            "height": 301
        }
    frame2 = {
            "top":0,
            "left":600,
            "width": 700,
            "height": 301
        }
    frame3 = {
            "top":301,
            "left":0,
            "width": 600,
            "height": 397
        }
    frame4 = {
            "top":301,
            "left":600,
            "width": 700,
            "height": 397
        }
    print("type c to capture, q to quit")
    while True:
        userin = str(input()).lower()
        if userin == "c":
            print("taking pictures.")
            sct_img = sct.grab(frame1)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output="imgs/frame1.png")
                    
            sct_img = sct.grab(frame2)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output="imgs/frame2.png")
                    
            sct_img = sct.grab(frame3)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output="imgs/frame3.png")
                    
            sct_img = sct.grab(frame4)
            mss.tools.to_png(sct_img.rgb, sct_img.size, output="imgs/frame4.png")
            keep = str(input("want to keep? y/n:   ")).lower()
            if keep == "y":
                print("keeping files")
                break
            elif keep == "n":
                for deletedimg in os.listdir("imgs"):
                    os.remove(os.path.join("imgs", deletedimg))
                break
        
        elif userin == "q":
            print("breaking")
            break
        
        else:
            print("unknown")
            break
    #! FIX: CHARACTER HEAD MAY BE IN BOTH FRAMES THAT WILL MAKE IT HARD. TAKE ONE PICTURE OF THE UNDIVIDED FRAME AND WOK ON IT INSTEAD.        
    '''