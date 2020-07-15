import matplotlib.pyplot as plt

class Plotting:

    def __init__(self, x_axis, y_axis):
        self._x_axis = x_axis
        self._y_axis = y_axis

        self._figure = plt.figure(figsize = (9, 3))

    def make_plot(self):
        plt.plot(self._x_axis, self._y_axis)
        plt.savefig("plots/test.jpeg")
