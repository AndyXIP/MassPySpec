import os
from masspyspec.utils import relative

def access_file(filename):
    mypath = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(mypath, filename)
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