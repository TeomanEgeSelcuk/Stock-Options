import numpy as np
import pandas as pd
from scipy.stats import norm
import pytest
import os

# Directly set the file path based on your provided path
file_path = '/app/src/Cleaned_data_aapl.csv'

# Assert if the file exists
assert os.path.exists(file_path), f"The file at path {file_path} does not exist"

# Try to read the file and assert if it's readable
try:
    df = pd.read_csv(file_path)
except Exception as e:
    pytest.fail(f"Could not read the CSV file at {file_path}: {e}")

# Try to read the file and assert if it's readable
try:
    df = pd.read_csv(file_path)
    
    # Calculate the number of rows for the first 1/N th
    n_rows = len(df) // 10

    # Select the first 1/N th of the rows
    df = df.iloc[:n_rows]

except Exception as e:
    pytest.fail(f"Could not read the CSV file at {file_path}: {e}")

# Function to calculate Theta and Rho
def calculate_theta_rho(row: pd.Series, r: float = 0.01) -> (float, float):
    """
    Calculate the Theta and Rho for given option data.
    
    Parameters:
    - row: pd.Series containing the option data.
    - r: float, risk-free interest rate.

    Returns:
    - Theta and Rho as float.
    """
    # Step 1: Extract necessary data from the row
    S = row['UNDERLYING_LAST']  # Underlying price
    K = row['STRIKE']  # Strike price
    T = row['DTE'] / 365.25  # Convert days to years (Days to expiration)
    sigma = row['C_IV']  # Implied volatility

    # Step 2: Calculate d1 and d2 using the given formulas
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    # Step 3: Calculate Theta using the given formula
    theta = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))

    # Step 4: Calculate Rho using the given formula
    rho = K * T * np.exp(-r * T) * norm.cdf(d2)

    return theta, rho

# Test function to compare calculated Theta and Rho with CSV values and calculate % difference
def test_average_theta_rho() -> None:
    """
    Test the average Theta and Rho difference against the tolerance level.
    
    Raises an assertion error if the average difference exceeds the tolerance.
    """
    theta_diffs = np.array([])
    rho_diffs = np.array([])

    for _, row in df.iterrows():
        # Calculate Theta and Rho for each row
        theta, rho = calculate_theta_rho(row)
        
        # Extract the C_THETA and C_RHO values from the CSV
        c_theta = row['C_THETA']
        c_rho = row['C_RHO']

        # Calculate the percentage difference for Theta and Rho
        theta_diff = np.abs((theta - c_theta) / c_theta) * 100 if c_theta != 0 else 0
        rho_diff = np.abs((rho - c_rho) / c_rho) * 100 if c_rho != 0 else 0

        # Append the percentage differences to the arrays
        theta_diff = np.append(theta_diff, theta_diff)
        rho_diff = np.append(rho_diff, rho_diff)

    # Calculate the average percentage differences
    avg_theta_diff = np.mean(theta_diffs)
    avg_rho_diff = np.mean(rho_diffs)

    # Specify the tolerance level for the percentage difference
    tolerance = 5  

    # Assert if the average difference is within the tolerance level, else raise an error
    assert avg_theta_diff <= tolerance, f"Average Theta difference {avg_theta_diff:.2f}% exceeds {tolerance}% tolerance"
    assert avg_rho_diff <= tolerance, f"Average Rho difference {avg_rho_diff:.2f}% exceeds {tolerance}% tolerance"

# Steps
# 1. Set the file path and check if the file exists and is readable.
# 2. Read the CSV file into a DataFrame.
# 3. Calculate Theta and Rho for each row and store the differences in NumPy arrays.
# 4. Calculate the average Theta and Rho differences.
# 5. Compare the average differences to the tolerance level and assert if within tolerance.

