# MassPySpec

## Description
MassPySpec is a Python package designed for the analysis and visualization of Mass Spectrometry (MS) data. This tool aims to simplify the process of MS data processing, by directly converting MS data into possible chemical formulas for molecules.

## Installation
MassPySpec requires Python 3.12.0 or newer. You can install it directly from https://www.python.org/downloads/


The project file only needs to be downloaded and no installation commands are required. Make sure you add your MS data to the same directory.


## Dependencies
- matplotlib 3.8.0 or newer

This can be installed using pip by typing the following in a terminal window:

```
pip install matplotlib
```

## Usage
To get started with MassPySpec, load your MS data in JCAMP-DX format into the data folder qnd then run the following script:

```
python -m masspyspec.main
```

You will then be prompted to enter your filename:

```
Enter file name: [Filename]
```

### Examples
Using the data already in the directory:

```
python -m masspyspec.main
Enter file name: benzene
```
