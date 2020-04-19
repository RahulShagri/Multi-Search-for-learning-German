import pyautogui
import pyperclip

def locate_wait(img):
    loc = None
    while loc is None:
        loc = pyautogui.locateOnScreen(img, confidence = 0.8)
    return loc

while True:

    user_word = input("Enter the word: ")

    if user_word == '':
        break

    user_word = user_word.lower()
    pyperclip.copy(user_word)
    pyautogui.moveTo(pyautogui.center(locate_wait("chrome.png")), duration = 0.2)
    pyautogui.click()

    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite("https://www.dict.cc/?s=", interval = 0.005)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite("https://www.google.de/search?q=", interval = 0.005)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite("&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjs8Mf514_oAhXCWisKHU-FDAQQ_AUoA3oECAsQBQ&biw=1366&bih=657", interval = 0.005)
    pyautogui.press('enter')

    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite("https://en.wiktionary.org/w/index.php?title=", interval = 0.005)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite("&rdfrom", interval = 0.005)
    pyautogui.press('enter')

    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite("https://de.thefreedictionary.com/", interval = 0.005)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite("https://www.linguee.com/english-german/search?source=auto&query=", interval = 0.005)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite("https://de.forvo.com/word/", interval = 0.005)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.typewrite("/#de", interval = 0.005)
    pyautogui.press('enter')
