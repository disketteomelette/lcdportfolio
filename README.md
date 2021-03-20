# lcdportfolio
![lcdportfolio-raspi](https://user-images.githubusercontent.com/39524746/111867607-75796100-8975-11eb-9e2f-94e17f8a3f3a.gif)

Simple python code to show your crypto portfolio updated on a LCD screen in a Raspberry


I have followed these fantastic (and colorful) instructions for wiring a LCD 2x16 screen 
in a Raspberry without using Arduino or any other "extras":
https://www.rototron.info/lcd-display-tutorial-for-raspberry-pi/

This script uses a Coinbase price API call for each cypto pair and should be properly
rate-limited for avoid a ban (i.ex. using sleep() function). 

