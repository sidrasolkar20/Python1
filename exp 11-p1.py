# Exp11(Postlb01) 
# Aim:Write a program for single thread.
# Name: Sidra Solkar
# UIN: 231P087   Roll No: 43
import time 

def task1(): 
    print("Task 1 started.") 
    time.sleep(2)  # Simulate a task that takes 2 seconds 
    print("Task 1 completed.") 

def task2(): 
    print("Task 2 started.") 
    time.sleep(3)  # Simulate a task that takes 3 seconds 
    print("Task 2 completed.") 

def main(): 
    print("Program started.") 
    task1()  # Execute task 1
    task2()  # Execute task 2
    print("Program completed.") 
    print("\nName: Sidra Solkar \nUIN: 231P087\nRoll No: 43") 

if __name__ == "__main__":  # Ensure that the program runs only when executed directly
    main()
