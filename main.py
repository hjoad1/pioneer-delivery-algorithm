import csv
import sys

from delivery import Delivery
from algorithms import (
    maximum_deliveries,
    minimum_drivers,
    minimum_rejections,
)


def read_deliveries(filename):
    deliveries = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            delivery = Delivery(
                id=row["id"],
                start_time=int(row["start_time"]),
                finish_time=int(row["finish_time"]),
            )

            if delivery.start_time >= delivery.finish_time:
                raise ValueError(
                    f"{delivery.id}: start time must be less than finish time."
                )

            deliveries.append(delivery)

    return deliveries


def print_task_a(deliveries):
    selected = maximum_deliveries(deliveries)

    print("\nTASK A: Maximum Deliveries for One Driver")
    print("-----------------------------------------")

    for delivery in selected:
        print(
            f"{delivery.id}: "
            f"{delivery.start_time} -> {delivery.finish_time}"
        )

    print(f"Total deliveries completed: {len(selected)}")


def print_task_b(deliveries):
    schedules = minimum_drivers(deliveries)

    print("\nTASK B: Minimum Number of Drivers")
    print("---------------------------------")

    for driver_id in sorted(schedules):
        print(f"Driver {driver_id}:")

        for delivery in schedules[driver_id]:
            print(
                f"  {delivery.id}: "
                f"{delivery.start_time} -> {delivery.finish_time}"
            )

    print(f"Minimum drivers required: {len(schedules)}")


def print_task_c(deliveries):
    rejected = minimum_rejections(deliveries)

    print("\nTASK C: Minimum Deliveries Rejected")
    print("-----------------------------------")
    print(f"Minimum deliveries rejected: {rejected}")


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "deliveries.csv"

    deliveries = read_deliveries(filename)

    print_task_a(deliveries)
    print_task_b(deliveries)
    print_task_c(deliveries)


if __name__ == "__main__":
    main()
    s