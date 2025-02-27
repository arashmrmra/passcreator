import random
keyboard = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%&-+/*!@#$%&-+/*!@#$%&-+/*!@#$%&-+/*!@#$%&-+/*!@#$%&-+/*!@#$%&-+/*!@#$%&-+/*!@#$%&-+/*012345678901234567890123456789"
def start():
    for j in range(10):
        for i in range(21):
            point = random.randint(0,196) 
            print(keyboard[point],end="")
            if i == 20:
                print()
start()