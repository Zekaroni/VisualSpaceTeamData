from csv import reader
from os import path

def getCSVData(file_name: str):
    if file_name.lower().endswith('.csv'):
        if path.isfile(file_name):
            _data = []
            with open(file_name, newline='') as csvfile:
                file_contents = reader(csvfile)
                for row in file_contents:
                    _data.append(row)
            return _data
        else:
            raise FileExistsError("File does not exist")
    else:
        raise ValueError("Non-csv file given")