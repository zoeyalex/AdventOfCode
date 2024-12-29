def get_distance(pair):
    return max(pair) - min(pair)

def main():
    left_list, right_list = ([] for _ in range(2))

    with open(file='input', mode='r') as f:
        for line in f:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    left_list = sorted(left_list)
    right_list = sorted(right_list)

    return sum(get_distance(pair) for pair in zip(left_list, right_list))

if __name__ == '__main__':
    print(main())
