from delivery import Delivery
from algorithms import (
    maximum_deliveries,
    minimum_drivers,
    minimum_rejections,
)


def make_deliveries(intervals):
    result = []

    for i, (start, finish) in enumerate(intervals, start=1):
        result.append(
            Delivery(
                id=f"D{i}",
                start_time=start,
                finish_time=finish,
            )
        )

    return result


def test_task_a():
    tests = [
        ([], 0),
        ([(1, 3)], 1),
        ([(1, 3), (3, 5), (5, 7)], 3),
        ([(1, 5), (2, 6), (3, 7)], 1),
        ([(5, 7), (1, 3), (3, 5), (2, 4)], 3),
        ([(1, 4), (2, 4), (4, 6)], 2),
    ]

    for number, (intervals, expected) in enumerate(tests, start=1):
        deliveries = make_deliveries(intervals)
        result = len(maximum_deliveries(deliveries))

        assert result == expected, (
            f"Task A Test {number}: "
            f"expected {expected}, got {result}"
        )

        print(f"Task A Test {number}: PASS")


def test_task_b():
    tests = [
        ([], 0),
        ([(1, 3)], 1),
        ([(1, 3), (3, 5), (5, 7)], 1),
        ([(1, 5), (2, 6), (3, 7)], 3),
        ([(1, 4), (2, 5), (4, 7), (5, 8)], 2),
        ([(5, 8), (1, 4), (2, 5), (4, 6), (6, 9)], 2),
    ]

    for number, (intervals, expected) in enumerate(tests, start=1):
        deliveries = make_deliveries(intervals)
        result = len(minimum_drivers(deliveries))

        assert result == expected, (
            f"Task B Test {number}: "
            f"expected {expected}, got {result}"
        )

        print(f"Task B Test {number}: PASS")


def test_task_c():
    tests = [
        ([], 0),
        ([(1, 3)], 0),
        ([(1, 3), (3, 5), (5, 7)], 0),
        ([(1, 5), (2, 6), (3, 7)], 2),
        ([(5, 7), (1, 3), (3, 5), (2, 4)], 1),
        ([(1, 2), (2, 3), (3, 4), (1, 3)], 1),
    ]

    for number, (intervals, expected) in enumerate(tests, start=1):
        deliveries = make_deliveries(intervals)
        result = minimum_rejections(deliveries)

        assert result == expected, (
            f"Task C Test {number}: "
            f"expected {expected}, got {result}"
        )

        print(f"Task C Test {number}: PASS")


if __name__ == "__main__":
    test_task_a()
    test_task_b()
    test_task_c()

    print("\nAll required tests passed.")
    