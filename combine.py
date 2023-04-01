#!env/bin/python
import csv

def convert_string_to_int(string):
    return int(float(string))

def search():
    all_props = open("./daytontaxroll.csv", "r")
    scraped_props = open("./rawscraped.csv", "r")
    historic_props = open("./historic.csv", "r")
    combined = open("./historicscraped.csv", "w")

    all_reader =  csv.reader(all_props)
    scraped_reader = csv.reader(scraped_props)
    historic_reader = csv.reader(historic_props)

    match_writer = csv.writer(combined)

    count = 0
    for line in scraped_reader:
        found = False
        for d_line in all_reader:
            if line[0] == d_line[1]:
                found = True
                print('FOUND', line[0], line[1], d_line[33])
                for h_line in historic_reader:
                    if line[0] == h_line[0]:
                        match_writer.writerow([
                            line[0],
                            line[1],
                            line[2],
                            line[3],
                            convert_string_to_int(d_line[33]),
                            convert_string_to_int(d_line[34]),
                            convert_string_to_int(d_line[35]),
                            h_line[8],
                            h_line[9],
                            h_line[10]])
                        count += 1
                        print(count)
                        continue
                historic_props.seek(0)
                historic_reader = csv.reader(historic_props)
                continue
        if not found:
            print("not found", line[0], d_line[1])
        all_props.seek(0)
        all_reader = csv.reader(all_props)

    all_props.close()
    scraped_props.close()
    combined.close()


if __name__ == "__main__":
    search()
