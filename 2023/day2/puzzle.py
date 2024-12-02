with open("input2.txt", "r") as f:
    f = f.read()
    files = f.split("\n")
    lst = []
    reds = 12
    greens = 13
    blues = 14

    for lines in files:

        line = lines.split(";")
        if len(lines) == 0:
            break
        found = False
        for words in line:
            blue, green, red = int(), int(), int()
            words = words.split(" ")
            for i, word in enumerate(words):
                if word == "blue," or word == "blue;" or word == "blue":
                    blue = blue + int(words[i - 1])
                elif word == "red," or word == "red;" or word == "red":
                    red = red + int(words[i - 1])
                elif word == "green," or word == "green;" or word == "green":
                    green = green + int(words[i - 1])
            if blue <= blues and red <= reds and green <= greens:
                found = True
            else:
                found = False
                break
            # if len(words) == 0:
            #     pass
        if found == True:
            num_ = line[0].split(":")
            num = num_[0].split(" ")
            lst.append(int(num[1]))
        else:
            pass
print(sum(lst))