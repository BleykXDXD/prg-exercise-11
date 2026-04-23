class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        points = self.scores[index]
        if points >= 0 and points <= 49:
            return "F"
        elif points >= 50 and points <= 59:
            return "E"
        elif points >= 60 and points <= 69:
            return "D"
        elif points >= 70 and points <= 79:
            return "C"
        elif points >= 80 and points <= 89:
            return "B"
        else:
            return "A"

    def find(self, points):
        return self.scores.index(points)

    def get_sorted(self):
        scores_copy = self.scores.copy()
        for num in range(len(scores_copy)):
            for j in range(0, len(scores_copy) - num - 1):
                if scores_copy[j] > scores_copy[j + 1]:
                    scores_copy[j], scores_copy[j + 1] = scores_copy[j + 1], scores_copy[j]

        return scores_copy
def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    count1 = results.count()
    print(f"Test psalo: {count1} studentu")

    for idx, points in enumerate(results.scores):
        mark = results.get_grade(idx)
        print(f"Student {idx}: {points} points – {mark}")

        if points == 100:
            print(f"Student {idx} mel 100 bodu")


print(main())
# if __name__ == "__main__":
#     # results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
#     #
#     # print(results.count())  # 9
#     # print(results.get_by_index(2))  # 91
#     # print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]
#     # print(results.get_grade(6))
#     # print(results.find(73))
#     # print(results.get_sorted())