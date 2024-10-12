n = int(input())
def print_subsets(l):
    print('{', end='')
    print(*l, sep=', ',end='')
    print('}')
    if(len(l) < n):
        for i in range((0 if len(l) == 0 else l[-1]) + 1, n + 1):
            print_subsets(l+[i])
print_subsets([])
