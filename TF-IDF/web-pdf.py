import pdfkit


path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

url_base = "http://98.126.2.246/Html/Book/38/4754/"

for i in range(119237, 119274):
    url = url_base + str(i) + ".htm"
    print(url)
    pdfkit.from_url(url, str(i) + ".pdf", configuration=config)