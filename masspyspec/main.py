from .visualization.plotter import graph
from .utils.utils import mass, intensity
from .core.parser import access_file
from .core.calculator import fragment_calc
from .core.analyzer import print_possible_formulas

from .config.constants import ATOMIC_MASSES, MAX_CARBON_ATOMS, MIN_DBE


def masspyspec(file):
    """
    Main function to process the mass spectrum data from a JCAMP-DX file.
    
    Args:
        file (str): File name of the JCAMP-DX file in data/.
    """
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
    print_possible_formulas(hydrocarbon, oMolecule, nMolecule, onMolecule)
    # printing out each of the possible formulas for the calculated molecular mass only if it has a formula in that array.

    graph(x_values, y_values)
    # graphs the MS data


def main():
    """Run the masspyspec function with user input."""
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