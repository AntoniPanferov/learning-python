def rucksack_greedy_whole_items(values, weights, capacity):
    # Berechne das Wert-Gewicht-Verhältnis für jedes Item
    ratio = [v / w for v, w in zip(values, weights)]

    # Erstelle eine Liste von Tupeln (ratio, value, weight, index)
    items = list(zip(ratio, names,values, weights, range(len(values))))

    # Sortiere die Items absteigend nach dem Wert-Gewicht-Verhältnis
    items.sort(reverse=True)
    print(items)
    total_value = 0
    total_weight = 0
    selected_items = []

    for r, n, v, w, i in items:
        if total_weight + w <= capacity:
            # Füge das komplette Item hinzu, wenn es in den Rucksack passt
            selected_items.append(n)
            total_value += v
            total_weight += w

    return total_value, total_weight, selected_items
'''
# Beispiel 1

weights = [30, 20, 15]
values = [3000, 2000, 1500]
names = ["Stereoanlage", "Laptop", "Gitarre"]
capacity = 35

'''
# Beispiel 2

weights = [50, 2, 200, 1, 100, 3]
values = [500, 300, 700, 4000, 300, 1000]
names = ["Fernseher", "Kerzenständer", "Kühlschrank", "Halskette", "Bücher", "Laptop"]
capacity = 75


max_value, total_weight, selected = rucksack_greedy_whole_items(values, weights, capacity)

print(f"Maximaler Wert: {max_value}")
print(f"Gesamtgewicht: {total_weight}")
print("Ausgewählte Items:")
for item in selected:
    print(f"  Item {item}")