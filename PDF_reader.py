import pdfplumber

with pdfplumber.open("60  DALOG PERFORMANCE REPORT CAULDON MAAG TTVL 3080A RAW MILL  2022.09.27.pdf") as pdf:
    first_page = pdf.pages[4]
    print(first_page.extract_tables(table_settings={}))