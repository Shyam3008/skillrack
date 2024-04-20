A string S is passed as input. 
S will contain multiple integer values with each integer value followed by an alphabet. 
The program must expand the alphabets based on the related integer value. 
Input Format: The first line contains S. 
Output Format: The first line contains the expanded string value. 
Boundary Conditions: Length of S is from 2 to 100.
Example Input/Output 1: 
Input: 4a5h 
Output: aaaahhhhh 
Explanation: As it is 4a and 5h, four a's are printed followed by 5 h's 
Example Input/Output 2: 
Input: 1k2b4k 
Output: kbbkkkk

S = input()
expanded_string = ''
num = ''
for char in S:
    if char.isdigit():
        num += char
    else:
        expanded_string += int(num) * char
        num = ''
print(expanded_string)
