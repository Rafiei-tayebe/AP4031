buy = int(input())
current = int(input())
count = int(input())
valid = False

if 1000 <= buy <= 100000 and buy % 10 == 0 :
    if 1000 <= current <= 100000 and buy % 10 == 0 :
        if 50 <= count <= 5000:
            valid = True

if valid:
    diff = current - buy
    if diff >= 0:
        print('Profit')
        print(f'+{(diff/buy*100):.2f}')
        if current * count > 5000000 and diff/buy > 0.20 :
            print('Lucky')
        else:
            print('Normal')
    else:
        print('Loss')
        print(f'{(diff/buy*100):.2f}')
        if (buy + diff) * count and diff/buy > -0.20:
            print('Chance')
        else:
            print('under the coverage')

        
else:
    print('Invalid Input')
