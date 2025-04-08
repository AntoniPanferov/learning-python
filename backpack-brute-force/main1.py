def knapsack_brute_force(weights, values, names, capacity, n, current_selection=[]):
    print("Aufruf mit foldenden Parametern:")
    print("knappsack_brute_force(",weights,values,names,"cap:",capacity,"n=",n,current_selection,")")
    if n == 0 or capacity == 0:
        return 0, current_selection
    #Wenn das Gewicht des aktuellen Gegenstandes das Gesamtgewicht uebersteigt,
    #dann kann er nicht in den Rucksack gelegt werden
    if weights[n - 1] > capacity:
        return knapsack_brute_force(weights, values, names, capacity, n - 1, current_selection)

    # Option 1: Den aktuellen Gegenstand einpacken
    value_with, selection_with = knapsack_brute_force(
        weights, values, names, capacity - weights[n - 1], n - 1,
                                current_selection + [names[n - 1]]
    )
    value_with += values[n - 1]

    # Option 2: Den aktuellen Gegenstand nicht einpacken
    value_without, selection_without = knapsack_brute_force(
        weights, values, names, capacity, n - 1, current_selection
    )

    if value_with > value_without:
        return value_with, selection_with
    else:
        return value_without, selection_without


'''
# Beispielaufruf
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


n = len(weights)

max_value, selected_items = knapsack_brute_force(weights, values, names, capacity, n)

print(f"Maximaler Wert im Rucksack: {max_value}")
print(f"Anzahl der ausgewählten Gegenstände: {len(selected_items)}")
print("Ausgewählte Gegenstände:")
#for item in selected_items:
 #   print(f"- {item}")
print(selected_items)
