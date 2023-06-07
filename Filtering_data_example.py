import openpyxl
import pandas as pd

def filter_duplicates_excel(file_path, sheet_name, sheet2_name, output_file_path):
    # load workbook and sheets 
    wb = openpyxl.load_workbook(file_path)
    sheet = wb[sheet_name]
    sheet2 = wb[sheet2_name]

    # convert sheet to a pandas dataframe
    data = sheet.values
    columns = next(data)  # Get the column names from the first row
    df = pd.DataFrame(data, columns=columns)

    # loop through sheet and find matches 
    for index, row in df.iterrows():
        column = row['uni_prot'] # select desired column to change
        if column is not None and any(x[0] == column for x in sheet2.iter_rows(min_row=2, values_only=True)): # change element of x to select column
            df.drop(index, inplace=True) # remove rows 

    # Ssave output
    df.to_csv(output_file_path, index=False)

    wb.close()

    print(f"Filtering complete. Modified data saved to {output_file_path}")

# Usage example
file_path = "C:/Users/"
sheet_name = "sheet1"
sheet2_name = "rows_2_remove"
output_file_path = "C:/Users/filtered_data.xls"

filter_duplicates_excel(file_path, sheet_name, sheet2_name, output_file_path)
