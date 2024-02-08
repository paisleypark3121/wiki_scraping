import asyncio
import pdfkit
from pyppeteer import launch
from Wikipedia2PDF import Wikipedia2PDF

import wikipedia

async def save_wikipedia_page_as_pdf(url, output_path):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url, {'waitUntil': 'networkidle0'})
    await page.pdf({'path': output_path, 'format': 'A4'})
    await browser.close()

def save_wikipedia_page_as_pdf(url, output_path):
    HTML(url).write_pdf(output_path)

# url = "https://it.m.wikipedia.org/wiki/Moto_rettilineo"
# output_path = "pagina_di_esempio.pdf"
# Wikipedia2PDF(url, filename=output_path)
#await save_wikipedia_page_as_pdf(url, output_path)
#save_wikipedia_page_as_pdf(url, output_path)

# response=wikipedia.search("uniform rectilinear motion")
# response=wikipedia.summary("Linear motion")
# print(response)

# page=wikipedia.page("Linear motion").content
# print(page)


import wikipedia
from bs4 import BeautifulSoup

topic = wikipedia.page('kinetic energy')
equations = BeautifulSoup(topic.html(),'lxml').find_all('annotation')

print(equations[0].text)

from pylatexenc.latex2text import LatexNodes2Text
text = LatexNodes2Text().latex_to_text(equations[0].text)
print(text)