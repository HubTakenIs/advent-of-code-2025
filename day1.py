class Dial:
    def __init__(self):
        self.position = 50
        self.zeroes = 0
    
    def process_line(self,line):
        direction = line[0]
        distance = int(line[1:])
        return direction,distance
    def turn_dial(self, line):
        print(f"current dial position: {self.position}")
        direction, distance = self.process_line(line)
        print(f"turning {direction}, for {distance} click(s)")
       
        div = divmod(distance,100)

        if div[0] > 0:
            distance = div[1]

        if direction == "L":
            temp = self.position - distance
            if temp < 0:
                self.position = 100 + temp
            if temp == 0:
                self.position = temp
                self.zeroes +=1
            if temp > 0:
                self.position = temp

        if direction == "R":
            temp = self.position + distance
            if temp > 99:
                self.position = 0 + (temp-100)
            if temp <= 99:
                self.position = temp
            if self.position == 0:
                self.zeroes +=1
        print(f"Turned Dial to position {self.position}")
def main():
    with open("day1_input") as f:
        lines = f.read().splitlines()
    print(lines)
    print(f"read lines: {len(lines)}")
    print(f"line to be processed: {lines[0]}")

    dial = Dial()
    # that's bad. dial doesn't need to contain process_lines.
    for line in lines:
        dial.turn_dial(line)
    print(f"password should be: {dial.zeroes}")
    # I need to track of how many times the dial has hit 0.
    # initial position is 50.
    # 
    


if __name__ == "__main__":
    main()



