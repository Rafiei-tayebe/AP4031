s = input()
while True:
    ins = input()
    if 'SHIFT-L' in ins and len(s) != 0 :
        N = int(ins.split()[1])
        if N > len(s): N = N % len(s)
        f = s[N:]
        l = s[:N]
        s = f + l
    elif 'SHIFT-R' in ins and len(s) != 0 :
        N = int(ins.split()[1])
        if N > len(s): N = N % len(s)
        f = s[-N:]
        l = s[:-N]
        s = f + l
    elif 'EXTEND' in ins:
        N = int(ins.split()[1])
        s = s+ '*'*N
    elif 'SHRINK' in ins:
        N = int(ins.split()[1])
        if N >= len(s): s = ''
        else:
            s = s[:-N]
    elif 'REVERSE' in ins and len(s) != 0 :
        s = s[-1::-1]
    elif 'PUT' in ins and len(s) != 0 :
        I = int(ins.split()[1])
        C = ins.split()[2]
        s = s[:I-1] + C + s[I:] 
    elif 'PRINT' in ins:
        print(s)
    elif 'EXIT' in ins:
        break
