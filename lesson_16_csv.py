import csv

def csv_reader(filename: str):
    data = []
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        for row in reader:
            data.append(row)

    return data

filename = "data.csv"
data = csv_reader(filename)
print(data)