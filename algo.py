
import random

a=input("Enter a sentence: ")
population = 200
generations = 0
mutation = 0.01

alphabet = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#*+-$&?<>{}()|\/! "
target = a
output = ""
data = []
pool = []
score_range = []

class Item:
    def __init__(self, data, target):
        self.target = target
        self.data = data
        self.score = self.get_score()

    def get_score(self):
        score = 0
        for i in range(len(self.data)):
            if self.data[i] == self.target[i]:
                score += 1
        return score / len(self.data)

    def __str__(self):
        return 'String: ' + ''.join(self.data) + ', Score: ' + str(self.score)

# SETUP
for i in range(population):
    data.append(Item([random.choice(alphabet) for item in [0] * len(target)], target))

while output != target:

    pool = []

    # SELECTION
    for item in data:
        if item != 0:
            for i in range(int(item.score * 100)):
                pool.append(item)

    # REPEAT
    # PICK 2 PARENTS
    # CROSSOVER
    # MUTATION
    # ADD NEW CHILD TO POPULATION

    data = []
    while len(data) < population:
        parentA = pool[random.randint(0,len(pool)-1)]
        parentB = pool[random.randint(0,len(pool)-1)]

        parentAScore = int(parentA.score / (parentA.score + parentB.score) * 100)
        parentBScore = int(parentB.score / (parentA.score + parentB.score) * 100)

        childData = []
        for i in range(len(target)):
            choice_list = [parentA.data[i]] * int(parentAScore) + [parentB.data[i]] * int(parentBScore)
            childData.append(random.choice(choice_list))

        for i in range(len(childData)):
            m = mutation * 100
            r = random.randint(0,100/m)
            if r == 0:
                childData[i] = random.choice(alphabet)

        child = Item(childData, target)
        data.append(child)
        output = "".join(child.data)
        if output == target:
            break
    best = None
    for i in range(len(data)):
        if best == None:
            best = data[i]
        elif data[i].score > best.score:
            best = data[i]
    print(best)
    generations += 1
print("Generation: " + str(generations))
