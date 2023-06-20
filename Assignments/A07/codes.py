import csv

# Creates list of airport codes based on csv file
def parse_codes():
    codes = []

    with open('airport_codes.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            codes.append(row[0])

    return codes

# Testing
if __name__=='__main__':
    pass
    # print(parse_codes())