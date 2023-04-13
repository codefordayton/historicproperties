#!env/bin/python
import csv

def convert_string_to_int(string):
    return int(float(string))

def search():
    all_props = open("./daytontaxroll.csv", "r")
    scraped_props = open("./nonhistoricscraped.csv", "r")
    combined = open("./nonhistoricresidential.csv", "w")

    all_reader =  csv.reader(all_props)
    scraped_reader = csv.reader(scraped_props)

    match_writer = csv.writer(combined)

    count = 0
    found_count = 0
    for line in scraped_reader:
        found = False
        for a_line in all_reader:
            if line[0] == a_line[1] and a_line[30] != 'R   ':
                found = True
                found_count += 1
                print('FOUND', found_count, line[0])
                break
        if not found:
            match_writer.writerow(line)
            count += 1
            print(line[0], count)
        all_props.seek(0)
        all_reader = csv.reader(all_props)

    all_props.close()
    combined.close()
    print('found', found_count, 'not found', count)


if __name__ == "__main__":
    search()
