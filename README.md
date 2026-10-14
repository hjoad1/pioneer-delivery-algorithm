# Pioneer Delivery Company's Algorithm Portfolio
## Part I: Greedy Algorithms

### Language

Python 3

### Files

- `main.py` - reads delivery data and runs Tasks A, B, and C
- `delivery.py` - defines the Delivery class
- `algorithms.py` - contains the greedy algorithms
- `tests.py` - tests the required cases
- `deliveries.csv` - sample input data

---

## Running the Program

Run:

python main.py deliveries.csv

To run the required tests:

python tests.py

---

## Input File Format

The input file is a CSV file with the following columns:

id,start_time,finish_time

Example:

D01,10,13
D02,2,5
D03,4,7

Each delivery must have a start time smaller than its finish time.

---

# Task A: Maximum Deliveries for One Driver

### Greedy Choice

The algorithm sorts all deliveries by increasing finish time and
repeatedly chooses the next delivery that starts at or after the finish
time of the last selected delivery.

### Why the Greedy Strategy Is Optimal

The delivery with the earliest finish time is a safe first choice.
Suppose an optimal solution starts with a different delivery. Replacing
that first delivery with the earliest-finishing delivery cannot make any
later delivery incompatible, because the greedy delivery finishes no
later. Therefore, there is an optimal solution containing the greedy
choice. Repeating this argument gives an optimal schedule.

### Running Time

Sorting the deliveries by finish time takes O(n log n).
The algorithm then scans the sorted list once in O(n) time.

Therefore, the total running time is O(n log n).

---

# Task B: Minimum Number of Drivers

### Information Stored in the Priority Queue

The priority queue stores each currently used driver's next available
time, which is the finish time of that driver's most recently assigned
delivery. The driver ID is stored with the finish time.

### Selecting a Driver

The deliveries are processed in increasing order of start time.

For each delivery, the algorithm checks the driver with the earliest
finish time. If that driver's finish time is less than or equal to the
new delivery's start time, that driver is reused.

If no driver is available, a new driver is created.

### Why the Algorithm Uses the Minimum Number of Drivers

A new driver is created only when every existing driver is still busy
when the current delivery begins. At that point, the current delivery
overlaps with deliveries assigned to all existing drivers.

Therefore, any valid schedule must use at least one more driver.
The algorithm only creates a driver when this is necessary, so the
number of drivers is minimum.

### Running Time

Sorting by start time takes O(n log n).

Each delivery causes a constant number of priority-queue operations,
and each priority-queue operation takes O(log n).

Therefore, the total running time is O(n log n).

---

# Task C: Minimum Number of Rejected Deliveries

Task C is directly related to Task A.

If there are n total deliveries and Task A finds a maximum compatible
set containing k deliveries, then the minimum number that must be
rejected is:

n - k

The same Task A algorithm is therefore used first, so the total running
time remains O(n log n).

---

# Task D: When a Greedy Choice Fails

Consider three deliveries:

| Delivery | Ready Time | Profit |
|----------|------------|--------|
| D1       | 0          | 6      |
| D2       | 0          | 4      |
| D3       | 1          | 2      |

The proposed greedy strategy considers deliveries in decreasing order
of profit.

Therefore, the greedy order is D1, D2, D3.

### Greedy Schedule G

D1 is scheduled at time 0.

D2 is scheduled at time 1.

D3 is scheduled at time 2.

The values are:

D1: 6 / (1 + 0) = 6

D2: 4 / (1 + 1) = 2

D3: 2 / (1 + 1) = 1

Therefore:

V(G) = 6 + 2 + 1 = 9

### Better Schedule S

Instead, use:

D1 at time 0

D3 at time 1

D2 at time 2

The values are:

D1: 6 / (1 + 0) = 6

D3: 2 / (1 + 0) = 2

D2: 4 / (1 + 2) = 4/3

Therefore:

V(S) = 6 + 2 + 4/3 = 28/3 ≈ 9.33

Since 28/3 > 9, this schedule has a larger total value than the
schedule produced by the proposed greedy strategy.

Therefore, the proposed decreasing-profit greedy strategy is not
always optimal.

---

# Required Test Results

## Task A

Test 1: 0
Test 2: 1
Test 3: 3
Test 4: 1
Test 5: 3
Test 6: 2

## Task B

Test 1: 0
Test 2: 1
Test 3: 1
Test 4: 3
Test 5: 2
Test 6: 2

## Task C

Test 1: 0
Test 2: 0
Test 3: 0
Test 4: 2
Test 5: 1
Test 6: 1
