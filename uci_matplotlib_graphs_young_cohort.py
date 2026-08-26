# Access UCI Data Set To Run This

# First Speech Examination Graphs

import matplotlib.pyplot as plt
import numpy as np

profile = ["PD12", "PD13", "PD19", "RBD27", "HC02", "HC07", "HC09", "HC21", "HC45", "HC49"]

# SPEAKING TASK OF READING PASSAGE

# -----------------------------------------------------------------------------------

# Entropy of Speech Timing (-) | Speaking Task of Reading Passage
# speechScore = [1.565, 1.549, 1.547, 1.565, 1.555, 1.549, 1.557, 1.567, 1.530, 1.56]

# Rate of Speech Timing (-/min) | Young Cohort
# speechScore = [365, 301, 263, 339, 339, 312, 388, 399, 457, 359]

# Duration of Pause Intervals (ms) | Young Cohort
# speechScore = [129, 224, 245, 188, 157, 138, 136, 105, 125, 169]

# Duration of Voiced Intervals (ms) | Young Cohort
# speechScore = [261, 280, 326, 239, 263, 318, 243, 253, 197, 256]

# Gaping In-Between Voiced Intervals (-/min) | Young Cohort
# speechScore = [70.09, 35.87, 40.11, 63.95, 43.42, 23.31, 40.70, 79.78, 44.38, 50.68]

# Duration of Unvoiced Stops | Young Cohort
# speechScore = [24.63, 25.75, 33.62, 33.63, 30.25, 29.13, 20.13, 22.38, 20.13, 17.88]

# Decay of Unvoiced Fricatives | Young Cohort
# speechScore = [-1.187, -2.067, -0.042, -1.412, -0.761, -0.573, -1.211, -0.868, -5.649, -0.823]

# Relative Loudness of Respiration | Young Cohort
# speechScore = [-24.99, -23.49, -22.09, -23.32, -28.5, -22.12, -28.43, -20.58, -16.49, -23.82]

# Pause Intervals per Respiration (-) | Young Cohort
# speechScore = [6.75, 3.75, 3.5, 4, 4.25, 4, 5, 9.75, 8.75, 6.5]

# Rate of Speech Respiration (-/min) | Young Cohort
# speechScore = [20.68, 24.32, 20.62, 24.18, 23.44, 16.19, 22.2, 14.26, 10.91, 18.14]

# Latency of Respiratory Exchange | Young Cohort
# speechScore = [170, 190, 136, 95, 143, 70, 118, 70, 133, 226]

# -----------------------------------------------------------------------------------



# SPEAKING TASK OF READING PASSAGE

# -----------------------------------------------------------------------------------

# Entropy of Speech Timing (-): Monologue | Young Cohort
# speechScore = [1.556, 1.514, 1.562, 1.565, 1.548, 1.555, 1.562, 1.574, 1.564, 1.561]

# Rate of Speech Timing (-/min): Monologue | Young Cohort
# speechScore = [277, 342, 295, 267, 335, 215, 295, 348, 384, 262]

# Acc. of Speech Timing (-/min²): Monologue | Young Cohort
# speechScore = [-0.81, 3.33, -0.17, -2.38, -0.12, -5.91, 5.63, -3.52, -1.67, 2.8]

# Duration of Pause Intervals (ms): Monologue | Young Cohort
# speechScore = [214, 261, 225, 259, 215, 258, 211, 141, 132, 252]

# Duration of Voiced Intervals (ms): Monologue | Young Cohort
# speechScore = [313, 248, 313, 309, 274, 407, 299, 300, 241, 361]

# Gaping In-Between Voiced Intervals (-/min): Monologue | Young Cohort
# speechScore = [50.98, 21.76, 46.69, 50.25, 31.49, 26.44, 30.62, 60.65, 56.71, 38.92]

# Duration of Unvoiced Stops (ms): Monologue | Young Cohort
# speechScore = [22.38, 26.87, 22.37, 35.87, 22.38, 26.87, 22.38, 17.88, 22.37, 26.88]

# Duration of Unvoiced Fricatives (%/min): Monologue | Young Cohort
# speechScore = [0.722, -0.12, 1.249, -0.035, 0.338, 0.606, 0.434, 0.141, -0.201, 0.389]

# Relative Loudness of Respiration: Monologue | Young Cohort
# speechScore = [-23.71, -21.98, -21.23, -20.01, -24.61, -21, -26.54, -19.12, -8.86, -17.53]

# Pause Intervals per Respiration (-): Monologue | Young Cohort
# speechScore = [4, 3, 4, 4, 6, 3, 5, 9, 6, 4]

# Rate of Speech Respiration (-/min): Monologue | Young Cohort
# speechScore = [19.25, 21.11, 16.59, 16.98, 13.72, 19.95, 14.34, 9.97, 15.75, 17.51]

# Latency of Respiratory Exchange (ms): Monologue | Young Cohort
speechScore = [179, 189, 49, 146, 260, 180, 138, 151, 117, 154]

lineStyle = dict(marker = "o", markersize = 8, markerfacecolor = "blue", linestyle = "dotted", linewidth = 2) # Creating a dictionary for line specifications

plt.title("Latency of Respiratory Exchange (ms): Monologue | Young Cohort", color = "blue", fontweight = "bold")
plt.xlabel("Profiles", color = "green", fontweight = "bold")
plt.ylabel("LRE (Monologue)", color = "green", fontweight = "bold")

plt.plot(profile, speechScore, **lineStyle)
plt.show()