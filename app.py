from flask import Flask
import userDatabase

uri = "mongodb+srv://rajaramanishwar:VaGhUt2Ej7niI1Rb@stackoverflowers.4ri5c.mongodb.net/"
con=MongoClient(uri,tls=True)
app = Flask(__name__)

@app.route("/")
def home():
  return render_template

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug = True)

@app.route("/login")
def login():
  return render_template('login.html')

user_name=input
if login_password = retrieve_user_data(con,user_name)