def fragment_calc(mass):
    """
    Calculate possible molecular formulas for a given mass.

    Args:
        mass: Molecular mass (int)
    Returns:
        Tuple of lists containing possible formulas:
        - Hydrocarbon formulas (C, H only)
        - Oxygen-containing formulas (C, H, O)
        - Nitrogen-containing formulas (C, H, N)
        - Oxygen and nitrogen formulas (C, H, O, N)
    """
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
