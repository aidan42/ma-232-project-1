import numpy as np 
import pandas as pd

sectors = ["AGR", "MIN", "UTL", "CON", "MAN", "TRA", "INF", "FIN", "PRO", "GOV"]

C = np.array([
  [0.12,0.01,0.00,0.05,0.18,0.02,0.00,0.01,0.02,0.05],
  [0.02,0.08,0.15,0.08,0.22,0.05,0.01,0.00,0.01,0.02],
  [0.06,0.09,0.10,0.02,0.11,0.08,0.04,0.03,0.02,0.08],
  [0.01,0.04,0.02,0.02,0.05,0.03,0.02,0.08,0.14,0.15],
  [0.20,0.15,0.05,0.25,0.15,0.12,0.08,0.02,0.05,0.10],
  [0.08,0.10,0.06,0.06,0.08,0.07,0.03,0.01,0.04,0.05],
  [0.01,0.02,0.02,0.01,0.04,0.04,0.12,0.10,0.15,0.06],
  [0.04,0.05,0.03,0.08,0.06,0.05,0.10,0.15,0.12,0.04],
  [0.05,0.06,0.04,0.10,0.08,0.06,0.18,0.12,0.10,0.12],
  [0.05,0.04,0.08,0.05,0.04,0.04,0.03,0.04,0.05,0.02],
])

# 1. Column Sum Verification
column_sums = np.sum(C, axis=0)
print(f"column sums: ", column_sums)

# column sum significance: 
# if the column_sum_j < 1.0, then sector_j spends less than $1.0 per $1.0 output
# if the column_sum_g > 1.0, then sector_j spends more than $1.0 per $1.0 ouput

# why is this vital?
# In order to have a sustainaible economomy, outputs must consume less than they are outputing.
# If a sector consumes more than they output, this means they have either a zero or negative output 
#   making the secotor unprofitable.

# 2. The Leontief Matrix
I = np.identity(C.shape[0]) # initializing identitiy matrix of 10 columns
A = I - C # Leontief matrix
print(pd.DataFrame(A, index=sectors, columns=sectors).round(2)) # dataframe for easier visualization in terminal

# 3. Productivity Proof
A_inverse = np.linalg.inv(A) # computing inverse matrix => (I-C)^-1
print(pd.DataFrame(A_inverse, index=sectors, columns=sectors).round(3)) # all cells are positive
