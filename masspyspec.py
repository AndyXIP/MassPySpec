import matplotlib.pyplot as plt
import os


def masspyspec(file):
    x_values, y_values = access_file(file)
    # access and convert JCAMP-DX data to obtain x and y values

    M_intensity = intensity(y_values)
    x_M = mass(y_values, M_intensity)
    M_mass = x_values[x_M]
    '''
    calculate the M+ peak
    find the position of the x value for the most intense M+ peak
    calculate mass of the molecule by finding the x value of M+ peak 
    '''
    hydrocarbon, oMolecule, nMolecule, onMolecule = fragment_calc(M_mass)
    # obtaining possible chemical formulas for different types of molecules
    
    print(f"This molecule has an atomic mass of {M_mass} amu. This means that it can have the following chemical formulas:")
    if len(hydrocarbon) >= 1:
        print("It can be a hydrocarbon: ")
        for i in hydrocarbon:
            print(i)
    if len(oMolecule) >= 1:
        print(f"It can contain oxygen: ")
        for i in oMolecule:
            print(i)
    if len(nMolecule) >= 1:
        print(f"It can contain nitrogen: ")
        for i in nMolecule:
            print(i)
    if len(onMolecule) >= 1:
        print(f"It can contain both oxygen and nitrogen: ")
        for i in onMolecule:
            print(i)
    # printing out each of the possible formulas for the calculated molecular mass only if it has a formula in that array.

    graph(x_values, y_values)
    # graphs the MS data

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


def relative(array):
    y = []
    for i in array:
        z = i * 100 / max(array)
        y.append(round(z, 2))
    return y
# converts each y value into relative y values, relative to the largest y value

def graph(x, y):
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_title("Mass Spectra")
    ax.set_ylabel("Relative Intensity")
    ax.set_xlabel("m/z")
    # creating graph, axes and titles

    plt.show()


def intensity(array):
    length = len(array)
    if array[length - 2] < array[length - 3]:
        return array[length - 3]
    elif array[length - 1] < 20:
        return array[length - 2]
    else:
        return array[length - 1]
# determine the M+ peak through comparing intensities

def mass(array, intensity):
    for i in range(len(array)):
        if array[i] == intensity:
            x = i
            break
        else:
            continue
    return x
# calculates the possition of the x value of the M+ peak

def fragment_calc(mass):
    possiblehc_formulas = []
    possibleO_formulas = []
    possibleN_formulas = []
    possibleON_formulas = []
    C = int(mass / 12)
    for i in range(1, C + 1):
        C = i
        max_H = 2 * C + 2
        # limit to help create more realistic formulas and determine number of hydrogens.
        tmass = mass - C * 12
        O = int(tmass / 16)
        for i in range(0, O + 1):
            O = i
            tmass = mass - C * 12 - O * 16
            N = int(tmass / 14)
            for i in range(0, N + 1):
                N = i
                max_H += N
                H = tmass - N * 14
                total_mass = 12 * C + 16 * O + 14 * N + H
                DBE = C - (H / 2) + (N / 2) + 1
                # calculate double bond equivalence
                if 0 <= H <= max_H and total_mass == mass and DBE % 1 == 0 and DBE >= 0:
                    atoms = [C, H, O, N]
                    new_atoms = []
                    for atom in atoms:
                        if atom == 1:
                            new_atoms.append("")
                        else:
                            new_atoms.append(atom)
                    C_, H_, O_, N_ = new_atoms[0], new_atoms[1], new_atoms[2], new_atoms[3]
                    if N == 0 and O == 0:
                        possiblehc_formulas.append(f"C{C_}H{H_}, DBE = {DBE:.0f}")
                    elif N == 0 and O != 0:
                        possibleO_formulas.append(f"C{C_}H{H_}O{O_}, DBE = {DBE:.0f}")
                    elif N != 0 and O == 0:
                        possibleN_formulas.append(f"C{C_}H{H_}N{N_}, DBE = {DBE:.0f}")
                    elif N != 0 and O != 0:
                        possibleON_formulas.append(f"C{C_}H{H_}O{O_}N{N_}, DBE = {DBE:.0f}")
    return possiblehc_formulas, possibleO_formulas, possibleN_formulas, possibleON_formulas


def main():
    try:
        x = input("Enter file name: ").strip()
        masspyspec(x)
    except FileNotFoundError:
        print("File Missing. Please ensure the file is in the correct directory and that you have entered the correct file name.")
        # error occurs when no file is found with that name
    except:
        print("Something went wrong, please try entering the file name again and ensure the file is in JCAMP-DX format.")
        # printed when any other error appears


if __name__ == "__main__":
    main()
# executes the function when running the file