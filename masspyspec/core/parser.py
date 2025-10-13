import os
from ..utils.utils import relative

def access_file(filename):
    """
    Access and read a JCAMP-DX file, returning mass and relative intensity data.

    Args:
        filename: Name of the JCAMP-DX file (with or without .jdx extension)
    Returns:
        Tuple of two lists: (masses, relative intensities)
    """
    if not filename.endswith('.jdx'):
        filename += '.jdx'

    mypath = os.path.dirname(os.path.abspath(__file__))

    # Go up two directories (to project root) and into data/
    data_dir = os.path.abspath(os.path.join(mypath, '..', '..', 'data'))
    filepath = os.path.join(data_dir, filename)

    # finding current directory and desired file location within that directory
    x_values = []
    y_values = []


    with open(filepath, 'r') as f: # opening file with while will also close it automatically at the end
        for line in f:
            if line[0].isnumeric(): # copies desired data by detecting if the first character is numeric
                spec = line.split() # splits at " " and removes \n
                length = len(spec)
                for i in range(length):
                    x, y = spec[i].split(",")
                    x_values.append(int(x))
                    y_values.append(int(y))
                    # separates x and y values into two arrays

    y_relative = relative(y_values) # converts raw y data into relative values
    return x_values, y_relative