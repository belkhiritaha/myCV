import pdfkit

# encode the html file to utf-8
with open('cv.html', 'r', encoding='utf-8') as f:
    html = f.read()

# transform cv.html to pdf
pdfkit.from_string(html, 'cv.pdf')

