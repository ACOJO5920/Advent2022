
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


