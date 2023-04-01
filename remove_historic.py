#!env/bin/python
import csv

def convert_string_to_int(string):
    return int(float(string))

def search():
    all_props = open("./alldaytonscraped.csv", "r")
    historic_props = open("./historic.csv", "r")
    combined = open("./nonhistoric.csv", "w")

    all_reader =  csv.reader(all_props)
    historic_reader = csv.reader(historic_props)

    match_writer = csv.writer(combined)

    count = 0
    found_count = 0
    for line in all_reader:
        found = False
        for h_line in historic_reader:
            if line[0] == h_line[0]:
                found = True
                found_count += 1
                print('FOUND', found_count, line[0])
                break
        if not found:
            match_writer.writerow(line)
            count += 1
            print(count)
        historic_props.seek(0)
        historic_reader = csv.reader(historic_props)

    all_props.close()
    combined.close()
    print('found', found_count, 'not found', count)


if __name__ == "__main__":
    search()
