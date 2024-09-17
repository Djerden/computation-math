def parse_point(x):
    try:
        point = float(x.strip().replace(',', '.'))
        return point
    except Exception:
        return ''


def parse_points_amount(x):
    try:
        amount = int(x.strip())
        return amount
    except Exception:
        return ''


def parse_coordinate_line(coordinate_input_line):
    try:
        coord = [float(x) for x in coordinate_input_line.strip().replace(",", ".").split(" ")]
        return coord
    except Exception:
        return []

