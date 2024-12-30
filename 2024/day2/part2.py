
def is_in_range(pair):
    return max(pair) - min(pair) in range(1, 4)

def is_safe(report):
    n = len(report)
    # increasing
    if report[0] < report[1]:
        trend = -1
    # decreasing
    elif report[0] > report[1]:
        trend = 1
    else:
        return False

    for l, r in zip(range(n-1), range(1, n)):
        if not is_in_range((report[l], report[r])) or (report[l] - report[r]) * trend < 0:
            return False

    return True

def is_safe_with_dampen(report):
    n = len(report)
    if is_safe(report):
        return True

    for i in range(n):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True

    return False

def main():
    safe = 0
    with open(file='input', mode='r') as f:
        for line in f:
            if is_safe_with_dampen([int(report) for report in line.split()]):
                safe += 1
    return safe

if __name__ == '__main__':
    print(main())
