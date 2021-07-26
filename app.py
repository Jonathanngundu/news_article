from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.htm")



@app.route("/paper", methods=["POST"])
def paper():
    link = request.form.get('link')
    website = link
    URL = website

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup =  BeautifulSoup(page.content, 'html.parser')

    infromation = soup.find('title').get_text()
    atricle = soup.find('article').get_text()
    return render_template("paper.htm", link=link, art=atricle, infromation=infromation)

