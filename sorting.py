import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(numbers):
    numbs = numbers.copy()
    for num in range(len(numbers)):
        smallest = num
        for j in range(num, len(numbs)):
            plt.ion()
            plt.show()
            if numbs[j] < numbs[smallest]:
                smallest = j

        numbs[num], numbs[smallest] = numbs[smallest], numbs[num]
    return numbs


def bubble_sort(numbers):
    numbs = numbers.copy()
    plt.ion()
    plt.show()
    for num in range(len(numbers)):
        for j in range(0, len(numbs) - num - 1):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(numbs)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(numbs)), numbs, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if numbs[j] > numbs[j+1]:
                numbs[j], numbs[j+1] = numbs[j+1], numbs[j]
    plt.ioff()
    plt.show()
    return numbs

if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    # print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    sort = selection_sort([5, 1, 4, 2, 8])
    # print(sort)
    bubble = bubble_sort(random_numbers(20))
    print(bubble)

    small = random_numbers(5, low=0, high=20)# 5 čísel v rozsahu 0–20
    # print(small)