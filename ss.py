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
        os.makedirs("imgs", exist_ok=True)
        
        sct_img = sct.grab(pygame_window)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output="imgs/pygame_check.png")
        
        time.sleep(2)
