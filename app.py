from flask import Flask, request
import urllib.request, json
app = Flask(__name__)
import os

@app.route("/")
def get_movies():
    url = "http://www.omdbapi.com/?i=tt3896198&apikey={}".format("77af47a6")
    print("URL:", url)
    response = urllib.request.urlopen(url)
    data = response.read()
    # print("Response:", response)
    dict = json.loads(data)
    a= request.args.get('type')
    
    return dict[a]

#
# @app.route("/username")
# def login():
#     a = request.args.get('a')
#     print("A:",a)
#     b = request.args.get('b')
#     print("B:",b)
    
    
#     d = str(int(a) / int(b))
#     print("D:", d)
#     return d

# @app.route("/wow")
# def wow():
#     return 'wow!'

if __name__ == '__main__':
    app.run()


