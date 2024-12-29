from collections import Counter


def main():
    left_list, right_list = ([] for _ in range(2))

    with open(file='input', mode='r') as f:
        for line in f:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    right_counter = Counter(right_list)
    return sum(num * right_counter[num] for num in left_list if num in right_counter)

if __name__ == '__main__':
    print(main())
