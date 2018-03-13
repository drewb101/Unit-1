def course_grader(test_scores):
    sum = 0
    n = 0

    for score in test_scores:
        sum = sum + score
        n += 1
        if score < 50:
            return "fail"

    avg_score = sum / n

    if avg_score >= 70:
        return "pass"
    else:
        return "fail"


def main():
    print(course_grader([100, 75, 45]))  # "fail"
    print(course_grader([100, 70, 85]))  # "pass"
    print(course_grader([80, 60, 60]))  # "fail"
    print(course_grader([80, 80, 90, 30, 80]))  # "fail"
    print(course_grader([70, 70, 70, 70, 70]))  # "pass"


if __name__ == "__main__":
    main()
