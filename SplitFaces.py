from IO import read
def splitFaces(f='cube_twist.obj.HYBRID'):
    """
    Argument: 
    The name of a hybrid file. If none is provided, the cube twist object is used as a default view

    Returns: A 3D matrix with the shape (number of edges,2,3). 
    The 2 represents how each edge must have a start and end vertex. 
    The 3 represents the x,y, and z coordinates of a vertex.
    """

    #Read the input
    vertices,faces,polyhedra=read(f)

    edge_mat=[]
    for face in faces:
        n=len(face)
        for i in range(n):
            edge=[vertices[face[i%n]],vertices[face[(i+1)%n]]]
            edge.sort()
            #Ensure that each edge is unique
            if edge not in edge_mat:
                edge_mat.append(edge)

    return edge_mat
