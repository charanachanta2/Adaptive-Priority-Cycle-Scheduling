import APCS_algorithm


def detect_emergency_vehicle():
    """
    Temporary simulation.
    Later this will be replaced by camera detection.
    """

    emergency = input(
        "\nEmergency Vehicle Detected? (y/n): "
    ).lower()

    if emergency == "y":

        direction = input(
            "Enter Direction "
            "(North/South/East/West): "
        )

        if direction in APCS_algorithm.directions:
            return direction

    return None


def emergency_override(direction):

    print(
        f"\n🚑 Emergency Vehicle "
        f"Detected in {direction}"
    )

    direction_index = (
        APCS_algorithm.directions.index(direction)
    )

    priorities = [0, 0, 0, 0]

    priorities[direction_index] = 9999

    cycle = APCS_algorithm.generate_cycle(
        priorities
    )

    green_times = [10, 10, 10, 10]

    green_times[direction_index] = 40

    print("\n===== EMERGENCY CYCLE =====")

    for rank, item in enumerate(
        cycle,
        start=1
    ):

        index = item[2]

        print(
            f"{rank}. "
            f"{item[0]} | "
            f"Green Time="
            f"{green_times[index]}s"
        )

    print(
        f"\n✅ Immediate GREEN "
        f"for {direction}"
    )

    APCS_algorithm.waiting_counter[
        direction_index
    ] = 0


def run_controller():

    while True:

        print(
            "\n=================================="
        )
        print(
            "SMART TRAFFIC CONTROLLER"
        )
        print(
            "=================================="
        )

        emergency_direction = (
            detect_emergency_vehicle()
        )

        if emergency_direction:

            emergency_override(
                emergency_direction
            )

            continue

        vehicles = (
            APCS_algorithm.get_vehicle_counts()
        )

        densities = (
            APCS_algorithm.calculate_density(
                vehicles
            )
        )

        priorities = (
            APCS_algorithm.calculate_priority(
                vehicles,
                densities,
                APCS_algorithm.waiting_counter
            )
        )

        cycle = (
            APCS_algorithm.generate_cycle(
                priorities
            )
        )

        green_times = (
            APCS_algorithm.allocate_green_times(
                priorities
            )
        )

        print(
            "\n===== NORMAL APCS CYCLE ====="
        )

        APCS_algorithm.print_cycle(
            cycle,
            green_times,
            priorities
        )

        APCS_algorithm.update_waiting_counter(
            cycle
        )

        choice = input(
            "\nRun Next Cycle? (y/n): "
        )

        if choice.lower() != "y":
            break


if __name__ == "__main__":
    run_controller()
