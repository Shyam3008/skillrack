A string S is passed as the input. 
S has at least one repeating character. 
The program must print the first repeating character C. 
Input Format: The first line contains S. 
Output Format: The first line contains C. 
Boundary Conditions: Length of S will be from 3 to 100. 
Example Input/Output 1: Input: abcdexyzbwqpoolj Output: b

S = input()
for char in S:
    if S.count(char) > 1:
        print(char)
        break
