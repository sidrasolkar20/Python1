#Python Exp04(1)
# Aim:Python program to count number of lines, words and characters in a file.
# Name: Sidra Solkar
# UIN:231P087   Roll No.:43
fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
 for line in f:
  num_lines += 1
print("Number of lines:")
print(num_lines)
print("\nName: Sidra Solkar \nUIN:231P087 \nRoll no:43")
