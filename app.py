from flask import Flask ,render_template , request , redirect
import snapgrap 

app = Flask(__name__)



@app.route('/',methods=['POST','GET'])
def home():
  if request.method.lower() == 'get':
    return render_template('index.html')
  if request.method.lower() == 'post':
    surl = request.form.get('url')
    url = snapgrap.mediaUrlGet(surl)
    return render_template('index.html',Rmode=True,url=url)
@app.route('/url',methods=['POST','GET'])
def index():
  if request.method.lower() == 'get':
    return redirect(home)
  if request.method.lower() == 'post':
    surl = request.form.get('url')
    url = snapgrap.mediaUrlGet(surl)
    return url




if __name__ == '__main__':
  app.run(host='0.0.0.0',port='9090',debug=True)