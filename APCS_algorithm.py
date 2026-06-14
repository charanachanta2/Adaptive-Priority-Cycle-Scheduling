# Traffic Management System - Dynamic Cycle Scheduling
#Adaptive Priority Cycle Scheduling (APCS)
import APCS_algorithm

directions = ["North", "South", "East", "West"]

waiting_counter = [0, 0, 0, 0]

MIN_GREEN = 10
MAX_GREEN = 40
CYCLE_NUMBER = 1


def get_vehicle_counts():

    vehicles = []

    print("\n=== Vehicle Input ===")

    for direction in directions:
        count = int(
            input(f"Enter vehicles in {direction}: ")
        )
        vehicles.append(count)

    return vehicles


def calculate_density(vehicles):

    total = sum(vehicles)

    if total == 0:
        return [0] * len(vehicles)

    return [v / total for v in vehicles]


def calculate_priority(
        vehicles,
        densities,
        waiting_counter):

    priorities = []

    for i in range(len(directions)):

        vehicle_score = vehicles[i]

        density_score = densities[i] * 100

        waiting_score = waiting_counter[i]

        priority = (
            0.5 * vehicle_score +
            0.3 * density_score +
            0.2 * waiting_score
        )

        priorities.append(priority)

    return priorities


def generate_cycle(priorities):

    cycle = []

    for i in range(len(directions)):
        cycle.append(
            (
                directions[i],
                priorities[i],
                i
            )
        )

    cycle.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return cycle


def allocate_green_times(priorities):

    total_priority = sum(priorities)

    green_times = []

    for priority in priorities:

        if total_priority == 0:
            green_time = MIN_GREEN

        else:
            green_time = (
                priority /
                total_priority
            ) * 60

        green_time = max(
            MIN_GREEN,
            min(MAX_GREEN, green_time)
        )

        green_times.append(green_time)

    return green_times


def update_waiting_counter(cycle):

    served_index = cycle[0][2]

    for i in range(len(waiting_counter)):

        if i == served_index:
            waiting_counter[i] = 0

        else:
            waiting_counter[i] += 10


def print_cycle(
        cycle,
        green_times,
        priorities):

    print("\n===== COMPLETE SIGNAL CYCLE =====")

    for rank, item in enumerate(cycle, start=1):

        direction = item[0]
        index = item[2]

        print(
            f"{rank}. "
            f"{direction} | "
            f"Priority={priorities[index]:.2f} | "
            f"Green Time={green_times[index]:.2f}s"
        )

    print("\nSignal Order:")

    order = " -> ".join(
        [item[0] for item in cycle]
    )

    print(order)


def main():

    global CYCLE_NUMBER

    while True:

        print(
            f"\n\n========== CYCLE {CYCLE_NUMBER} =========="
        )

        vehicles = get_vehicle_counts()

        densities = calculate_density(
            vehicles
        )

        priorities = calculate_priority(
            vehicles,
            densities,
            waiting_counter
        )

        cycle = generate_cycle(
            priorities
        )

        green_times = allocate_green_times(
            priorities
        )

        print("\n===== TRAFFIC REPORT =====")

        for i in range(len(directions)):

            print(
                f"{directions[i]} | "
                f"Vehicles={vehicles[i]} | "
                f"Density={densities[i]:.2f} | "
                f"Waiting={waiting_counter[i]} | "
                f"Priority={priorities[i]:.2f}"
            )

        print_cycle(
            cycle,
            green_times,
            priorities
        )

        update_waiting_counter(
            cycle
        )

        CYCLE_NUMBER += 1

        choice = input(
            "\nGenerate next cycle? (y/n): "
        )

        if choice.lower() != "y":
            break


if __name__ == "__main__":
    main()
