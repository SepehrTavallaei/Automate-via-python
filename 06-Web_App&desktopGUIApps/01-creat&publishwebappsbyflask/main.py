from flask import Flask,render_template,request

app = Flask(__name__)

#              added this part after reading line 9
@app.route('/')
def home():
    print("get request string")
    return render_template('index.html')
# till now we hust did a get request but for actually  having interact with the server we need to have a post request like this:
@app.route('/',methods=['POST']) # see the first comment on the index , html file
def home_post():
    dim1 = request.form('first_dim')
    dim2 = request.form('second_dim')
    dim3 = request.form('third_dim')
    volume = float(dim1)*float(dim2)*float(dim3)

    print("get post request")
    return render_template('index.html',output=volume)
app.run() 