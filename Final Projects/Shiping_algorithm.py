Items = int(input("\n\n\nPlease enter the total number of items: "))

Big_box = (Items - (Items % 10)) / 10
Big_box = int(Big_box)
print("\nTotal big boxes: ",Big_box)

Items_remaining = Items - (Big_box * 10)

Medium_box = (Items_remaining - (Items_remaining % 5)) / 5
Medium_box = int(Medium_box)
print("Total medium boxes: ",Medium_box)

Items_remaining = Items_remaining - (Medium_box * 5)

Small_box = (Items_remaining - (Items_remaining % 1)) / 1
Small_box = int(Small_box)
print("Total small boxes: ",Small_box)