from flask import Flask, render_template,request
from IO import read
from SplitFaces import splitFaces
import cgi
import numpy as np
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        #Retrieve user input if available
        input_file=request.form['fileToUpload']
        
        if input_file:
            edge_mat,vertices,faces,polyhedra,n_vertices,n_faces,n_polyhedra=splitFaces(input_file)
    
    else:
        #Use default cube object as the view
        edge_mat,vertices,faces,polyhedra,n_vertices,n_faces,n_polyhedra=splitFaces()
    #Pass python data to javascript
    edge_mat=[edge_mat]
    edge_mat.append(vertices)
    edge_mat.append(faces)
    edge_mat.append(polyhedra)
    return render_template('index.html',name=edge_mat)

if __name__ == "__main__":
    app.run(debug=True)
