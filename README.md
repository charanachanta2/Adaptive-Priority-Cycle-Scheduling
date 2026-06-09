# Adaptive Priority Cycle Scheduling (APCS)

## Overview
Adaptive Priority Cycle Scheduling (APCS) is a dynamic traffic signal scheduling algorithm designed to optimize traffic flow at road intersections.

Unlike traditional fixed-time traffic signal systems, APCS continuously evaluates traffic conditions and dynamically generates a complete signal cycle based on:
- Vehicle Count
- Traffic Density
- Waiting Score

The algorithm determines signal order and green signal durations according to real-time traffic conditions while ensuring fairness among all directions.

## Key Features
- Dynamic Signal Scheduling
- Density-Based Decision Making
- Waiting-Based Fairness
- Adaptive Green Time Allocation
- Cycle-Based Operation

## Priority Formula

Priority Score =

0.5 × Vehicle Score +
0.3 × Density Score +
0.2 × Waiting Score

Density = Vehicles(i) / Total Vehicles

Density Score = Density × 100

## Green Time Allocation

Green Time(i) = Priority(i) / ΣPriority × 60

Constraints:
- MIN_GREEN = 10 seconds
- MAX_GREEN = 40 seconds

## Workflow

Vehicle Count
→ Density Calculation
→ Priority Score Calculation
→ Direction Selection
→ Green Time Allocation
→ Waiting Score Update
→ Next Cycle Generation

## Components

1. get_vehicle_counts()
2. calculate_density()
3. calculate_priority()
4. generate_cycle()
5. allocate_green_times()
6. update_waiting_counter()
7. print_cycle()

## Time Complexity

Cycle generation uses Python's Timsort.

- Best Case: O(n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

## Future Enhancements

- Traffic Growth Rate Analysis
- Cycle Stability Mechanism
- Traffic Prediction Module
- Emergency Vehicle Prioritization
- Adaptive Weight Optimization

## Applications

- Smart Cities
- Intelligent Transportation Systems
- Urban Traffic Management
- IoT Traffic Monitoring
- Smart Intersections
