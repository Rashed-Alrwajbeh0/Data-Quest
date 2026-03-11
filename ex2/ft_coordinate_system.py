from math import sqrt


def calculate_distance(point1: tuple, point2: tuple) -> float:
    return sqrt((point2[0] - point1[0])**2 +
                (point2[1] - point1[1])**2 +
                (point2[2] - point1[2])**2)


def pars(point: str) -> tuple:
    x, y, z = point.split(',')
    return (int(x), int(y), int(z))


print("=== Game Coordinate System ===\n")
point = (10, 20, 5)
print(f"Position created: {point}")
print(f"Distance between (0, 0, 0) and {point}:"
      f" {calculate_distance((0, 0, 0), point):.2f}")
point = "3,4,0"
print(f"\nParsing coordinates: \"{point}\"")
pointt = pars(point)
print(f"Parsed position: {pointt}")
print(f"Distance between (0, 0, 0) and {pointt}:"
      f" {calculate_distance((0, 0, 0), pointt):.1f}")
try:
    point2 = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{point2}\"")
    pars(point2)
except ValueError as e:
    print(f"Error parsing coordinates: {e}")
    print(f"Error details - Type: ValueError, Args: (\"{e}\",)")
print("\nUnpacking demonstration:")
print(f"Player at x={pointt[0]}, y={pointt[1]}, z={pointt[2]}")
print(f"Coordinates: X={pointt[0]}, Y={pointt[1]}, z={pointt[2]}")
