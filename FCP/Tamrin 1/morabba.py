n = int(input())
s = n//2 - 1
t = n - 4
for i in range(n):
    if i == 0 or i == n-1:
        print('#'*n)
    else:
        print('#', end='')
        print(' '*(s-abs(i - s - 1)), end='')
        print('#', end='')  
        if i != n//2:                        
            print(' '*abs(t), end='')
            print('#', end='')
            t -= 2             
        print('#'*(s-abs(i - s - 1)), end='')
        print('#')
