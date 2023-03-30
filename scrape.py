#!env/bin/python

import csv
import requests
import time
from lxml import html

QUERY = "https://www.mcrealestate.org/Datalets/PrintDatalet.aspx?pin=PARCEL_ID&gsp=PROFILEALL&taxyear=2012&jur=000&ownseq=0&card=1&roll=RP_OH&State=1&item=1&items=-1&all=undefined&ranks=Datalet,Sketch"

XPATH = "//font[@size=-2]/text()"

def scrape():
    properties = open("./historic.csv", "r")
    props_reader = csv.reader(properties)
    next(props_reader)

    output_file = open("./rawscraped.csv", "w")
    output_writer = csv.writer(output_file)

    for line in props_reader:
        print("Querying for ", line[0])
        parcel_query = QUERY.replace("PARCEL_ID", line[0])
        r = requests.get(parcel_query)
        data = html.fromstring(r.text)
        values = data.xpath(XPATH)
        if len(values) != 10:
            print('ERROR', line[0], values)
            output_writer.writerow([line[0], '!', '!', '!'])
        else:
            print(
                int(values[3].replace(',','')),
                int(values[5].replace(',','')),
                int(values[9].replace(',','')))
            output_writer.writerow([
                line[0],
                int(values[3].replace(',','')),
                int(values[5].replace(',','')),
                int(values[9].replace(',',''))
            ])
        time.sleep(2)
       

if __name__ == "__main__":
    scrape()
