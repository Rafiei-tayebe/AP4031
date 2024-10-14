s = input()
for letter in s:
    if not letter.isalpha() :
        s = s.replace(letter,' ')

for word in s.split():
    if len(word) >= 5 and not word.isupper():
        count = 0
        for letter in word:
            if letter not in 'aeiouy':
                count += 1
            else:
                count = 0
            if count >= 5 :
                print(word, end=' ')
                break
