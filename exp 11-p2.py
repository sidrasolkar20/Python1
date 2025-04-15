# Exp11(Postlab02) 
# Aim:Write a program for multiple thread.
# Name: Sidra Solkar
# UIN: 231P087   Roll No: 43
import threading 
import time 

# Define the first task 
def task1(): 
    print("Task 1 started.") 
    time.sleep(2)  # Simulate a task that takes 2 seconds 
    print("Task 1 completed.") 

# Define the second task 
def task2(): 
    print("Task 2 started.") 
    time.sleep(3)  # Simulate a task that takes 3 seconds 
    print("Task 2 completed.") 

def main(): 
    print("Program started.") 
    # Create two threads for the tasks 
    thread1 = threading.Thread(target=task1) 
    thread2 = threading.Thread(target=task2) 
    # Start both threads 
    thread1.start() 
    thread2.start() 
    # Wait for both threads to complete 
    thread1.join() 
    thread2.join() 
    print("Program completed.") 
    print("\nName: Sidra Solkar \nUIN: 231P087\nRoll No: 43") 

if __name__ == "__main__": 
    main()
