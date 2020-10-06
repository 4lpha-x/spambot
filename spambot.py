import pyautogui, time

print("Create a wordlist file in the same directory in which the spammer.py is present.\n")

sleeptime = int(input("Please enter the sleeptime of the bot (in seconds): "))
time.sleep(sleeptime)

spamwords = input("Please enter the name of the Wordfile: ")
f = open(spamwords, 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press('enter')
