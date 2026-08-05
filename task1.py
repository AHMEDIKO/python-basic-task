import random

def open_door_nexus():
    posture = random.choice(["sitting", "standing"])
    direction = random.choice(["left", "right", "facing"])
    distance = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(f"Start State -> Posture: {posture}, Direction: {direction}, Distance: {distance}")
    if posture == "sitting":
        print("stands up.")
    if direction == "left" or direction == "right":
        print("turns towards the door.")
    while distance > 0:
        print(f"Moving {distance} steps left")
        distance -= 1
    print("reached the door and opened it!")

open_door_nexus()