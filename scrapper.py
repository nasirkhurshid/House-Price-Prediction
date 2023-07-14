import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

aria_labels = ["Price", "Location", "Beds", "Baths", "Area"]
header_row = ["House No."]
for label in aria_labels:
    header_row.append(label)
sheet.append(header_row)

n = 1
for i in range(14):
    url = "https://www.zameen.com/Houses_Property/Islamabad_F_7-165-"+str(i+1)+".html"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    listing = soup.find_all(attrs={"aria-label": "Listing"})

    for list in listing:
        prices = list.find_all(attrs={"aria-label": "Price"})
        locations = list.find_all(attrs={"aria-label": "Location"})
        beds = list.find_all(attrs={"aria-label": "Beds"})
        baths = list.find_all(attrs={"aria-label": "Baths"})
        areas = list.find_all(attrs={"aria-label": "Area"})

        row_data = [n]
        n += 1
        row_data.append(prices[0].text if prices else "")
        row_data.append(locations[0].text if locations else "")
        row_data.append(beds[0].text if beds else "")
        row_data.append(baths[0].text if baths else "")
        row_data.append(areas[0].text if areas else "")

        sheet.append(row_data)
    
    print("Wrote {} records!".format(n))

wb.save("houses.xlsx")