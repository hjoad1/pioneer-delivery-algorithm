import heapq
from delivery import Delivery


# ---------------------------------------------------------
# Task A: Maximum Deliveries for One Driver
# ---------------------------------------------------------

def maximum_deliveries(deliveries):
    # Earliest-finish-time-first:
    # sort deliveries by finishing time
    sorted_deliveries = sorted(
        deliveries,
        key=lambda d: (d.finish_time, d.start_time)
    )

    selected = []
    last_finish = None

    for delivery in sorted_deliveries:
        # If this is the first delivery, take it.
        # Otherwise, take it only if it starts after or exactly
        # when the last selected delivery finishes.
        if last_finish is None or delivery.start_time >= last_finish:
            selected.append(delivery)
            last_finish = delivery.finish_time

    return selected


# ---------------------------------------------------------
# Task B: Minimum Number of Drivers
# ---------------------------------------------------------

def minimum_drivers(deliveries):
    # Earliest-start-time-first
    sorted_deliveries = sorted(
        deliveries,
        key=lambda d: (d.start_time, d.finish_time)
    )

    # Heap entries are:
    # (finish time of driver's last delivery, driver ID)
    heap = []

    # driver ID -> list of deliveries assigned to that driver
    schedules = {}

    next_driver_id = 1

    for delivery in sorted_deliveries:

        # The heap root is the driver who becomes available first.
        if heap and heap[0][0] <= delivery.start_time:
            _, driver_id = heapq.heappop(heap)

        else:
            # No existing driver is available, so create a new one.
            driver_id = next_driver_id
            next_driver_id += 1
            schedules[driver_id] = []

        schedules[driver_id].append(delivery)

        # Driver is now busy until this delivery finishes.
        heapq.heappush(
            heap,
            (delivery.finish_time, driver_id)
        )

    return schedules


# ---------------------------------------------------------
# Task C: Minimum Deliveries Rejected
# ---------------------------------------------------------

def minimum_rejections(deliveries):
    selected = maximum_deliveries(deliveries)

    return len(deliveries) - len(selected)
