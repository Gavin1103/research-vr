from db import get_positions_by_id
from users import users
from math import sqrt

def total_movement(positions):
    total = 0
    for i in range(1, len(positions)):
        p1 = positions[i - 1]
        p2 = positions[i]
        distance = sqrt(
            (p2['x'] - p1['x'])**2 +
            (p2['y'] - p1['y'])**2 +
            (p2['z'] - p1['z'])**2
        )
        total += distance
    return total

# Resultaten verzamelen
for user in users:
    naam = user["name"]
    positions_with = get_positions_by_id(user["test_with_controller_id"])
    positions_without = get_positions_by_id(user["test_without_controller_id"])

    if not positions_with or not positions_without:
        print(f"⚠️ Data ontbreekt voor {naam}")
        continue

    movement_with = total_movement(positions_with)
    movement_without = total_movement(positions_without)
    difference = movement_without - movement_with

    print(f"\n📊 Resultaat voor {naam}:")
    print(f"  Met controller    : {movement_with:.5f}")
    print(f"  Zonder controller : {movement_without:.5f}")
    print(f"  Verschil          : {difference:+.5f}")
    print(f"  Voorkeur          : {user['preference']}")

