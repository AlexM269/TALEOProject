import csv

vectors = [["abeille : 8", "rouge : 2",  "carré : 2"], ["arbre : 6", "blanc : 2", "grand : 4"], ["manger : 4", "plat : 6", "courir : 4"]]
indice = 0

with open('vectors.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for vector in vectors:
        indice = indice + 1
        case = ['doc : '+str(indice)]
        writer.writerow(case + vector)
