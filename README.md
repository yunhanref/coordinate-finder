<img width="1280" height="688" alt="pygame_check" src="https://github.com/user-attachments/assets/da3d93e0-a18c-4d16-af6e-871c422f8c8f" />

# How Does It Work?

**Terminal 1: `python dots.py`**
1) `dots.py` file opens a 640x360 pygame window. Inside this window three different coloured circles gets drawn in random coordinates every 2 seconds.
2) As `dots.py` runs, `screenshot()` function inside the file `ss.py` gets called and takes screenshots of the pygame window every 2 seconds and saves it inside /imgs.


**Terminal 2: `python ss_analyser.py`**

3) `ss_analyser.py` file analyses the image inside /imgs and finds coordinates of the the circle that has red color.


# **-----Installation-----**



---

**For Windows:**
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**For Mac/Linux**
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# **-----Running the Program-----**

---

**Terminal 1:**
```
 python dots.py
 ctrl + c to exit  
```

**Terminal 2 (Coordinate results will get printed to terminal 2)**

**NOTE:** Make sure you open the second terminal outside of the pygame window.
```
python ss_analyser.py
ctrl + c to exit
```
