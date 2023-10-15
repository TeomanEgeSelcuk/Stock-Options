
import numpy as np
import pandas as pd
from scipy.stats import norm
import pytest
import os

# Test if the CSV file exists and is readable
def test_csv_file():
    # Specify the file path (update this path as per your file location)
    file_path = '/mnt/data/Cleaned_data_aapl.csv'  # Update this path as needed

    # Assert if the file exists
    assert os.path.exists(file_path), f"The file at path {file_path} does not exist"

    # Try to read the file and assert if it's readable
    try:
        pd.read_csv(file_path)
    except Exception as e:
        pytest.fail(f"Could not read the CSV file at {file_path}: {e}")


import numpy as np
import pandas as pd
from scipy.stats import norm
import pytest

# Load the CSV file
file_path = '/mnt/data/Cleaned_data_aapl.csv'
df = pd.read_csv(file_path)

# Function to calculate Theta and Rho
def calculate_theta_rho(row, r=0.01):
    S = row['UNDERLYING_LAST']
    K = row['STRIKE']
    T = row['DTE'] / 365.25  # Convert days to years
    sigma = row['C_IV']

    # Calculate d1 and d2
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    # Calculate Theta
    theta = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))

    # Calculate Rho
    rho = K * T * np.exp(-r * T) * norm.cdf(d2)

    return theta, rho

# Test function to compare calculated Theta and Rho with CSV values and calculate % difference
@pytest.mark.parametrize("index, row", df.iterrows())
def test_theta_rho(index, row):
    # Tolerance level for the percentage difference
    tolerance = 5  # Adjust this value as needed

    # Calculate Theta and Rho
    theta, rho = calculate_theta_rho(row)

    # Get C_THETA and C_RHO from the CSV
    c_theta = row['C_THETA']
    c_rho = row['C_RHO']

    # Calculate the percentage difference
    theta_diff = np.abs((theta - c_theta) / c_theta) * 100 if c_theta != 0 else 0
    rho_diff = np.abs((rho - c_rho) / c_rho) * 100 if c_rho != 0 else 0

    # Assert if the difference is within the tolerance level, include the actual % diff in the message
    assert theta_diff <= tolerance, f"Row {index}: Theta difference {theta_diff:.2f}% exceeds {tolerance}% tolerance"
    assert rho_diff <= tolerance, f"Row {index}: Rho difference {rho_diff:.2f}% exceeds {tolerance}% tolerance"

