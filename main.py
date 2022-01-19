
import math
import matplotlib.pyplot as plt
import numpy as np

List_of_Points = []



def RandomPoint(N):

    for n in range(N):
        j = np.random.uniform(-1,1) #y direction
        i = np.random.uniform(-1,1) #x direction



        List_of_Points.append((i,j))
    print("Number of points = ", N)


def Draw_plot_graph(List,xtitle,ytitle):
    for n in List:
        plt.scatter(n[0], n[1], vmin=0, vmax=100)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.show()

def Draw_hist_graph(Int,xtitle,ytitle):
    plt.hist(Int,bins=100)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)
    plt.show()



#gives avg displacement and a histogram of displacements
def Displacement(List):

    disps_x = []
    disps_y=[]
    for n in List:
        disps_y.append(n[1])
        disps_x.append(n[0])


    Draw_hist_graph(disps_x,"Disp from Origin, x","occurrence")
    Draw_hist_graph(disps_y, "Disp from Origin, y", "occurrence")


    disp_tot = (sum(disps_x),sum(disps_y))
    print("total displacement = ", disp_tot)





#gives length avg and a histogram of lengths
def Length(List):
    lengths = []

    for n in List:
        j = n[1]
        i = n[0]
        length = math.sqrt(i * i + j * j)

        lengths.append(length)

    #Draw_hist_graph(lengths,"Dist from Origin","occurrence")
    length_avg = sum(lengths) / len(lengths)
    print("Average Length = ",length_avg)





RandomPoint(1000000000000000)

Length(List_of_Points)
#Displacement(List_of_Points)
#Draw_plot_graph(List_of_Points,"x","y")
