def main():

    #part 1
    reports = get_lines("input.txt")
    safe_part1 = sum(map(safe_check, reports))
    print(f"PART 1 = {safe_part1}")

    #part2
    safe_part2 = 0
    for repo in reports:
        safe_part2 += (safe_check(repo) or any(safe_check(repo[:i] + repo[i+1:]) for i in range(len(repo))))
    print(f"PART 2 = {safe_part2}")


def get_lines(txt):
    reports = []
    with open(txt) as file:
        for line in file.readlines():
            reports.append([int(x) for x in line.split()])
    return reports


def safe_check(reports):
    lenght = len(reports)
    return ((all(1 <= reports[i+1] - reports[i] <= 3 for i in range(lenght-1)))
            or (all(1 <= reports[i] - reports[i+1] <= 3 for i in range(lenght-1))))


if __name__ == "__main__":
    main()