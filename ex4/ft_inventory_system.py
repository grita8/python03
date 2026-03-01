import sys

inventory = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 1,
                "quantum_ring": 3,
            },
            "total_value": 1875,
            "item_count": 6,
        },
        "bob": {
            "items": {"code_bow": 3, "pixel_sword": 2},
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {"pixel_sword": 1, "code_bow": 1},
            "total_value": 350,
            "item_count": 2,
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3,
            },
            "total_value": 4125,
            "item_count": 12,
        },
    },
    "catalog": {
        "pixel_sword": {"type": "weapon", "value": 150, "rarity": "common"},
        "quantum_ring": {"type": "accessory", "value": 500, "rarity": "rare"},
        "health_byte": {"type": "consumable", "value": 25, "rarity": "common"},
        "data_crystal": {
            "type": "material",
            "value": 1000,
            "rarity": "legendary"
        },
        "code_bow": {"type": "weapon", "value": 200, "rarity": "uncommon"},
    },
}


def main() -> None:
    print("=== inventory System Analysis ===")
    argc = len(sys.argv)
    player_inv = {}
    total = 0
    if argc == 1:
        print("No arguments provided! Using default data...\n")
        player_inv = (
            inventory.get("players", {})
            .get("alice", {})
            .get("items", {})
        )
        total = sum(player_inv.values())
    else:
        args = sys.argv[1:]
        try:
            for arg in args:
                list_inv = arg.split(":")
                key = list_inv[0]
                value = int(list_inv[1])
                player_inv.update({key: value})
                total += int(value)
        except Exception:
            print("Error wrong arguments format!: "
                  "(must be item_name:item_count)")
            return
    print(f"Total items in inventory: {total}")
    unique_items = set(player_inv)
    print(f"Unique item types: {len(unique_items)}\n")
    print("=== Current inventory ===")
    for key, value in player_inv.items():
        print(f"{key}: {value} units ({(((value)/total) * 100):.1f}%)")
    print()
    print("=== player_inv Statistics ===")
    max_value = max(player_inv.values())
    max_key = max(player_inv, key=player_inv.get)
    print(f"Most abundant: {max_key} ({max_value} units)")
    min_value = min(player_inv.values())
    min_key = min(player_inv, key=player_inv.get)
    print(f"Least abundant: {min_key} ({min_value} unit)\n")

    print("=== Item Categories ===")
    bottom_dict = {}
    top_dict = {}
    for key, value in player_inv.items():
        if value == max_value:
            top_dict.update({key: value})
        elif value < max_value:
            bottom_dict.update({key: value})
    print(f"Moderate: {top_dict}")
    print(f"Scarce: {bottom_dict}\n")
    print("=== Management Suggestions ===")
    restock_list = []
    for key, value in player_inv.items():
        if value < 2:
            restock_list.append(key)
    print(f"Restock needed: {restock_list}\n")
    print("=== Dictionary Properties Demo ===")
    keys_list = list(player_inv.keys())
    values_list = list(player_inv.values())
    print(f"Dictionary keys: {keys_list}")
    print(f"Dictionary values: {values_list}")
    if player_inv:
        sample_key = list(player_inv.keys())[0]
        print(
            f"Sample lookup - '{sample_key}' in player_inv: "
            "{sample_key in player_inv}"
        )


main()
