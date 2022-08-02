from flask import Flask, render_template,request
from IO import read
from SplitFaces import splitFaces
import cgi
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        input_file=request.form['fileToUpload']
        
        if input_file:
            
            edge_mat=splitFaces(input_file)
           
    else:
        edge_mat=splitFaces()
    #print(edge_mat,flush=True)
    return render_template('index.html',name=edge_mat)

if __name__ == "__main__":
    app.run(debug=True)
