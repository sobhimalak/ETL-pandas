import os
import pandas as pd

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = CURR_DIR_PATH + '/data/attendance_data-1'

# Get a list of all the files in the DATA_PATH directory
file_list = os.listdir(DATA_PATH)

# Filter the list to only include files with a .csv or .txt extension
csv_files = [file for file in file_list if file.endswith('.csv')]
txt_files = [file for file in file_list if file.endswith('.txt')]

# Set the subject name
subject_name = 'biology'

# Determine which file extension is used
if len(csv_files) > len(txt_files):
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
# merged_data = merged_data.drop('Unnamed: 0', axis=1)

# Merge the "first name" and "last name" columns into a new "Full Name" column and
# insert it at the start of the DataFrame
merged_data.insert(1, 'Full Name', merged_data['firstname'] + ' ' + merged_data['surname'])
# Drop the first and last name columns
merged_data = merged_data.drop(['firstname', 'surname'], axis = 1)

# Write the merged data to a CSV file
merged_data.to_csv(os.path.join(DATA_PATH, f"{subject_name}_data.csv"), index = False)

# Write the merged data to a JSON file
biology_data = CURR_DIR_PATH + '/data/attendance_data-1/biology_data.csv'
herbology_data = CURR_DIR_PATH + '/data/attendance_data-1/herbology_data.csv'
pe_data = CURR_DIR_PATH + '/data/attendance_data-1/pe_data.csv'
math_data = CURR_DIR_PATH + '/data/attendance_data-1/math_data.csv'
physics_data = CURR_DIR_PATH + '/data/attendance_data-1/physics_data.csv'

# read the data from the file and print it
with open(biology_data, 'r') as file:
    data = file.read()
    print(merged_data)

# print a message to the console to indicate that the file has been saved
print(f"Merging and saving complete for {subject_name}!")


#create a read me file and write some text to it to explain what the going on in the project
with open('README.md', 'w') as file:
    file.write('This is a readme file')