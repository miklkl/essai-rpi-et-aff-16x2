#importe le pilote et appel du module "time"
import lcddriver
import sys
from time import *



# initlaise le lcd
lcd = lcddriver.lcd()
#initilaise le lcd
lcd.lcd_clear()

#affichage du message
lcd.lcd_display_string('coucou', 1)
lcd.lcd_display_string('virginie', 2)
