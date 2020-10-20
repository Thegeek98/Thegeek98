import random
import pyautogui
import time

#password = str(input("Enter password only numbers : "))

#guess = " "

while 2 != 1:
  guess = str(random.randint(0, 99999999))
  pyautogui.typewrite(guess)
  #time.sleep(1)
  pyautogui.press('enter')
  pyautogui.press('enter')
  pyautogui.press('enter')
#  print("=> "+ guess)

#  if(guess == password):
#    print("The password is :"+ password)
#    break










