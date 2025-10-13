import matplotlib.pyplot as plt

def graph(x, y):
    """
    Plot the mass spectra.
    
    Args:
        x: List of mass/charge (m/z) values
        y: List of relative intensity values
    """
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_title("Mass Spectra")
    ax.set_ylabel("Relative Intensity")
    ax.set_xlabel("m/z")
    # creating graph, axes and titles

    plt.show()