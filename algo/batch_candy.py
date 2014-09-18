from collections import defaultdict

class Candy:
    def __init__(self, color):
        self.color = color

def batch_candy(candies):
    count = defaultdict(list)
    for candy in candies:
        count[candy.color].append(candy)

    batches = []
    while True:
        batch = []
        for color, candy in count.items():
            if candy:
                batch.append(candy[0].color)
                count[color].pop()
        if batch:
            batches.append(batch)
        else:
            break

    return batches

candies = [Candy("red"), Candy("red"), Candy("red"), Candy("blue"), Candy("blue"), Candy("yellow"), Candy("pink")]

print batch_candy(candies)
