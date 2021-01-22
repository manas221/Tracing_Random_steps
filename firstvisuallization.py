import matplotlib.pyplot as plt
from Randomwalks_makingclass import Randomwalk

inp = int(input("Enter choice for different uses of Randomwalk : "))
if (inp == 1):
    rw = Randomwalk()
    rw.fill_walk()
    plt.scatter(rw.x_values ,rw.y_values ,s =15)
    plt.show()

elif (inp == 2):
    #keep making new walks as long as the program is active
    while True:
        rw = Randomwalk()
        rw.fill_walk()
        plt.scatter(rw.x_values ,rw.y_values ,s =15)
        plt.show()

        ask = input("Enter y to keep going or n to quit : ")
        if (ask == 'n'):
            break

elif (inp == 3):
    # Coloring the points using colormap attribute of scatter function
    rw = Randomwalk()
    rw.fill_walk()  #now the points are filled in the class variable
    p_nums = list(range(rw.num_points))
    plt.scatter(rw.x_values ,rw.y_values ,c = p_nums ,cmap = plt.cm.Blues ,edgecolor='none' ,s = 15)
    plt.show()