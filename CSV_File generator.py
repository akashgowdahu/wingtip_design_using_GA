import numpy as np
import pandas as pd

# Define the ranges and number of samples for each parameter
start1 = 0.16
stop1 = 0.25
num_samples1 = 100 # Change this according to your needs

start2 = 30.00
stop2 = 55.00
num_samples2 = 100 # Change this according to your needs

start3 = 0.05     
stop3 = 0.12        
num_samples3 = 100 # Change this according to your needs

start4 = 115.00
stop4 = 125.00
num_samples4 = 100 # Change this according to your needs

start5 = 213.00
stop5 = 223.00
num_samples5 = 100 # Change this according to your needs

start6 = 1.00
stop6 = 100.00
num_samples6 = 100 # Change this according to your needs

start7 = 8.00
stop7 = 108.00
num_samples7 = 100 # Change this according to your needs

# Generate the parameters
parameters1 = np.linspace(start1, stop1, num_samples1)
parameters2 = np.linspace(start2, stop2, num_samples2)
parameters3 = np.linspace(start3, stop3, num_samples3)
parameters4 = np.linspace(start4, stop4, num_samples4)
parameters5 = np.linspace(start5, stop5, num_samples5)
parameters6 = np.linspace(start6, stop6, num_samples6)
parameters7 = np.linspace(start7, stop7, num_samples7)

# Create a DataFrame with modified column names
df = pd.DataFrame({'wing': parameters1, 'wingtiph': parameters2, 'wingtipscale': parameters3, 'wingtipx': parameters4, 'wingtipz': parameters5, 'drag': parameters6, 'upper surface transition position': parameters7})

# Write the DataFrame to a CSV file
df.to_csv('D:/Wingtip_design project/generation_0_parameters.csv', index=False)