waste_item = input ("Enter the waste item:")

if waste_item == "banana peel":
    print("Category: Wet waste")
    print("Disposal: Compost Bin")
    print("Hazard Level: Low")

elif waste_item == "plastic bottle":
    print("Category: Dry waste")
    print("Disposal: Recycling Bin")
    print("Hazard Level: Medium")

elif waste_item == "battery":
    print("Category: Hazardous waste")
    print("Disposal: E-waste Centre")
    print("Hazard Level: High")

else:
    print("Waste item not found in database")