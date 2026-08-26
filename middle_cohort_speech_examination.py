# -*- coding: utf-8 -*-
# Access UCI Data To Run This

import matplotlib.pyplot as plt
import numpy as np

# PROFILES

pdProfiles = ["PD01", "PD05", "PD06", "PD22", "PD28", "PD29"] # PARKINSON'S DISEASE PATIENTS (NO MEDICATION)
rbdProfiles = ["RBD02", "RBD05", "RBD07", "RBD12", "RBD16", "RBD18", "RBD19", "RBD22", "RBD29", "RBD35", "RBD40", "RBD43", "RBD45", "RBD49"] # PATIENTS WITH A CASE OF IDIOPATIC RBD (NO MEDICATION)
healthyControls = [] # HEALTHY INDIVIDUALS (NO MEDICATION)

# Speech Examination Figures (PD PATIENTS)

# ENTROPY OF SPEECH TIMING
estScoreReading = [1.564, 1.543, 1.553, 1.546, 1.573, 1.559]
estScoreMonologue = [1.564, 1.56, 1.518, 1.56, 1.572, 1.562]

# RATE OF SPEECH TIMING
rstScoreReading = [354, 269, 317, 283, 340, 289]
rstScoreMonologue = [330, 230, 181, 208, 261, 325]

# ACCELERATION OF SPEECH TIMING
astScoreReading = [6.05, 6.72, 24.19, 10.09, 14.94, 18.4]
astScoreMonologue = [-2.82, 11.77, 13.38, 1, -7.02, 3.57]

# DURATION OF PAUSE INTERVALS
dpiScoreReading = [146, 211, 186, 183, 154, 174]
dpiScoreMonologue = [158, 206, 611, 374, 243, 201]

# DURATION OF VOICED INTERVALS
dviScoreReading = [264, 328, 286, 317, 258, 303]
dviScoreMonologue = [318, 480, 398, 397, 308, 287]

# GAPING IN-BETWEEN VOICED INTERVALS
gibviScoreReading = [58.65, 42.9, 43.83, 43.53, 76.58, 52.25]
gibviScoreMonologue = [49.01, 33.54, 18.18, 36.21, 51.58, 43.29]

# DURATION OF UNVOICED STOPS
dusScoreReading = [31.38, 47.12, 33.63, 41.5, 22.38, 47.13]
dusScoreMonologue = [22.37, 26.87, 49.37, 26.88, 20.13, 22.38]

# DECAY OF UNVOICED FRICATIVES
dufScoreReading = [-2.101, -0.973, 0.921, -0.989, -1.413, -0.151]
dufScoreMonologue = [0.588, 0.075, 1.488, -0.707, 0.254, 0.019]

# RELATIVE LOUDNESS OF RESPIRATION
rlrScoreReading = [-22.47, -22.61, -25, -22.98, -20.32, -28.5]
rlrScoreMonologue = [-19.77, -22.32, -25.08, -24.08, -17.7, -21.63]

# PAUSE INTERVALS PER RESPIRATION
piprScoreReading = [4.5, 5, 2.75, 3.5, 18.5, 5.5]
piprScoreMonologue = [6, 5, 2, 3, 6, 4]

# RATE OF SPEECH RESPIRATION
rsrScoreReading = [21.14, 16.26, 27.07, 21.34, 5.22, 17.63]
rsrScoreMonologue = [13.81, 14.61, 18.21, 18.56, 17.47, 24.84]

# LATENCY OF RESPIRATORY EXCHANGE
lreScoreReading = [167, 78, 124, 166, 172, 99]
lreScoreMonologue = [127, 151, 593, 174, 262, 139]


# Speech Examination Figures (iRBD PATIENTS)

estScoreReading2 = [1.564, 1.551, 1.541, 1.56, 1.564, 1.552, 1.559, 1.565, 1.468, 1.534, 1.559, 1.556, 1.485, 1.537]
estScoreMonologue2 = [1.568, 1.555, 1.56, 1.535, 1.541, 1.563, 1.555, 1.543, 1.536, 1.544, 1.556, 1.567, 1.547, 1.55]

rstScoreReading2 = [359, 358, 270, 285, 278, 342, 361, 354, 293, 337, 296, 294, 317, 297]
rstScoreMonologue2 = [286, 273, 288, 234, 247, 286, 273, 273, 246, 259, 269, 307, 255, 266]

