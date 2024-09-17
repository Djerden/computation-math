def validate_coordinate(coordinate_input_data):
    if 3 <= len(coordinate_input_data) <= 12:
        return True
    else:
        return False


def validate_points_amount(amount):
    if amount > 2:
        return True
    else:
        return False

def validate_coordinates(coordinates_data):
    if len(coordinates_data[0]) == len(coordinates_data[1]):
        return True
    else:
        return False