n = int(input())
mod = n%4
div = n//4
if mod == 0:
    print(-1*div, div)
elif mod == 1:
    print(-1*div, -1*div)
elif mod == 2:
    print(div+1, -1*div)
elif mod == 3:
    print(div+1, div+1)
