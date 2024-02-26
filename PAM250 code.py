import pandas as pd

# Read in the PAM250 matrix from an Excel file
df = pd.read_excel("/content/drive/My Drive/projects/pam250.xlsx", index_col=0)
# Create a dictionary to store the PAM250 matrix
pam250 = {}
for i in range(len(df)):
    amino1 = df.index[i]
    for j in range(len(df.columns)):
        amino2 = df.columns[j]
        score = df.iloc[i, j]
        pam250[(amino1, amino2)] = score

# Define a function to look up the score for a given amino acid pair
def pam_score(amino1, amino2):
    return pam250.get((amino1, amino2), pam250.get((amino2, amino1), None))

# Test the function with an example amino acid pair
while A_1 and A_2 != 0:
    print('Note: type END in the first input to terminate the program.')
    A_1 = input('1. Enter your first AA:ACTGACCACTGAC ').upper()
    A_2 = input('2. Enter your second AA:TCTGCCTCTGC ').upper()
    score = pam_score(A_1, A_2)
    print(score)
    if A_1 == 'END':
      break

