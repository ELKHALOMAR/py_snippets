def power(inp):
    q = 0
    y = 0
    lenght = 12
    o = ["weak", "medium", "strong"]
    while not y > 1:
        user = inp
        q += 1
        if q > 1:
            user = input("please enter how strong: ")
        else:
            user = inp

        for x in o:
            if x == user:
                k = True
                break

            else:
                k = False
                continue
        print(k)
        if k == False:
            y = 0
            continue
        else:
            print("you chose", user)
            y = 2


    if user == o[0]:
        lenght = 6
    elif user == o[1]:
        lenght = 8
    else:
        lenght = 12

    return lenght

