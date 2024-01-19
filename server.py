from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import csv


app = Flask(__name__)

def get_current_year():
    return datetime.now().year

@app.route('/')
def my_home():
    return render_template('index.html', current_year=get_current_year())

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name, current_year=get_current_year())

def write_to_csv(data):
  with open('database.csv', newline='', mode='a') as database:
    name = data["name"]
    phone = data["phone"]
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([name,phone,email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
      except:
        return 'Did not save to database'
    else:
      return 'Something went wrong. Try again!'
    
