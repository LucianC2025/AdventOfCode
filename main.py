import pandas as pd

# Write a FUNCTION for each day's puzzle
def day01():
    print("Day 01")
    # Set up empty list
    left = []
    right = []
    # Read TXT file
    file = open('Day1Input.txt', 'r')
    split = [line.strip() for line in file]
    for line in split:
        left.append(line.split('   ')[0]) # line.split('   ') takes a row and splits the left side into [0] and the right side into [1], and is split by three spaces
        right.append(line.split('   ')[1])
    print(left)
    # Pair the smallest number in left with the smallest number in right list
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    print("****** Sorted LISTS! (Least to Greatest) ******")
    for (l, r) in zip(sorted_left, sorted_right):
        print(l, r) # current pair
        # follow procedure in puzzle instructions
            


    data2 = {'location ID': [sorted_left, sorted_right]}
    df = pd.DataFrame(data2)
    print(df)






def main():
    # UPDATE this method call for each puzzle
    day01()


if __name__ == "__main__":
    main()