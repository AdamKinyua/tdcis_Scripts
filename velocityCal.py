import sys

def velocity(distance, time):
    angstrom_to_meter = 1e-10
    atomic_time_to_second = 2.418884326505e-17
    distance_in_meters = distance * angstrom_to_meter
    time_in_seconds = time * atomic_time_to_second
    velocity_in_m_per_s = distance_in_meters / time_in_seconds
    print(f"{velocity_in_m_per_s:.2e} m/s in z direction")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Correct syntax: $ python3 velocityCal.py <distance> <time>")
        sys.exit(1)
    else:
        distance = float(sys.argv[1])
        time = float(sys.argv[2])
        velocity(distance, time)


