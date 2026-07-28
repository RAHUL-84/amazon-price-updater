from openpyxl import Workbook
import os

FILE_NAME = "products.xlsx"

if not os.path.exists(FILE_NAME):

    wb = Workbook()
    ws = wb.active
    ws.title = "Products"

    ws.append([
        "Serial No",
        "Product Name",
        "Selling Price",
        "MRP",
        "Discount"
    ])

    wb.save(FILE_NAME)

    print("products.xlsx created")

else:
    print("products.xlsx already exists")