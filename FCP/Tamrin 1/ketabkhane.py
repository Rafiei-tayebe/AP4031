library = []
n = int(input())
for i in range(n):
    library.append(input())
command = input()
while command!="Exit":
    if command == "AddLeft":
        library.insert(0, input())
    if command == "AddRight":
        library.append(input())
    if command == "DeleteLeft":
        library.pop(0)
    command = input()
n = len(library)
print(n)
for i in range(n):
    print(library[i])
