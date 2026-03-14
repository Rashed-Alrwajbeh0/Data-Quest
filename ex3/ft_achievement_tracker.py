print("=== Achievement Tracker System ===\n")
alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
bob = {"first_kill", "level_10", "boss_slayer", "collector"}
charlie = {"level_10", "treasure_hunter",
           "boss_slayer", "speed_demon", "perfectionist"}
print(f"Player alice achievements: {alice}\n"
      f"Player bob achievements: {bob}\n"
      f"Player charlie achievements: {charlie}\n")
print("=== Achievement Analytics ===")
set1 = bob.union(alice, charlie)
print(f"All unique achievements: {set1}")
print(f"Total unique achievements: {len(set1)}\n")
set2 = alice.intersection(bob, charlie)
print(f"Common to all players: {set2}")
alice_rare = alice.difference(bob, charlie)
bob_rare = bob.difference(alice, charlie)
charlie_rare = charlie.difference(alice, bob)
rare = alice_rare.union(bob_rare, charlie_rare)
print(f"Rare achievements (1 player): {rare}\n")
print(f"Alice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")
