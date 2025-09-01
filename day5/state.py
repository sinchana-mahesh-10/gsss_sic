import sys

# Step 1: Define lists inside the program
states = ["Karnataka", "Maharashtra", "Tamil Nadu", "Kerala"]
capitals = ["Bengaluru", "Mumbai", "Chennai", "Thiruvananthapuram"]

# Step 2: Print header
print("State                | Capital")
print("----------------------------------------")

# Step 3: Print using loop (without zip, using index)
for i in range(len(states)):
    print(f"{states[i]:20} | {capitals[i]}")