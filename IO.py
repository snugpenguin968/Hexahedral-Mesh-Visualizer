
def read(f):
    with open(f) as file:
        n_vertices,n_faces,n_polyhedra=map(int,file.readline().split())
        #print(n_vertices,n_faces,n_polyhedra,flush=True)
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
        
        return vertices,faces,polyhedra
