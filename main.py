# load excel files one by one with all vouchers from the ./uploads folder
# the excel file contains vouchercodes, but has no csv header

# prompt to user and save the value for the following questions:
# 1. What is the batch ID?
# 2. What is the supplier ID?

# convert the excel files one by one to csv
# where all the vouchers are under csv header 'code'
# for each row, add the batch ID from the prompt to the csv line under csv header 'batch_id' 
# for each row, add the supplier ID from the prompt to the csv line under csv header 'supplier_id'

# Save the .csv file to the ./done folder

# log when it's done

import os
import pandas as pd
from pathlib import Path

def main():
    Path("./uploads").mkdir(parents=True, exist_ok=True)
    Path("./done").mkdir(parents=True, exist_ok=True)

    for file_name in os.listdir("./uploads"):
        if file_name.endswith(".xlsx") or file_name.endswith(".xls"):
            file_path = os.path.join("./uploads", file_name)
            
            print(f"Processing file: {file_name}")
            batch_id = input("What is the batch ID? ")
            supplier_id = input("What is the supplier ID? ")
            
            df = pd.read_excel(file_path, header=None)
            
            df.columns = ['code']
            
            df['batch_id'] = batch_id
            df['supplier_id'] = supplier_id
            
            csv_file_name = os.path.splitext(file_name)[0] + ".csv"
            csv_file_path = os.path.join("./done", csv_file_name)
            
            df.to_csv(csv_file_path, index=False, header=True)
            
            print(f"File {file_name} is converted and saved as {csv_file_name}")

            os.remove(file_path) # OR move the excel file to backup folder?
            print(f"File {file_name} is removed from uploads folder")

    print("All files are processed.")

if __name__ == "__main__":
    main()