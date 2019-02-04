import csv
import os
path = "PATH TO CSV GOES HERE"
os.chdir(path)
from data.models import Data
from data.csv_importer_helpers import clean

with open('challenge_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    format_string = '%m/%d/%Y'
    for row in reader:
        #Store cleaned fields in memory
        area_unit = row['area_unit']
        bathrooms = clean(row['bathrooms'], "float", inc)
        bedrooms = clean(row['bedrooms'], "integer", inc)
        home_size = clean(row['home_size'], "integer", inc)
        home_type = row['home_type']
        last_sold_date = clean(row['last_sold_date'], "date", inc)
        last_sold_price = clean(row['last_sold_price'], "integer", inc)
        link = row['link']
        price = clean(row['price'], "price", inc)
        property_size = clean(row['property_size'], "integer", inc)
        rent_price = clean(row['rent_price'], "integer", inc)
        rentzestimate_amount = clean(row['rentzestimate_amount'], "integer", inc)
        rentzestimate_last_updated = clean(row['rentzestimate_last_updated'], "date", inc)
        tax_value = clean(row['tax_value'], "integer", inc)
        tax_year = clean(row['tax_year'], "integer", inc)
        year_built = clean(row['year_built'], "integer", inc)
        zestimate_amount = clean(row['zestimate_amount'], "integer", inc)
        zestimate_last_updated = clean(row['zestimate_last_updated'], "date", inc)
        zillow_id = row['zillow_id']
        address = row['address']
        city = row['city']
        state = row['state']
        zipcode = row['zipcode']
        p = Data(
            #Populate rows
            area_unit=area_unit, bathrooms=bathrooms, bedrooms=bedrooms, home_size=home_size, home_type=home_type, last_sold_date=last_sold_date, last_sold_price=last_sold_price, link=link, price=price, property_size=property_size, rent_price=rent_price, rentzestimate_amount=rentzestimate_amount, rentzestimate_last_updated=rentzestimate_last_updated, tax_value=tax_value, tax_year=tax_year, year_built=year_built, zestimate_amount=zestimate_amount, zestimate_last_updated=zestimate_last_updated, zillow_id=zillow_id, address=address, city=city, state=state, zipcode=zipcode)
        #save to database
        p.save()

exit()