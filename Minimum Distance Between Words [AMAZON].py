A string S is passed as the input. 
Two words W1 and W2 which are present in the string S are also passed as the input. 
The program must find the minimum distance D between W1 and W2 in S (in forward or reverse order) and print D as the output.
Input Format: The first line will contain S. 
The second line will contain W1. 
The third line will contain W2.
Output Format: The first line will contain D - the minimum distance between W1 and W2 in S. 
Boundary Conditions: Length of S is from 5 to 200.
Example Input/Output 1: Input: the brown quick frog quick the the quick Output: 1 
Explanation: quick and the are adjacent as the last two words. Hence distance between them is 1.
Example Input/Output 2: Input: the quick the brown quick brown the frog quick frog Output: 3


words = input().split()
a = input().strip()
b = input().strip()
indices_a = [i for i, word in enumerate(words) if word == a]
indices_b = [i for i, word in enumerate(words) if word == b]
if a == b:
    if len(indices_a) >= 2:
        print(indices_a[1] - indices_a[0])
    else:
        print(0)
else:
    if indices_a and indices_b:
        min_distance = min(abs(i - j) for i in indices_a for j in indices_b)
        print(min_distance)
    else:
        print(-1)
