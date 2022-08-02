from IO import read
def splitFaces(f='cube_twist.obj.HYBRID'):
    vertices,faces,polyhedra=read(f)
    edge_mat=[]
    for face in faces:
        n=len(face)
        for i in range(n):
            edge=[vertices[face[i%n]],vertices[face[(i+1)%n]]]
            edge.sort()
            if edge not in edge_mat:
                edge_mat.append(edge)
    #print(len(edge_mat),flush=True)
    return edge_mat
