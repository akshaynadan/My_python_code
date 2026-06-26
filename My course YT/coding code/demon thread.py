import threading
import time  


def timer():
    count =0
    while True:
        time.sleep(1)
        count+=1
        print("Time passed :",count,"seconds")
        
        
x = threading.Thread(target=timer,daemon = True)
x.start() 


user_input = input("Do you wish to Exit:? \n")







