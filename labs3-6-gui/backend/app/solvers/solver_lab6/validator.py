def validate_eps(eps):
    if 1 >= eps >= 0.000000001:
        return True
    else:
        return False