import time
while(True):
    time.sleep(1)
    number = input("pick a number")
    if int(number)%2 ==0 and int(number)%5 ==0:
        print("buzz")
    elif int(number)%2 ==0:
        print("fizz")
    elif int(number)%5 ==0:
        print("pop")
    


    
