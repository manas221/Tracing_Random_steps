from random import choice

class Randomwalk():
    # a class to generate random walks in a plane
    def __init__(self ,num_points = 5000):
        self.num_points = num_points
        # all walks start from (0 ,0)
        self.x_values = [0] #holds the x value of step
        self.y_values = [0] #holds the y value of step

    def fill_walk(self):
        # calculates the steps
        while(len(self.x_values) < self.num_points):
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])    #just read the code, it's intuitive enough to understand
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])    #just read the code, it's intuitive enough to understand
            y_step = y_direction * y_distance

            #if there is no change in coordinates, reject that sequence
            if x_step == 0 and y_step == 0:
                continue
            
            #and since ,this is a walk ,each new coordinate is added to previous(last item in list) to get the final co-ordinate
            next_x = x_step + self.x_values[-1]
            next_y = y_step + self.y_values[-1]

            self.x_values.append(next_x)
            self.y_values.append(next_y)