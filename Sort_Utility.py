import pathlib
import os
import pandas as pd

def get_path():
    path = input("Enter the name/path of the file (CSV/XLSX) >>> ")

    if os.path.exists(path):
        name_ext_path = [pathlib.Path(path).stem, pathlib.Path(path).suffix, path]
        return name_ext_path
        

    else:
        print("File does not exist")
        get_path()
        return None
    
def load_file(name_ext_path):
    if name_ext_path[1] == ".csv":
        df = pd.read_csv(name_ext_path[2])

    elif name_ext_path[1] == ".xlsx":
        df = pd.read_excel(name_ext_path[2])

    else:
        df = None

    return df

def sort_file(df):
    # Print all the columns
    print("Columns in the file")
    print("===================")
    i = 0
    for col in df.columns:
        print(f"{i}. " + col)
        i += 1

    # Select the columns to sort
    print("Enter the column number to sort the file")
    print("=======================================")
    col_num = int(input("Enter the column number >>> "))
    col_name = df.columns[col_num]

    # Select the sort type
    print("Select sort type")
    print("1. Ascending")
    print("2. Descending")
    print("================")
    sort_type = input("Enter the sort type >>> ")
    if sort_type == "1":
        sort_type = "ascending"
    else:
        sort_type = "descending"

    # Sort the file
    print("Sorting the file based on " + col_name + " with sort type " + sort_type + "...")
    print("=====================================")
    df = df.sort_values(by=col_name)

    return df

    

def main():
    print("Sort Utility")
    print("============")
    
    path = get_path()
    if path:
        df = load_file(path)
        if df is not None:
            sorted_df = sort_file(df)

            # Save the file
            print("Enter the name of the file to save the sorted file")
            print("==================================================")
            save_file = input("Enter the name of the file >>> ")
            print("Choose the file type to save the file")
            print("1. CSV")
            print("2. Excel")
            print("========")
            file_type = input("Enter the file type >>> ")
            if file_type == "1":
                save_file = save_file + ".csv"
                sorted_df.to_csv(save_file, index=False)
            else:
                save_file = save_file + ".xlsx"
                sorted_df.to_excel(save_file, index=False)
            print("File saved as " + save_file)

        
    else:
        print("File does not exist")
        main()
    

if __name__ == "__main__":
    main()