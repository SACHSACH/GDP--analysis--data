import csv

#get names from the file
filename = 'countries-of-the-world.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    print(header_row)

    # north_america = []
    # for row in reader:
    #     north = int(float(row[6]))
    #     north_america.append(north)
    # print(north_america)