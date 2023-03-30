#!env/bin/python

import csv
import requests
import time
from lxml import html

QUERY = "https://www.mcrealestate.org/Datalets/PrintDatalet.aspx?pin=PARCEL_ID&gsp=PROFILEALL&taxyear=2012&jur=000&ownseq=0&card=1&roll=RP_OH&State=1&item=1&items=-1&all=undefined&ranks=Datalet,Sketch"

XPATH = "//font[@size=-2]/text()"

def convert_string_to_int(string):
    return int(float(string))

def scrape():
    properties = open("./daytontaxroll.csv", "r")
    props_reader = csv.reader(properties)

    output_file = open("./alldaytonscraped.csv", "w")
    output_writer = csv.writer(output_file)

    count = 1;
    for line in props_reader:
        print("Querying for ", line[1], count)
        count += 1
        parcel_query = QUERY.replace("PARCEL_ID", line[1])
        r = requests.get(parcel_query)
        data = html.fromstring(r.text)
        values = data.xpath(XPATH)
        if len(values) != 10:
            print('ERROR', line[0], values)
            output_writer.writerow([line[1], '!', '!', '!'])
        else:
            print(
                int(values[3].replace(',','')),
                int(values[5].replace(',','')),
                int(values[9].replace(',','')),
                convert_string_to_int(line[33]),
                convert_string_to_int(line[34]),
                convert_string_to_int(line[35]),
                line[49])
            output_writer.writerow([
                line[1],
                int(values[3].replace(',','')),
                int(values[5].replace(',','')),
                int(values[9].replace(',','')),
                convert_string_to_int(line[33]),
                convert_string_to_int(line[34]),
                convert_string_to_int(line[35]),
                line[49]
            ])
        time.sleep(1.5)
       

if __name__ == "__main__":
    scrape()
