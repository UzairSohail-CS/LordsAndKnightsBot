
import pyautogui
import time

# Account details
accounts = [
  ['username1', 'password1'],
  ['username2', 'password2']
]

def login(username, password):
  pyautogui.click(100, 100) # Click login button
  pyautogui.typewrite(username)
  pyautogui.typewrite(password)
  pyautogui.press('en'
                  'ter')

def build_habitat():
  pyautogui.click(200, 200) # Click build button
  pyautogui.click(300, 300) # Click habitat type
  pyautogui.click(400, 400) # Click build location
  pyautogui.press('enter')

def defend():
  pyautogui.click(500, 500) # Click defend button
  pyautogui.click(600, 600) # Click troops
  pyautogui.press('enter')

def attack():
  pyautogui.click(700, 700) # Click attack button
  pyautogui.click(800, 800) # Click target player
  pyautogui.press('enter')

def main():
  for account in accounts:
    username = account[0]
    password = account[1]

    login(username, password)

    while True:
      build_habitat()
      defend()
      attack()
      time.sleep(600) # Wait 10 minutes

if __name__ == '__main__':
  main()
