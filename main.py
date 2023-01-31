# class SuperList(list):
#     def __len__(self):
#         return 5
#
#
# super_list = SuperList()
# print(len(super_list))
# super_list.append(5)
# print(super_list[0])
# adds image processing capabilities
from PIL import Image

# will convert the image to text string
import pytesseract

# translates into preferred language
from googletrans import Translator

# assigning an image from the source path
# img = Image.open('images/img_2.png')
#
# # converts the image to result and saves it into result variable
# result = pytesseract.image_to_string(img)
# print(result)
# p = Translator()
#
# # translates the text into french language
# k = p.translate(result, dest='uk')
# #converts the result into string format
# translated = str(k.text)
#
# print(translated)
#
# name  =  None
# print(f"Hello {name if name else 'user'}")
from flask import render_template, url_for,Flask, request, redirect

from pymongo import MongoClient
from datetime import datetime

class DBRepository:

    def __init__(self, table = 'Quiz'):
        client = MongoClient(
            "mongodb+srv://root:nMoiWNI9fZAvAEf2@cluster0.hif69ym.mongodb.net/?retryWrites=true&w=majority")
        self.db = client.get_database('Train_Bot')
        self.table = self.db[table]

    def insert(self, param):
        self.db["Course_Website"].insert_one(param)

db = DBRepository()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST','GET'], )
def submit():
    data = request.form.to_dict()
    data["date"] = datetime.now()
    db.insert(data)
    return redirect('/thankyou.html')


if __name__ == '__main__':
    app.run()