# import packages
import re
import pandas as pd
import logomaker
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

def load_pwm_probability_matrix(file_path: str):
    """Read the first 'Probability matrix' from a PWM text file and
    return it as a list of [A, C, G, T] rows per position (P structure)."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    try:
        idx = next(i for i, line in enumerate(lines) if line.strip().lower() == 'probability matrix')
    except StopIteration:
        raise ValueError("'Probability matrix' header not found in file.")

    nuc_lines = lines[idx + 1 : idx + 5]
    parsed = {}
    for line in nuc_lines:
        if ':' not in line:
            continue
        label, rest = line.split(':', 1)
        label = label.strip()
        parts = re.split(r"\s+", rest.strip())
        vals = [float(p) for p in parts if p]
        parsed[label] = vals

    for nuc in ['A', 'C', 'G', 'T']:
        if nuc not in parsed:
            raise ValueError(f"Missing row for nucleotide '{nuc}'.")

    n_positions = len(parsed['A'])
    P_matrix = []
    for pos in range(n_positions):
        row = [parsed['A'][pos], parsed['C'][pos], parsed['G'][pos], parsed['T'][pos]]
        # optional renormalization to ensure each row sums to 1
        s = sum(row) or 1.0
        P_matrix.append([v / s for v in row])
    return P_matrix

P = [
    [0.408433395047277, 0.0956826076835842, 0.190137948246056, 0.305746049023083],  # Pos 1
    [0.281376722551463, 0.270927894530135, 0.242489348627911, 0.205206034290491],  # Pos 2
    [0.263582851865763, 0.22766552698685,  0.101031251748831, 0.407720369398556],  # Pos 3
    [0.445077685857706, 0.295938536515709, 0.0921250741219364, 0.166858703504648], # Pos 4
    [0.366154591644029, 0.164549309267025, 0.18020620787552,  0.289089891213425],  # Pos 5
    [0.4314240682835,   0.055303377391311, 0.156036347699385, 0.357236206625804],  # Pos 6
    [0.240564183361746, 0.0579765115876608, 0.0845776797405954, 0.616881625309998], # Pos 7
    [0.651652598516066, 0.109984047575195, 0.150251690112694, 0.0881116637960449], # Pos 8
    [0.0279149687307194, 0.927962160585145, 0.0102685857921324, 0.0338542848920034], # Pos 9
    [0.0502280745376657, 0.888826642364584, 0.0178085926182859, 0.0431366904794645], # Pos 10
    [0.0249227864948051, 0.92958600331709,  0.0121003538185325, 0.0333908563695728], # Pos 11
    [0.676756897182236, 0.00830038641023905, 0.133010220957148, 0.181932495450377], # Pos 12
    [0.125148007470904, 0.835193292377145, 0.00758925999735784, 0.0320694401545933], # Pos 13
    [0.0546772120741914, 0.89462257917745,  0.0142866733852458, 0.0364135353631131], # Pos 14
    [0.0355125755702617, 0.89882563622691,  0.0272244641560639, 0.0384373240467645], # Pos 15
    [0.206410777918164, 0.332561244400311, 0.166786281276195, 0.294241696405331],  # Pos 16
    [0.275480890778383, 0.18641516168608,  0.117157344992654, 0.420946602542883],  # Pos 17
    [0.354914734743446, 0.151637232008574, 0.155035142389598, 0.338412890858382],  # Pos 18
    [0.276051827749458, 0.235100625644068, 0.124057266014662, 0.364790280591812],  # Pos 19
    [0.371327161869755, 0.378962447188382, 0.10408309989157,  0.145627291050293],  # Pos 20
    [0.22236177066066,  0.433320638133398, 0.0791840832064862, 0.265133507999456], # Pos 21
    [0.329232326930375, 0.206265009656879, 0.121328963683538, 0.343173699729209],  # Pos 22
]

# Optional: set this to a PWM file to auto-fill P from the first Probability matrix
# PWM_FILE = r"c:\Users\Sana\GitHub\sana-python-course-assignments2026-1\day08\pwm_files\FL_R1_highC.txt"
PWM_FILE = r"c:\Users\Sana\GitHub\sana-python-course-assignments2026-1\day08\pwm_files\FL_R1_highC.txt"

if PWM_FILE:
    P = load_pwm_probability_matrix(PWM_FILE)
    print(f"Loaded Probability matrix from: {PWM_FILE}")
    print(f"Parsed positions: {len(P)}")
else:
    print(f"Using hard-coded P with {len(P)} positions")


# creating it as DataFrame
P = pd.DataFrame(P, columns=['A', 'C', 'G', 'T'], index=range(1, len(P) + 1))
print("DataFrame created: shape", P.shape)

# plot it (see here all plotting options https://logomaker.readthedocs.io/en/latest/implementation.html)
logomaker.Logo(df=P)
plt.ylabel('Probabilities')

# calculate entropy
entropy = np.sum(P * np.log2(P / 0.25), axis=1)

# scale each position of P with the entropy value
P_entropy = P.values * entropy.values.reshape(-1, 1)
P_entropy = pd.DataFrame(P_entropy, columns=P.columns, index=P.index)

# plot it
logomaker.Logo(df=P_entropy)
plt.ylim(0, 2)
plt.title("MSN2 in Argenine at 200nM", fontsize=18, fontweight='bold', pad=20)
plt.ylabel('Information Content [bits]', fontsize=12)
plt.xlabel('Position', fontsize=12)
plt.tick_params(axis='x', labelsize=12)  # Change font size of x-axis tick labels
plt.tick_params(axis='y', labelsize=12)  # Change font size of y-axis tick labels