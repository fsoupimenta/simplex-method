import numpy as np

from methods.vogel import Vogel

sources_nodes = {
    0: 'Casa Verde',
    1: 'Grajaú',
    2: 'Ipiranga',
    3: 'Itaquera',
    4: 'Mooca',
    5: 'Pinheiros'}
destiny_nodes = {
    0: "Alto de Pinheiros",
    1: "Anhanguera",
    2: "Aricanduva",
    3: "Bela Vista",
    4: "Bom Retiro",
    5: "Brasilândia",
    6: "Cambuci",
    7: "Capão Redondo",
    8: "Freguesia do Ó",
    9: "Iguatemi",
    10: "Itaim Bibi",
    11: "Jabaquara",
    12: "Liberdade",
    13: "Morumbi",
    14: "Moema",
    15: "Perdizes",
    16: "Perus",
    17: "Santa Cecília",
    18: "Santo Amaro",
    19: "Santo Amaro",
    20: "Tatuapé",
    21: "Tremembé",
    22: "Tucuruvi",
    23: "Vila Mariana",
    24: "Vila Matilde"
}

availability = [5147, 3053, 5900, 5044, 6149, 4312]
demands = [1297, 656, 1124, 837, 1445, 1495, 1981, 1440, 1228, 719, 1023, 763, 221, 628, 188, 1119, 1556, 1411, 1017,
           1467, 1424, 2396, 913, 1303, 976, None]

original_matrix = [
    [11.27, 58.40, 8.74, 53.58, 58.10, 27.65],
    [16.33, 11.55, 51.25, 54.46, 28.39, 16.57],
    [31.25, 11.69, 38.41, 21.82, 38.65, 38.97],
    [24.33, 29.98, 8.75, 58.13, 2.10, 19.14],
    [21.08, 14.28, 42.77, 26.05, 9.33, 19.06],
    [9.74, 28.57, 18.68, 16.43, 17.28, 25.09],
    [13.18, 55.43, 18.67, 9.95, 0.98, 28.65],
    [41.86, 37.28, 31.99, 41.04, 3.52, 4.71],
    [43.02, 20.44, 36.43, 46.77, 1.94, 51.38],
    [31.80, 33.49, 49.50, 23.83, 4.25, 35.79],
    [38.70, 38.18, 2.98, 7.49, 20.57, 0.94],
    [20.26, 24.97, 30.53, 0.88, 38.09, 51.28],
    [44.61, 34.84, 36.92, 11.74, 16.60, 56.34],
    [34.71, 40.53, 15.59, 8.62, 38.27, 40.41],
    [39.26, 34.96, 51.84, 40.16, 24.25, 6.89],
    [14.89, 44.99, 34.23, 31.66, 15.59, 0.39],
    [10.27, 16.57, 48.56, 29.36, 51.14, 5.43],
    [50.90, 6.92, 31.88, 49.68, 38.20, 38.73],
    [55.79, 46.34, 9.19, 29.52, 35.89, 30.00],
    [42.73, 34.32, 34.74, 4.67, 21.09, 5.48],
    [49.58, 27.39, 22.15, 17.81, 15.37, 42.16],
    [33.51, 33.08, 17.19, 25.13, 20.17, 16.77],
    [19.29, 38.05, 32.07, 45.24, 12.53, 9.39],
    [22.99, 53.46, 27.48, 42.37, 11.52, 36.70],
    [25.73, 45.88, 12.20, 18.87, 3.07, 36.46]
]


def create_matrix():
    matrix = list(map(list, zip(*original_matrix)))

    for i, row in enumerate(matrix):
        row.append(availability[i])

    matrix.append(demands)
    matrix = np.array(matrix).astype(float)

    return matrix


matrix = [
    [2, 3, 11, 7, 6],
    [1, 0, 6, 1, 1],
    [5, 8, 15, 9, 10],
    [7, 5, 3, 2, 0]
]

vogel = Vogel(np.array(matrix).astype(float))
vogel.calculate_penalty()
