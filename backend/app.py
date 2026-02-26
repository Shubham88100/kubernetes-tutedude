from flask import Flask ,jsonify,render_template
from business import get_data

app=Flask(__name__)

@app.route('/')
def helloworld():
    return render_template("index.html")

@app.route('/api',methods=['GET'])
def api():
    
    data=get_data()
    
    data= {
        'data':data
    }
    
    return jsonify(data)
    

if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0',debug=True)
    
    # Just a note my docker is running on 192.168.0.106 ip in VM ubuntu