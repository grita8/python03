import sys
import math


def parse_coords(s: str) -> tuple:
    """
    Takes a string like "1,2,3" and turns it into coordinates (1, 2, 3).
    """
    parts = s.split(",")
    if len(parts) != 3:
        return False

    return (int(parts[0]), int(parts[1]), int(parts[2]))


def distance(p1: tuple, p2: tuple) -> float:
    """
    Calculates the distance between two 3D points.
    """
    return math.sqrt(
        (p2[0] - p1[0]) ** 2
        + (p2[1] - p1[1]) ** 2
        + (p2[2] - p1[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===\n")
    origin = (0, 0, 0)
    data = [(10, 20, 5)]

    for value in data:
        default = value
        dist = distance(origin, default)
        print(f"Position created: {default}")
        print(f"Distance between {origin} and {default}: {dist:.2f}" + "\n")
    if len(sys.argv) > 1:
        coord_str = sys.argv[1]
    else:
        coord_str = "3,4,0"
    try:
        print(f'Parsing coordinates: "{coord_str}"')
        pos = parse_coords(coord_str)
        if not pos:
            print("ERROR! must be a 3D coordinates")
            return
        print(f"Parsed position: {pos}")
        dist = distance(origin, pos)
        print(f"Distance between {origin} and {pos}: {dist:.1f}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}\n")
        return

    try:
        print('\nParsing invalid coordinates: "abc,def,ghi"')
        parse_coords("abc,def,ghi")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")

    print("\n" + "Unpacking demonstration:")
    x, y, z = pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


main()
