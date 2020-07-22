import pyautogui 
import time

def join(id,pswd):
	meet_id = id
	password = pswd
	pyautogui.press('esc',interval=0.1)
	time.sleep(0.2)
	pyautogui.press('win',interval=0.1)
	pyautogui.write('zoom')
	pyautogui.press('enter',interval=0.5)
	time.sleep(10)
	x,y = pyautogui.locateCenterOnScreen('joinButton.png',confidence=0.7)
	pyautogui.click(x,y)
	pyautogui.press('enter',interval=1)
	pyautogui.write(meet_id)
	pyautogui.press('enter',interval=1)
	time.sleep(3)
	pyautogui.write(password)
	pyautogui.press('enter',interval = 1)
	time.sleep(5)
	try:
		x,y = pyautogui.locateCenterOnScreen('mute.png')
		pyautogui.click(x,y)
	except:
		pass