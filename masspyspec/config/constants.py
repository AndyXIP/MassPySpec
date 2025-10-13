"""
Constants and configuration settings for MassPySpec.
"""

# Atomic masses (in atomic mass units)
ATOMIC_MASSES: dict[str, float] = {
    'C': 12.0,
    'H': 1.0,
    'O': 16.0,
    'N': 14.0
}

# Analysis parameters
DEFAULT_INTENSITY_THRESHOLD = 20
MAX_HYDROGEN_RATIO = 2.0

# File parsing settings
JCAMP_NUMERIC_INDICATOR = '0123456789'

# Display settings
DEFAULT_PLOT_TITLE = "Mass Spectra"
DEFAULT_Y_LABEL = "Relative Intensity"
DEFAULT_X_LABEL = "m/z"

# Chemical formula limits
MAX_CARBON_ATOMS = 100
MIN_DBE = 0