import requests
from flask import Flask, render_template
from bs4 import BeautifulSoup

file = "kari-sakib-lab-report.txt"
url = "https://climate.nasa.gov/effects/"

def convert_tag_to_str_list(lst):
    new_lst = []
    for i in lst:
        new_lst.append(str(i))
    return new_lst

def scraper(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    data_headings = ["Climate Change Effect", "How It Happens"]
    data_findings = [x for x in range(2)]
    text_headings = convert_tag_to_str_list(soup.findAll('h2'))
    text_desc = convert_tag_to_str_list(soup.find('aside'))
    text_desc = text_desc[-2:-1]
    text_desc = text_desc[0][109:-11]
    heading = []
    for i in text_headings:
        if i.startswith('<h2 class='):
            heading.append(i)
    heading = heading[0][27:-6]
    data_findings[0] = heading
    data_findings[1] = text_desc

    return data_findings[0], data_findings[1]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/data')
def data():
    return scraper(url)

@app.route('/form')
def data():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)