def calculateWeightRange(rawWeight):
    if rawWeight % 1 == 0:
        return rawWeight

    if rawWeight > 20:
        return int(rawWeight) + 1

    if rawWeight % 1 <= 0.5:
        weight = int(rawWeight) + 0.5
    else:
        weight = int(rawWeight) + 1
    return weight


def main():
    print("Input 0 - Expect 0")
    print(calculateWeightRange(0))
    print("Input 0.2 - Expect 0.5")
    print(calculateWeightRange(0.2))
    print("Input 22 - Expect 22")
    print(calculateWeightRange(22))
    print("Input 22.1 - Expect 23")
    print(calculateWeightRange(22.1))
    print("Input 22.6 - Expect 23")
    print(calculateWeightRange(22.6))
    print("Input 3 - Expect 3")
    print(calculateWeightRange(3))
    print("Input 3.2 - Expect 3.5")
    print(calculateWeightRange(3.2))
    print("Input 3.8 - Expect 4")
    print(calculateWeightRange(3.8))


if __name__ == "__main__":
    main()
