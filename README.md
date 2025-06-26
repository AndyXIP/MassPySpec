# MassPySpec

## Description
MassPySpec is a Python package designed for the analysis and visualization of Mass Spectrometry (MS) data. This tool aims to simplify the process of MS data processing, by directly converting MS data into possible chemical formulas for molecules.

## Installation
MassPySpec requires Python 3.12.0 or newer. You can install it directly from https://www.python.org/downloads/


The project file only needs to be downloaded and no installation commands are required. Make sure you add your MS data to the same directory.


## Dependencies
- matplotlib 3.8.0 or newer

This can be installed using pip by typing the following in a terminal window:<br/>
pip install matplotlib


## Usage
To get started with MassPySpec, import the package and load your MS data in JCAMP-DX format into the data folder in the same directory as the program:

from masspyspec import main<br/>
main.main()

You will then be prompted to enter your filename:

Enter file name: [Filename]

### Examples
Using the data already in the directory:

import masspyspec as ms<br/>
ms.main()<br/>
Enter file name: data/benzene.jdx
