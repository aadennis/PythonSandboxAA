import pandas as pd

def get_csv():
    print("in callee")
    file_path = "c:/temp/logfile02.log"
    return pd.read_csv(file_path, skiprows=4, encoding='CP1252')

if __name__ == "__main__":
    print("running main in callee.py")
    a = get_csv()
