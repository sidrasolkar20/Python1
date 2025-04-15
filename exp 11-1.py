# Exp11(01) 
# Aim:Write a program for cutting tickets and show chair thread.
# Name: Sidra Solkar
# UIN: 231P087   Roll No: 43
from threading import * 
from time import * 

class Theatre: 
    # Constructor 
    def __init__(self, str, lock): 
        self.str = str 
        self.lock = lock 
    
    # Method to repeat for 5 tickets 
    def movieshow(self): 
        for i in range(1, 6): 
            with self.lock:  # Acquire the lock to ensure thread-safe printing
                print(self.str, ":", i) 
            sleep(0.5) 

# Create a lock for synchronizing the threads 
lock = Lock() 

# Create two instances of the Theatre class 
obj1 = Theatre("Cut Ticket", lock) 
obj2 = Theatre("Show Chair", lock) 

# Create two threads to run movieshow() 
t1 = Thread(target=obj1.movieshow) 
t2 = Thread(target=obj2.movieshow) 

# Start the threads 
t1.start() 
t2.start() 

# Wait for both threads to finish 
t1.join() 
t2.join() 

# Print thank you message after threads complete execution
print("\nName: Sidra Solkar \nUIN: 231P087\nRoll No: 43")

