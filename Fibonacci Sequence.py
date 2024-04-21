An integer value N is passed as the input. 
The program must print the first N terms in the Fibonacci sequence. 
Input Format: The first line denotes the value of N. 
Output Format: The first N terms in the Fibonacci sequence (with each term separated by a space)
Boundary Conditions: 3 <= N <= 50 
Example Input/Output 1: Input: 5 Output: 0 1 1 2 3 
Example Input/Output 2: Input: 10 Output: 0 1 1 2 3 5 8 13 21 34

N = int(input())
fibonacci = [0, 1]

for i in range(2, N):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

print(*fibonacci[:N])
