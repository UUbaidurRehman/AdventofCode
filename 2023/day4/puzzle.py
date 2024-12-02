def calculatePointsPart1(cards):
    totalPoints = 0
    
    for card in cards:
        numbers = card.split(":")[1].split("|")

        winniningNumbers =  numbers[0].strip().split()
        yourNumbers =  numbers[1].strip().split()

        # Using sets for constant lookups 
        winniningNumbers = {int(number) for number in winniningNumbers}
        yourNumbers = {int(number) for number in yourNumbers}
           
        points = 0

        for number in yourNumbers:
            if number in winniningNumbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2

        totalPoints += points

    print(totalPoints)


def calculatePointsPart2(cards):
    cardArr = [1 for i in range(len(cards))]

    for i in range(len(cards)):
        numbers = cards[i].split(":")[1].split("|")

        winniningNumbers =  numbers[0].strip().split()
        yourNumbers =  numbers[1].strip().split()
        
        winniningNumbers = {int(number) for number in winniningNumbers}
        yourNumbers = {int(number) for number in yourNumbers}
           
        count = 0

        for number in yourNumbers:
            if number in winniningNumbers:
                count += 1
        
        loopLimit = min(i + count + 1, len(cards))

        for j in range(i + 1, loopLimit):
            cardArr[j] += cardArr[i]

    print(sum(cardArr))


filePath = "input2.txt"
with open(filePath, "r", encoding="utf-8") as file:
    data = file.read()

rows = data.strip().split("\n")
calculatePointsPart1(rows) 
calculatePointsPart2(rows) 