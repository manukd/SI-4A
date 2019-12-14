import random
from Character import Character
from Army import Army
import csv

if __name__ == '__main__':
    with open('characters.csv') as csvfile:
        csvreader = csv.DictReader(csvfile)
        line_count = 0
        characters_list = []
        i = 0
        for row in csvreader:
            characters_list.append(Character(row["name"], row["first name"], row["age"], row["profession"], row["morale value"]))
            i = i + 1
    """rand = random.randrange(20,100)
    Army1 = Army(characters_list[0], rand)
    rand = random.randrange(20, 100)
    Army2 = Army(characters_list[1], rand)
    rand = random.randrange(20, 100)
    Army3 = Army(characters_list[2], rand)
    rand = random.randrange(20, 100)
    Army4 = Army(characters_list[3], rand)
    rand = random.randrange(20, 100)
    Army5 = Army(characters_list[4], rand)"""
    sum = 0.0
    for i in range(len(characters_list)):
        rand = random.randrange(20, 100)
        ArmyX = Army(characters_list[i], rand)
        sum += ArmyX.get_total_morale()
    print(sum)
