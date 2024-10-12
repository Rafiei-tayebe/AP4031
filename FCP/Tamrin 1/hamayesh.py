r, c = map(int, input().split())
if c > 10: 
    print(f'Left {11-r} {21-c}')
else:
    print(f'Right {11-r} {c}')

