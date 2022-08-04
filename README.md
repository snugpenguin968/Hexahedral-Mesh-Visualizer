# Hexahedral-Mesh-Visualizer


## About

Polygon meshes are just a collection of vertices, edges, and faces that make up a 3D object. The concept sounds simple but they are ubiquitous in computer graphics and modeling, finding applications in subjects such as engineering simulations. To contribute to this important field, I am making a site under the guidance of Associate Professor Guoning Chen and PhD Student Lei Si (University of Houston) to visualize the quality of hexahedral meshes. This is a work in progress.

## How to Use

- Download the code and rename the folder to anything of your choice. For demonstration purposes, I have my folder located at the following path: C:\Users\John Tian\MeshVisualizer.
- This project requires the use of Python packages such as Flask, which are accounted for in requirements.txt. Threejs is used to generate the mesh visualizations. The necessary JavaScript packages are already in the static folder.
- Once you have entered the MeshVisualizer directory, run the app.py file as shown below. This should open up a localhost server which you will then navigate to.  
![image](https://user-images.githubusercontent.com/85849926/182731303-031b7d38-56e8-4596-8394-7e0f57328a95.png)
- This is what the site currently looks like: 
![image](https://user-images.githubusercontent.com/85849926/182731510-b563be80-3f5e-40d0-b4a4-61dc20f9cd8a.png)
- There is a basic UI that allows the user to input their own hybrid files. The inputted files must be in the following format: 
  - The 1st line must contain the number of vertices, faces, and polyhedra. 
  - The next n_vertices lines contain 3 space-separated values that represent the x,y, and z coordinates of each vertex. 
  - There are then n_faces lines. Each will first have a number *f* that represents how many vertices make up each face. *f* space separated values follow *f* in the same line. 
  - Finally, there are n_polyhedra lines. Each will first have a number *p* that represents how many faces make up each polyhedra. *p* space separated values follow *p* in the same line. 
  - **See cube_twist.obj.HYBRID or fandisk-comp.obj.HYBRID** as examples. 

## Code Information

-**app.py** sets up the Flask framework. It passes and receives data to and from the frontend and backend. 
- **IO.py** reads in a hybrid file (cube_twist is used as a default) and returns 3 lists representing the vertices, faces, and polyhedra of the file. It also counts the number of pure hexahedral polygons there are in the file. 
- **SplitFaces.py** splits the list of faces into a 3D matrix of edges that can be visualized by Threejs. 
- **templates/index.html** contains all of the HTML, CSS, and JavaScript that renders the meshes. 

