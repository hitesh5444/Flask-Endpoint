from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/output', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET') :
        data = {
            "Subject-Code" : 12456,
            "Subject-Name" : "Python",
        }
        
        return jsonify(data)
    
if __name__ == '__main__' :
    app.run(debug = True)