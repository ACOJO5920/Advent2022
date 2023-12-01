def main():
    with open('Day1Input1.txt') as file:
        biggest_cals = 0

        current_elf_cals = 0
        for line in file.readlines():

            if line == "\n":
                if current_elf_cals > biggest_cals:
                    biggest_cals = current_elf_cals
                current_elf_cals = 0
            else:
                current_elf_cals += int(line)

        if current_elf_cals > biggest_cals:
            biggest_cals = current_elf_cals

        return biggest_cals


def main_2():
    with open('Day1Input1.txt') as file:
        biggest_cals = Cals()

        current_elf_cals = 0
        for line in file.readlines():

            if line == "\n":
                if current_elf_cals > biggest_cals.get_smallest()[0]:
                    biggest_cals.insert(current_elf_cals)

                current_elf_cals = 0
            else:
                current_elf_cals += int(line)

        if current_elf_cals > biggest_cals.get_smallest()[0]:
            biggest_cals.insert(current_elf_cals)

        return biggest_cals.sum()


class Cals:
    def __init__(self):
        self.data = [0, 0, 0]

    def get(self):
        return self.data

    def insert(self, value):

        if not self.is_full():
            for ix in range(3):
                if self.data[ix] == 0:
                    self.data[ix] = value
                    return
        else:
            smallest_ix = self.get_smallest()[1]
            self.data[smallest_ix] = value

    def sum(self):
        total = 0
        for cal in self.data:
            total += cal
        return total

    def get_smallest(self):
        smallest = 999999
        smallest_ix = -1
        for ix in range(3):
            if self.data[ix] < smallest:
                smallest = self.data[ix]
                smallest_ix = ix

        return smallest, smallest_ix

    def is_full(self):
        return not (0 in self.data)
