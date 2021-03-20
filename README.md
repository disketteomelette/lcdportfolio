# lcdportfolio
Simple python code to show your crypto portfolio updated on a LCD screen in a Raspberry

I have followed these fantastic (and colorful) instructions for wiring a LCD 2x16 screen 
in a Raspberry without using Arduino or any other "extras":
https://www.rototron.info/lcd-display-tutorial-for-raspberry-pi/

This script uses a Coinbase price API call for each cypto pair and should be properly
rate-limited for avoid a ban (i.ex. using sleep() function). 
