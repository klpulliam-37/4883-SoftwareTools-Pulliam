import csv

def parse_codes():
    codes = []

    with open('airport_codes.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            codes.append(row[0])

    return codes

if __name__=='__main__':
    print(parse_codes())