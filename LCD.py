import lcddriver
from time import *
lcd = lcddriver.lcd()
lcd.lcd_clear()
lcd.lcd_display_string(" Bonsoir", 1)
lcd.lcd_display_string(" Virginie", 2)
