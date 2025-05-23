# Importing model
import time 

# Main model
def delay(text,delay=0.1):
    for char in text:
        print(char,end='',flush=True)
        time.sleep(delay)
    print()

# How to use ? : for example : delay('Hello world')
        