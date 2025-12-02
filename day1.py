class Dial:
    def __init__(self):
        self.position = 50
        self.zeroes = 0

    def process_line(self, line):
        direction = line[0]
        distance = int(line[1:])
        return direction, distance

    def turn_dial(self, line):
        direction, distance = self.process_line(line)
        div = divmod(distance, 100)
        new_pos = 0
        # print(f"div: 0| {div[0]} : 1|{div[1]}")

        if direction == "L":
            new_pos = (self.position - div[1]) % 100
            if self.position - div[1] <= 0 and self.position != 0:
                # rolled.
                # print("counted roll for L")
                self.zeroes += 1

        if direction == "R":
            new_pos = (self.position + div[1]) % 100
            if self.position + div[1] >= 100:
                # rolled
                # print("counted roll for R")
                self.zeroes += 1

        if div[0] > 0:
            self.zeroes += div[0]

        self.position = new_pos
        # print("new pos: ", new_pos)


def main():
    with open("day1_input") as f:
        lines = f.read().splitlines()
    dial = Dial()
    for line in lines:
        dial.turn_dial(line)
    print(f"password should be: {dial.zeroes}")


if __name__ == "__main__":
    main()
