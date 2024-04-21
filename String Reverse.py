The program must accept a string value S and print the reverse of S.
Input Format: The first line denotes the value of S. 
Output Format: The first line contains reversed value of S. 
Boundary Conditions: Length of string S is from 2 to 100. 
Example Input/Output 1: Input: abcde Output: edcba 
Example Input/Output 2: Input: look Output: kool

S = input()
reversed_S = S[::-1]
print(reversed_S)
