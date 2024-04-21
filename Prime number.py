An integer value N is passed as the input. 
The program must print YES if N is prime number.
Else the program must print NO. 
Input Format: The first line denotes the value of N. 
Output Format: YES or NO based on if N is a prime number or not. 
(The OUTPUT is CASE SENSITIVE). Boundary Conditions: 2 <= N <= 9999999 
Example Input/Output 1: Input: 19 Output: YES 
Example Input/Output 2: Input: 189210 Output: NO

N = int(input())
if N < 2:
    print("NO")
else:
    is_prime = True
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            is_prime = False
            break
    print("YES" if is_prime else "NO")
