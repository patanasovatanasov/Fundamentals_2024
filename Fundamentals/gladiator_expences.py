lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_count = lost_fights_count // 2
sword_count = lost_fights_count // 3
shield_count = lost_fights_count // 6
armor_count = shield_count // 2

total_price = helmet_price * helmet_count + sword_price * sword_count + shield_price * shield_count + armor_price * armor_count

print(f"Gladiator expenses: {total_price:.2f} aureus")