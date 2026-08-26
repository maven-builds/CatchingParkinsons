# Access UCI Data Set To Run This

# THIS CODE IS STILL VERY EARLY IN-PROGRESS AND IS FAR FROM FUNCTIONAL

import matplotlib.pyplot as plt
import numpy as np

# All RBD patients in this set are idiopathic cases

pdPatients = np.array(["PD01", "PD05", "PD06", "PD22", "PD24", "PD29"])
rbdPatients = np.array(["RBD08", "RBD04", "RBD07", "RBD12", "RBD16", "RBD18", "RBD19", "RBD22", "RBD29", "RBD35", "RBD40", "RBD43", "RBD45", "RBD49"])
healthyControls = np.array(["HC04", "HC05", "HC12", "HC18", "HC19", "HC20", "HC22", "HC23", "HC25", "HC26", "HC41", "HC44", "HC48", "HC50"])

lineStylePD = dict(marker = "o", markersize = 8, markerfacecolor = "blue", linestyle = "solid", linewidth = 2)
lineStyleRBD = dict(marker = "o", markersize = 8, markerfacecolor = "orange", linestyle = "solid", linewidth = 2)
lineStyleHC = dict(marker = "o", markersize = 8, markerfacecolor = "green", linestyle = "solid", linewidth = 2) # Creating a dictionary for line specifications

speechScoreEST1 = [1.564, 1.543, 1.553, 1.546, 1.573, 1.559]
speechScoreEST2 = [1.564, 1.551, 1.554, 1.56, 1.564, 1.552, 1.559, 1.565, 1.468, 1.534, 1.559, 1.556, 1.485, 1.537]
speechScoreEST3 = [1.546, 1.558, 1.544, 1.563, 1.557, 1.508, 1.557, 1.558, 1.554, 1.549, 1.545, 1.561, 1.54, 1.552]

#plt.plot(pdPatients, speechScoreEST1, label = "PD Patients", **lineStylePD)
#plt.plot(rbdPatients, speechScoreEST2, label = "RBD Patients", **lineStyleRBD)
#plt.plot(healthyControls, speechScoreEST3, label = "Healthy Controls", **lineStyleHC)

plt.boxplot([speechScoreEST1, speechScoreEST2, speechScoreEST3], labels = ["PD Patients", "RBD Patients", "Healthy Controls"])

plt.title("Entropy of Speech Timing (-) | Middle Cohort", color = "blue", fontweight = "bold")
# plt.xlabel("Profiles", color = "green", fontweight = "bold")
plt.ylabel("EST (Dimensionless)", color = "green", fontweight = "bold")

# plt.xticks(rotation = 45)
plt.legend()
plt.show()