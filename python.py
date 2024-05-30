class myclass:
    def __init__(self):
        self.myFav = {'Paris': 500, 'New York City': 600}

    def get_extraCost(self, dist):
        return self.myFav.get(dist, 0)

    def validThis(self, dist):
        return isinstance(dist, str)


class passanger:
    def __init__(self, num):
        self.num = num

    def validNumber(self):
        return isinstance(self.num, int) and 0 < self.num <= 80

    def forHereDiscount(self):
        if 4 < self.num < 10:
            return 0.1
        elif self.num >= 10:
            return 0.2
        else:
            return 0.0


class total_TIME:
    def __init__(self, dur):
        self.dur = dur

    def is_valid_total_TIME(self):
        return isinstance(self.dur, int) and self.dur > 0

    def getFee(self):
        return 200 if self.dur < 7 else 0

    def getTheBestPromoEver(self):
        return 200 if self.dur > 30 else 0


class Vacation_:
    costBas = 1000

    def __init__(self, dist, num, dur):
        self.myclass = myclass()
        self.passanger = passanger(num)
        self.total_TIME = total_TIME(dur)
        self.dist = dist

    def sum(self):
        if not self.myclass.validThis(self.dist):
            return -1
        if not self.passanger.validNumber():
            return -1
        if not self.total_TIME.is_valid_total_TIME():
            return -1

        numberTotal = self.costBas
        numberTotal += self.myclass.get_extraCost(self.dist)
        numberTotal += self.total_TIME.getFee()
        numberTotal -= self.total_TIME.getTheBestPromoEver()

        discount = self.passanger.forHereDiscount()
        numberTotal -= numberTotal * discount

        return max(int(numberTotal), 0)


def main():
    # Inputs
    dist = "Paris"
    num = 5
    dur = 10

    # Calculate vacation package cost
    calculator = Vacation_(dist, num, dur)
    cost = calculator.sum()

    # Outputs
    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")


if __name__ == "__main__":
    main()