astScoreReading2 = [37.62, 16.54, 38.15, 7.3, 13, 2.54, 12.31, 19.01, 5.07, 21.35, 4.4, 30.59, 9.15, 4.46]
astScoreMonologue2 = [-1.89, 7.01, -4.21, -5.3, -17.87, 0.97, 3.21, 0.93, -0.78, -2.74, 0.21, -2.59, 0.7, 4.61]

dpiScoreReading2 = [135, 111, 175, 250, 181, 153, 145, 126, 226, 162, 245, 177, 147, 185]
dpiScoreMonologue2 = [221, 167, 224, 404, 169, 211, 260, 217, 245, 271, 253, 191, 186, 178]

dviScoreReading2 = [264, 261, 332, 303, 327, 271, 258, 273, 284, 288, 267, 335, 313, 274]
dviScoreMonologue2 = [322, 364, 302, 318, 392, 342, 324, 308, 347, 348, 348, 284, 360, 317]

gibviScoreReading2 = [61.22, 69.57, 69.34, 39.27, 55.71, 51.11, 47.17, 69.08, 28.83, 35.17, 56.43, 49.36, 21.09, 61.76]
gibviScoreMonologue2 = [50.47, 40.98, 48.77, 29.32, 30.97, 42.91, 34.7, 41.71, 28.73, 28.56, 27.13, 59.45, 37.84, 58.27]

dusScoreReading2 = [38.12, 38.13, 50.5, 25.75, 26.88, 24.63, 24.62, 22.38, 64, 29.13, 29.13, 24.63, 42.63, 35.88]
dusScoreMonologue2 = [22.38, 22.38, 31.37, 35.88, 35.88, 22.37, 31.37, 49.37, 35.88, 35.87, 22.38, 26.87, 35.88, 29.13]

dufScoreReading2 = [0.073, -0.893, -0.297, -0.438, -3.457, -1.392, -2.492, 0.356, 5.013, -2.466, -1.372, 0.92, 1.389, 0.835]
dufScoreMonologue2 = [-0.449, 0.466, -0.483, 0.428, 1.916, -0.275, -0.134, -0.013, 0.154, 0.789, 0.241, 1.487, 0.286, -0.347]

rlrScoreReading2 = [-24.73, -18.81, -18.01, -19.66, -20.87, -25.41, -22.85, -24.17, -23.37, -20.25, -30.48, -23.55, -18.09, -15.32]
rlrScoreMonologue2 = [-15.73, -17.91, -13.99, -19.33, -16.26, -24.48, -23.13, -20.04, -20.16, -20.99, -23.91, -20.88, -20.91, -19.73]

piprScoreReading2 = [7.5, 6.25, 4.5, 3.5, 5.5, 4.75, 4.75, 8, 2, 3.25, 3.25, 5.5, 4, 5.5]
piprScoreMonologue2 = [4.5, 4, 4, 2, 4, 3.5, 4, 3, 3, 3, 3, 5, 3, 5]

rsrScoreReading2 = [15.16, 20.63, 17.17, 23.09, 17.47, 20.62, 21.43, 12.92, 18.13, 19.27, 21.83, 11.93, 14.74, 15.78]
rsrScoreMonologue2 = [18.02, 17.52, 21.66, 18.07, 18.19, 21.5, 18.9, 22.39, 19.94, 20.93, 24.02, 13.79, 15.51, 6.04]

lreScoreReading2 = [117, 88, 180, 169, 196, 166, 128, 102, 75, 80, 121, 182, 42, 69]
lreScoreMonologue2 = [266, 58, 112, 216, 165, 128, 195, 96, 15, 128, 93, 144, 80, 90]

lineStyle = dict(marker = "o", markersize = 8, markerfacecolor = "orange", linestyle = "dotted", linewidth = 2)

plt.title("Latency of Respiratory Exchange (ms) | Middle Cohort", color = "blue", fontweight = "bold")
plt.xlabel("iRBD Patients", color = "green", fontweight = "bold")
plt.ylabel("LSR (Monologue)", color = "green", fontweight = "bold")

plt.xticks(rotation = 45)

plt.plot(rbdProfiles, lreScoreMonologue2, **lineStyle)
plt.show()