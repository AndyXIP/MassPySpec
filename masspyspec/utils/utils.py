def relative(array):
    y = []
    for i in array:
        z = i * 100 / max(array)
        y.append(round(z, 2))
    return y
# converts each y value into relative y values, relative to the largest y value

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
