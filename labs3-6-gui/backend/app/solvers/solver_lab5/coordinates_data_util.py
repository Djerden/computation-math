def sort_coordinates(coordinates_data):
    tt = []
    for i in range(len(coordinates_data[0])):
        tt.append([coordinates_data[0][i], coordinates_data[1][i]])
    coordinates_data = [[], []]
    for i in sorted(tt):
        coordinates_data[0].append(i[0])
        coordinates_data[1].append(i[1])
    return coordinates_data