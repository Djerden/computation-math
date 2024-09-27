def parse_value(x):
    try:
        value = float(x.strip().replace(',', '.'))
        return value
    except Exception:
        return ''


def parse_h(x):
    try:
        h = int(x.strip().replace(',', '.'))
        return h
    except Exception:
        return ''


def parse_coordinate_line(coordinate_input_line):
    try:
        coord = [float(x) for x in coordinate_input_line.strip().replace(",", ".").split(" ")]
        return coord
    except Exception:
        return []

