import matplotlib.pyplot as _plt

class Graph:
    def __init__(self, amount = 1):
        self.figure = _plt.figure(figsize=(_plt.figaspect(1/amount)))
        self._subplots = []
    
    def addPlot(self, nrows, ncols, index, data, title=None, xlegend = None, ylegend = None, grid = False,projection = "3d"):
        _plot = self.figure.add_subplot(nrows, ncols, index, projection=projection)
        _plot.set_label(title)
        _plot.set_xlabel(xlegend)
        _plot.set_ylabel(ylegend)
        _plot.grid()
        _plot.plot(*data)

    def show(self):
        _plt.show()