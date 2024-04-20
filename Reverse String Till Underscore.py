String S is passed as the input to the program. 
S may or may not have a single underscore embedded in it. 
The program must reverse the String S till the first underscore and print it as the output. 
Input Format: The first line contains S. 
Output Format: The first line contains the string S modified based on the given conditions.
Boundary Conditions: Length of S is from 3 to 100. 
Example Input/Output 1: 
Input: abcd_pqrs 
Output: dcba_pqrs 
Example Input/Output 2: 
Input: _kilo 
Output: _kilo 
Example Input/Output 3: 
Input: nounderscore 
Output: erocsrednuon

S = input()
if '_' in S:
    index = S.index('_')
    S = S[:index][::-1] + S[index:]
else:
    S = S[::-1]
print(S)
