A string value S is passed as the input. 
The program must print the first letter of each word in S in upper case. 
Input Format: First line will contain the string value S 
Output Format: First line will contain the string value with the first letter of each word in S in upper case. 
Boundary Conditions: Length of S is from 5 to 500
Example Input/Output 1: Input: She is happy. Output: She Is Happy. 
Example Input/Output 2: Input: joIN tHE ParTY Output: JoIN THE ParTY


a=input()
l=list(a)
for i in range(len(l)):
    if(i==0):
        l[i]=l[i].capitalize()
    elif(l[i]==" "):
        l[i+1]=l[i+1].capitalize()
string=""
print(string.join(l))
