import matplotlib.pyplot as plt

#plt.scatter(1,2,vmin=0,vmax=100)

ListA=[(0,0),(1,1),(2,2)]
ListB=[0,0,0,0,0,0,1,1.5,3,2,5,1.8,1.99,3.7,2.8,0,0,0,3]

def Draw_plot_graph(List):
    for n in List:
        plt.scatter(n[0], n[1], vmin=0, vmax=100)


def Draw_hist_graph(Int):
    for n in Int:
        plt.hist(n,bins = 2 )

plt.hist(ListB,bins=5)
#Draw_hist_graph(ListB)

plt.show()