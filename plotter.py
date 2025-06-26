import matplotlib.pyplot as plt

def graph(x, y):
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_title("Mass Spectra")
    ax.set_ylabel("Relative Intensity")
    ax.set_xlabel("m/z")
    # creating graph, axes and titles

    plt.show()