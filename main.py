import datetime
import time


def question():
    ans = input('how much weed per gram do you smoke daily?')
    return ans


ask = int(question())

if ask > 3:
    print("You're smoking too much")
elif ask < 2:
    print("You're being moderate")
