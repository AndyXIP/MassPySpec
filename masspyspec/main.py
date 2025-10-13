from plotter import graph
from masspyspec.utils import mass, intensity, fragment_calc
from parser import access_file

from config.constants import ATOMIC_MASSES, MAX_CARBON_ATOMS, MIN_DBE


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