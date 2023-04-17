import os
import pandas as pd

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = CURR_DIR_PATH + '/data/attendance_data-1'

subject_name = 'pe'
file_extension = DATA_PATH

if file_extension in ['.txt', '.csv']:
    file_extension = '.txt'
else:
    file_extension = '.csv'

# Create an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Loop over all the subject files and concatenate them into the merged_data DataFrame
for i in range(31):
    file_path = os.path.join(DATA_PATH, f"{subject_name}_{i:02d}{file_extension}")
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
        merged_data = pd.concat([merged_data, data])

# Drop the "Unnamed: 0" column
#merged_data = merged_data.drop('Unnamed: 0', axis=1)

# Write the merged data to a CSV file
merged_data.to_csv(os.path.join(DATA_PATH, f"{subject_name}_data.csv"), index=False)

biology_data = CURR_DIR_PATH + '/data/attendance_data-1/biology_data.csv'
pe_data = CURR_DIR_PATH + '/data/attendance_data-1/pe_data.csv'
math_data = CURR_DIR_PATH + '/data/attendance_data-1/math_data.csv'
physics_data = CURR_DIR_PATH + '/data/attendance_data-1/physics_data.csv'





with open(biology_data, 'r') as file:
    data = file.read()
    print(merged_data)


print("Merging and saving complete!")
