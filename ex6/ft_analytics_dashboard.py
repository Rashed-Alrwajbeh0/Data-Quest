print("=== Game Analytics Dashboard ===\n")
print("=== List Comprehension Examples ===")
players = ['alice', 'bob', 'charlie', 'diana']
scores = [2300, 1800, 2150, 2050]
active = ['alice', 'bob', 'charlie']
achievements = ["first_kill", "level_10", "boss_slayer", "collector",
                "speed_demon", "treasure_hunter", "perfectionist"]
regions = ['north', 'east', 'north', 'central', 'east']
print("High scorers (>2000): "
      f"{[players[i] for i in [0, 1, 2, 3] if scores[i] > 2000]}")
print(f"Scores doubled: {[i * 2 for i in scores]}")
print(f"Active players: {[i for i in active]}")
print("\n=== Dict Comprehension Examples ===")
player_scores = {players[i]: scores[i] for i in [0, 1, 2, 3]}
print(f"Player scores: {player_scores}")
score_categories = {
        "high": len([i for i in scores if i > 2000]),
        "medium": len([i for i in scores if 2000 <= i <= 2200]),
        "low": len([i for i in scores if i < 2000])
}
print(f"Score categories: {score_categories}")
alice_ach = {'first_kill', 'level_10', 'boss_slayer',
             'treasure_hunter', 'speed_demon'}
bob_ach = {'first_kill', 'level_10', 'collector'}
charlie_ach = {'level_10', 'treasure_hunter', 'first_kill', 'collector',
               'boss_slayer', 'speed_demon', 'perfectionist'}
ach_dict = {'alice': alice_ach, 'bob': bob_ach, 'charlie': charlie_ach}
achievement_counts = {p: len(ach_dict[p]) for p in ach_dict}
print(f"Achievement counts: {achievement_counts}")
print("\n=== Set Comprehension Examples ===")
some_achievements = ["first_kill", "level_10", "boss_slayer"]
Unique_achievements = {a for a in some_achievements}
regions = ['north', 'east', 'central']
Active_regions = {region for region in regions}
Unique_players = {p for p in players}
print(f"Unique players: {Unique_players}")
print(f"Unique achievements: {Unique_achievements}")
print(f"Active regions: {Active_regions}")
print("\n=== Combined Analysis ===")
print(f"Total players: {len(Unique_players)}")
print(f"Total unique achievements: {len(Unique_achievements)}")
print(f"Average score: {sum(scores)/len(scores):.1f}")
top = max(scores)
top2 = ""
for i in [0, 1, 2, 3]:
    if scores[i] == top:
        top2 = players[i]
        break
print(f"Top performer: {top2} ({top} points, {len(alice_ach)} achievements)")
