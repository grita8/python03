def find_rare_achievements(data: dict[str, list[str]]) -> set[str]:
    """Find achievements that appear in exactly 1 player's set"""
    achiev_count: dict[str, int] = {}

    for achievements in data.values():
        player_set = set(achievements)
        for achievement in player_set:
            achiev_count[achievement] = achiev_count.get(achievement, 0) + 1

    rare = {achiev for achiev, count in achiev_count.items() if count == 1}
    return rare


def for_two(data: dict[str, list[str]], p1: list[str], p2: list[str]):
    """Compare achievements between two players"""
    set1 = set(data[p1])
    set2 = set(data[p2])

    common = set1.intersection(set2)
    unique1 = set1.difference(set2)
    unique2 = set2.difference(set1)

    print(f"{p1.capitalize()} vs {p2.capitalize()} common: {common}")
    print(f"{p1.capitalize()} unique: {unique1}")
    print(f"{p2.capitalize()} unique: {unique2}")


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    data = {
        "alice": [
            "first_kill",
            "level_10",
            "treasure_hunter",
            "speed_demon",
            "first_kill",
            "first_kill",
        ],
        "bob": [
            "level_10",
            "boss_slayer",
            "collector",
            "first_kill",
            "level_10",
            "level_10",
        ],
        "charlie": [
            "treasure_hunter",
            "boss_slayer",
            "level_10",
            "speed_demon",
            "boss_slayer",
            "speed_demon",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
        ],
    }
    alice_set = set(data["alice"])
    bob_set = set(data["bob"])
    charlie_set = set(data["charlie"])
    print(f"Player alice achievements: {alice_set}")
    print(f"Player bob achievements: {bob_set}")
    print(f"Player charlie achievements: {charlie_set}\n")
    print("=== Achievement Analytics ===")
    all_unique = alice_set.union(bob_set, charlie_set)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}\n")
    common_to_all = alice_set.intersection(bob_set, charlie_set)
    print(f"Common to all players: {common_to_all}")
    rare = find_rare_achievements(data)
    print(f"Rare achievements (1 player): {rare}\n")
    for_two(data, "alice", "bob")


main()
