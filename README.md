# Historic Properties Scripts #

This repo contains a handful of python scripts related to the Preservation Dayton project.

## Setup ##
Taxroll.csv file is not included in this repo due to its size (600MB).  You can get it from the Montgomery County Auditor's website.  The file is updated every month.  The file is located at http://www.mctreas.org/mctreas/fdpopup.cfm?dtype=TR. This file is used by a few of the scripts below.

### Requirements ###

Create a virtual environment and install the requirements:

```bash 
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Scripts ##

scrape.py - This script scrapes the Montgomery County Auditor's website for 2012 property data for historic properties.  It uses historic.csv file to identify the properties to scrape.

filter.py - This script filters the taxroll.csv (see the *Setup* section to see how to get this file) file to only include properties with a Dayton parcel id.

scrapeall.py - This script is the same as the scrape.py script, but it scrapes all of the properties in the taxroll.csv file.

combine.py - This script combines the scraped historic properties with taxroll.csv file data.

remove_historic.py - This script removes the historic properties from the alldaytonscraped.csv file.

## Data ##

historic.csv - This file contains a list of historic properties in Dayton. It was provided by Preservation Dayton.

rawscraped.csv - This file contains the scraped data from the scrape.py script. It is all the properties in the historic.csv file.

historicscraped.csv - This file contains the output from the combine.py script. It combines the data from rawscraped.csv with info from historic.csv and the daytontaxroll.csv.

alldaytonscraped.csv - This file contains the scraped data from the scrapeall.py script. This matches the format of the historicscraped.csv file.

nonhistoricscraped.csv - This file contains the contents of alldaytonscraped.csv without the properties in historic.csv.

Scraped data format:
Each row is a property.  The columns are:
Parcel ID - Dayton Parcel id, our unique id
2012 Value for ASMTLAND - 100% Appraised Land Value
2012 Value for ASMTBLDG - 100% Appraised Building Value
2012 Value for ASMTTOTAL - 100% Appraised Total Value 
2023 Value for ASMTLAND - 100% Appraised Land Value
2023 Value for ASMTBLDG - 100% Appraised Building Value
2023 Value for ASMTTOTAL - 100% Appraised Total Value
Planning District
Designation - Historic Designation
Neighborhood

If we couldn't find a 2012 value for the property, the values are replaced with exclamation points (!). They should be removed from the analysis.

The alldaytonscraped.csv and nonhistoricscraped.csv file contains the same data, but we include the NBHD code from the taxroll file. It doesn't align with the neighborhoods in historic.csv, but it is a start.