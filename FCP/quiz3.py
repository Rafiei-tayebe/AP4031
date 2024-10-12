chats = {}

while True:
    command = input().split(' ', 2)
    action = command[0]

    if action == "Send":
        user = command[1]
        message = command[2]
        if user not in chats:
            chats[user] = []
            print(f"{user} added")
        chats[user].append(message)

    elif action == "Delete":
        user = command[1]
        message = command[2]
        if user in chats and message in chats[user]:
            chats[user].remove(message)
            if not chats[user]:
                del chats[user]
                print("History was cleared")

    elif action == "Search":
        word = command[1]
        for user in sorted(chats.keys()):
            for msg in chats[user]:
                if word.lower() in msg.lower():
                    print(f"{user}: {msg}")

    elif action == "Forward":
        user1 = command[1]
        user2 = command[2]
        if user1 in chats:
            if user2 not in chats:
                chats[user2] = []
                print(f"{user2} added")
            chats[user2].extend(chats[user1])

    elif action == "Exit":
        break
