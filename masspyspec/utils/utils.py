def relative(array):
    """
    Convert absolute intensities to relative intensities.

    Args:
        array: List of absolute intensity values
    Returns:
        List of relative intensities (0-100%) rounded to 2 decimal places
    """
    y = []
    for i in array:
        z = i * 100 / max(array)
        y.append(round(z, 2))
    return y


def intensity(array):
    """
    Determine the M+ peak intensity by comparing peak intensities.

    Args:
        array: List of relative intensity values
    Returns:
        The intensity value of the molecular ion peak
    """
    length = len(array)
    if array[length - 2] < array[length - 3]:
        return array[length - 3]
    elif array[length - 1] < 20:
        return array[length - 2]
    else:
        return array[length - 1]


def mass(array, intensity):
    """
    Find the mass/charge (m/z) value corresponding to the M+ peak intensity.

    Args:
        array: List of intensity values
        intensity: The intensity value to find the corresponding mass for
    Returns:
        The index position of the specified intensity value
    """
    for i in range(len(array)):
        if array[i] == intensity:
            x = i
            break
        else:
            continue
    return x