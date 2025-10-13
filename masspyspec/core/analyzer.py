def print_possible_formulas(hydrocarbon, oMolecule, nMolecule, onMolecule): 
    """ 
    Print possible molecular formulas categorized by type. 
 
    Args: 
        hydrocarbon: List of hydrocarbon formulas (C, H only). 
        oMolecule: List of oxygen-containing formulas (C, H, O). 
        nMolecule: List of nitrogen-containing formulas (C, H, N). 
        onMolecule: List of formulas containing both oxygen and nitrogen (C, H, O, N). 
    """ 
    if hydrocarbon: 
        print("It can be a hydrocarbon: ") 
        for formula in hydrocarbon: 
            print(f"  • {formula}") 
    if oMolecule: 
        print("It can contain oxygen: ") 
        for formula in oMolecule: 
            print(f"  • {formula}") 
    if nMolecule: 
        print("It can contain nitrogen: ") 
        for formula in nMolecule: 
            print(f"  • {formula}") 
    if onMolecule: 
        print("It can contain both oxygen and nitrogen: ") 
        for formula in onMolecule: 
            print(f"  • {formula}")