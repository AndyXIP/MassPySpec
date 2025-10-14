# MassPySpec

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10%2B-11557c?logo=matplotlib&logoColor=white)

A Python package for mass spectrometry (MS) data analysis and molecular formula determination. MassPySpec processes JCAMP-DX files, identifies molecular peaks, calculates possible chemical formulas with Double Bond Equivalence (DBE), and visualizes mass spectra.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Quick Start](#quick-start)
  - [Examples](#examples)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Data Format](#data-format)
- [Dependencies](#dependencies)
- [License](#license)

---

## Overview

MassPySpec simplifies mass spectrometry data analysis by automating the process of:
1. **Parsing** JCAMP-DX format MS data files
2. **Identifying** the molecular ion peak (M⁺)
3. **Calculating** all possible molecular formulas for the detected mass
4. **Computing** Double Bond Equivalence (DBE) for structural insights
5. **Visualizing** mass spectra with matplotlib

Perfect for chemistry students, researchers, and analysts working with mass spectrometry data.

---

## Features

- **JCAMP-DX File Parsing**: Automatic extraction of mass/charge (m/z) and intensity data
- **Molecular Formula Prediction**: Generates all chemically valid formulas (C, H, O, N) for a given mass
- **DBE Calculation**: Computes Double Bond Equivalence for each formula to infer molecular structure
- **Categorized Results**: Organizes formulas by composition:
  - Hydrocarbons (C, H only)
  - Oxygen-containing molecules (C, H, O)
  - Nitrogen-containing molecules (C, H, N)
  - Mixed heteroatom molecules (C, H, O, N)
- **Visual Output**: Bar chart visualization of mass spectra
- **Sample Data Included**: Pre-loaded JCAMP-DX files (benzene, butene, methanol, octane)

---

## Installation

### Prerequisites

- **Python 3.12.0+** ([Download](https://www.python.org/downloads/))

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AndyXIP/MassPySpec.git
   cd MassPySpec
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install matplotlib directly:
   ```bash
   pip install matplotlib
   ```

---

## Usage

### Quick Start

1. **Place your JCAMP-DX file** (`.jdx` extension) in the `data/` directory
2. **Run the program**:
   ```bash
   python -m masspyspec.main
   ```
3. **Enter the filename** when prompted (without extension):
   ```
   Enter file name: [filename]
   ```

The program will:
- Parse the mass spectrum
- Identify the molecular ion peak
- Calculate possible molecular formulas
- Display results in the terminal
- Show a bar chart of the mass spectrum

### Examples

#### Using Pre-loaded Sample Data

**Benzene (C₆H₆)**:
```bash
python -m masspyspec.main
Enter file name: benzene
```

**Expected Output**:
```
This molecule has an atomic mass of 78 amu. This means that it can have the following chemical formulas:
It can be a hydrocarbon: 
  • C6H6, DBE = 4
```

**Methanol (CH₃OH)**:
```bash
python -m masspyspec.main
Enter file name: methanol
```

**Octane (C₈H₁₈)**:
```bash
python -m masspyspec.main
Enter file name: octane
```

---

## 📁 Project Structure

```
MassPySpec/
├── masspyspec/              # Main package directory
│   ├── __init__.py          # Package initialization
│   ├── main.py              # Entry point and orchestration
│   ├── config/              # Configuration and constants
│   │   ├── __init__.py
│   │   └── constants.py     # Atomic masses, thresholds, plot settings
│   ├── core/                # Core analysis modules
│   │   ├── __init__.py
│   │   ├── parser.py        # JCAMP-DX file parsing
│   │   ├── calculator.py    # Molecular formula calculation
│   │   └── analyzer.py      # Result formatting and display
│   ├── utils/               # Utility functions
│   │   ├── __init__.py
│   │   └── utils.py         # Peak detection, normalization
│   └── visualization/       # Plotting modules
│       ├── __init__.py
│       └── plotter.py       # Matplotlib visualization
├── data/                    # Sample JCAMP-DX files
│   ├── benzene.jdx
│   ├── butene.jdx
│   ├── methanol.jdx
│   └── octane.jdx
├── requirements.txt         # Python dependencies
├── LICENSE
└── README.md
```

---

## How It Works

### 1. File Parsing
The `parser.py` module reads JCAMP-DX files and extracts:
- **m/z values**: Mass-to-charge ratios
- **Intensity values**: Raw abundance data (converted to relative intensities)

### 2. Peak Identification
The `utils.py` module identifies the **molecular ion peak (M⁺)**:
- Finds the maximum intensity peak
- Retrieves the corresponding mass value

### 3. Formula Calculation
The `calculator.py` module generates all possible molecular formulas:
- Iterates through combinations of C, H, O, N atoms
- Validates formulas based on:
  - **Exact mass match**
  - **Hydrogen limits** (H ≤ 2C + 2 + N for organic molecules)
  - **Non-negative DBE** (Double Bond Equivalence)
- **DBE Formula**: `DBE = C - (H/2) + (N/2) + 1`

### 4. Result Display
The `analyzer.py` module categorizes and formats results:
- Groups formulas by heteroatom composition
- Displays DBE for structural inference
- Simplifies formula notation (e.g., "C" instead of "C1")

### 5. Visualization
The `plotter.py` module creates a bar chart:
- X-axis: m/z (mass/charge ratio)
- Y-axis: Relative intensity
- Title: "Mass Spectra"

---

## Data Format

MassPySpec accepts **JCAMP-DX** format files (`.jdx` extension).

**Expected Format**:
```
... (header metadata)
##XYDATA=(X++(Y..Y))
15,5 16,12 17,8 ...
```

- Each line contains space-separated `x,y` pairs
- `x` = m/z value (integer)
- `y` = intensity (integer, converted to relative %)

---

## 📦 Dependencies

- **matplotlib** 3.10.7+ - Data visualization
- **numpy** 2.3.3+ - Numerical operations (indirect dependency via matplotlib)

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Academic Context

- **Institution**: University College London
- **Program**: BSc Chemistry with Mathematics
- **Year**: 2021-2024
- **Module**: Programming for Chemists
- **Status**: Completed

---

## Acknowledgments

Developed as a tool to simplify mass spectrometry data analysis for chemistry students and researchers.

---

## Future Enhancements

Potential improvements for future versions:
- Support for additional file formats (mzXML, mzML)
- Isotope pattern analysis
- Fragment ion identification
- Batch processing of multiple files
- GUI interface for non-programmers
- Export results to CSV/JSON

---

**Note**: This tool assumes **electron ionization (EI)** mass spectrometry and identifies the **M⁺ molecular ion peak** as the most intense peak. For complex spectra with fragmentation patterns, manual interpretation may still be required.
