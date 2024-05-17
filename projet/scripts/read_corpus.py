import pandas as pd
import sys

def load_data(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Display the first few lines of the DataFrame to verify
    print(df.head())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_csv_file>")
    else:
        load_data(sys.argv[1])
