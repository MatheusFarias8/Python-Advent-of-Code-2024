import re

def main():
    memory = get_lines("input.txt")
    new_memory = format_memory(memory)
    mults = check_pattern(new_memory)
    total = sum(mults)
    print(f"TOTAL: {total}")


def get_lines(txt):
    memory = []
    with open(txt) as file:
        for line in file.readlines():
            memory.append(line.strip())
    return "".join(memory)

def check_pattern(str):
    nums = []
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, str)
    for num in matches:
        multiply = int(num[0]) * int(num[1])
        nums.append(multiply)
    return nums

def format_memory(memory):
    sliced = re.sub(r"don't.*?do\(.*?\)", "", memory)
    return sliced

if __name__ == "__main__":
    main()