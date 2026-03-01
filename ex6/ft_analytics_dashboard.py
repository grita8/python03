data = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5,
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2,
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7,
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4,
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7,
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements_count": 1,
        },
    },
    "sessions": [
        {
            "player": "bob",
            "duration_minutes": 94,
            "score": 1831,
            "mode": "competitive",
            "completed": True,
            "region": "north",
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "score": 1478,
            "mode": "casual",
            "completed": True,
            "region": "west",
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "mode": "competitive",
            "completed": False,
            "region": "east",
        },
        {
            "player": "alice",
            "duration_minutes": 98,
            "score": 1981,
            "mode": "ranked",
            "completed": True,
            "region": "west",
        },
        {
            "player": "diana",
            "duration_minutes": 15,
            "score": 2361,
            "mode": "competitive",
            "completed": True,
            "region": "east",
        },
        {
            "player": "eve",
            "duration_minutes": 29,
            "score": 2985,
            "mode": "casual",
            "completed": True,
            "region": "west",
        },
        {
            "player": "alice",
            "duration_minutes": 53,
            "score": 1238,
            "mode": "competitive",
            "completed": False,
            "region": "central",
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 155,
            "mode": "casual",
            "completed": False,
            "region": "central",
        },
        {
            "player": "eve",
            "duration_minutes": 117,
            "score": 188,
            "mode": "casual",
            "completed": False,
            "region": "north",
        },
        {
            "player": "alice",
            "duration_minutes": 42,
            "score": 1880,
            "mode": "casual",
            "completed": True,
            "region": "central",
        },
        {
            "player": "charlie",
            "duration_minutes": 117,
            "score": 1059,
            "mode": "casual",
            "completed": True,
            "region": "west",
        },
    ],
    "game_modes": ["casual", "competitive", "ranked"],
    "achievements": [
        "first_kill",
        "level_10",
        "boss_slayer",
    ],
}


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    high_score_players = [
        s["player"]
        for s in data["sessions"]
        if s["score"] > 2000
        ]
    score_doubled = [s["score"] * 2 for s in data["sessions"]]
    active_players = [
        s["player"]
        for s in data["sessions"]
        if not s["completed"]
        ]
    total_players = 0
    print(f"High scorers (>2000): {high_score_players}")
    print(f"Scores doubled: {score_doubled}")
    print(f"Active players: {active_players}\n")
    print("=== Dict Comprehension Examples ===")

    active_regions = set()
    player_score_dict = {s["player"]: s["score"] for s in data["sessions"]}
    player_achievement_dict = {
        p: info["achievements_count"] for p, info in data["players"].items()
    }
    categorie = {'high': 0, 'medium': 0, 'low': 0}
    for s in data['sessions']:
        score = s['score']
        if score >= 2000:
            categorie['high'] += 1
        elif score >= 1000:
            categorie['medium'] += 1
        else:
            categorie["low"] += 1
    print(f"Player scores: {player_score_dict}")
    print(f"Score categories: {categorie}")
    print(f"Achievement counts: {player_achievement_dict}\n")
    unique_players = {p for p in data["players"]}
    unique_achievements = {a for a in data["achievements"]}
    active_regions = {
        s["region"]
        for s in data["sessions"]
        if not s["completed"]
        }
    total_players = len(unique_players)

    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}\n")
    print("=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: "
          f"{sum(player_achievement_dict.values())}")
    average_score = sum(player_score_dict.values()) / len(player_score_dict)
    print(f"Average score: {average_score}")
    top_player = max(player_score_dict, key=player_score_dict.get)
    top_score = player_score_dict[top_player]
    top_achievements = player_achievement_dict[top_player]
    print(
        f"Top performer: {top_player} ({top_score} points, "
        f"{top_achievements} achievements)"
    )


main()
