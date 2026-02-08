#in this code i want to plot a simple graph to compare the viscosity of water against its temperature
# The raw data is from https://chem-casts.com/data-tables/water-viscosity-data-table
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_excel("water_viscosity_1bar_40e7fd0bdb.xlsx")
data.head()
print(data.columns)

plt.figure()
plt.plot(data["Temperature (Â°C)"], data["Dynamic Viscosity (mPaÂ·s)"], c="red", linewidth="2", label="temp vs dyn visc")
plt.plot(data["Temperature (Â°C)"], data["Kinematic Viscosity (mmÂ²/s)"], c="blue", linewidth="2", linestyle="dashed", label="temp vs kin visc")
plt.xlabel("Temperature °C")
plt.ylabel("Viscosity")
plt.title("Tempature of water vs viscocity")
plt.legend()
plt.show()
