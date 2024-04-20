Two string values S1 and S2 are passed as input. 
The program must print the count of common characters in the strings S1 and S2. 
Assume the alphabets in S1 and S2 will be in lower case.
Input Format:
First line will contain the value of string S1 Second line will contain 
the value of string S2 
Output Format: 
First line will contain the count of common alphabets. 
Boundary Conditions: Length of S1 and S2 will be from 3 to 100.
Sample Input/Output: 
Example 1: 
Input: china india 
Output: 3 
Explanation: The common characters are i,n,a 
Example 2: 
Input: energy every 
Output: 3 
Explanation: The common characters are e,r,y

s1 = input()
s2 = input()
count = sum(1 for c in set(s1) if c in s2)
print(count)
