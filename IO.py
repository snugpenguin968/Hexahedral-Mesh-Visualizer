import numpy as np
def read(f):
    with open(f) as file:
        """
        Argument: 
        The name of a Hybrid File. Cube_twist.obj is used as the default. 

        Returns: 
        3 lists representing the vertices, faces, and polyhedra of the file. 
        The vertices list is of shape (number of vertices, 3) as each vertex has an x,y, and z coordinate. 
        The face list is a 2D matrix. Its rows represent each face. Its columns represent the index of a vertex in the vertices list.
        The polyhedra list is a 2D matrix. Its rows represent each polyhedra. Its columns represent the index of a face in the face list.
        """
        n_vertices,n_faces,n_polyhedra=map(int,file.readline().split())
        vertices=[[*map(float,file.readline().split())] for j in range(n_vertices)]
        faces=[[*map(int,file.readline().split())][1:] for j in range(n_faces)]
        polyhedra=[]
        poly_orientation=[]
        for i in range(int(n_polyhedra/3)):
            polyhedra.append([*map(int,file.readline().split())][1:])
            poly_orientation.append([*map(int,file.readline().split())][1:])
        count_hexa=0
        for poly in polyhedra:
            flag=True
            if len(poly)==6:
                for f_i in poly:
                    if len(faces[f_i])!=4:
                        flag=False
                if flag:
                    count_hexa+=1
        return vertices,faces,polyhedra,n_vertices,n_faces,n_polyhedra
