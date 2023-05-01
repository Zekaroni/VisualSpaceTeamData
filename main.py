from lib.rocketClass import Rocket
from lib.graphWrapper import Graph
from lib.fileHandler import getCSVData
from lib.interpolation import Smooth


def singleRocketPath(file_path,hz=1):
    shuttle = Rocket()
    shuttle.setHertz(hz)
    data = getCSVData(file_path)
    for line in data:
        shuttle.calculatePosition(line)
    return shuttle.getStandAloneXYZ(shuttle._previous_locations)


def main():
    rocketPath = singleRocketPath("sample.csv")
    graph = Graph(amount=2)
    graph.addPlot(2,2,1,rocketPath)
    graph.addPlot(2,2,2,Smooth.cubicSplineInterpolation(rocketPath,subdivisons=2))
    graph.addPlot(2,2,3,rocketPath[:2],projection=None,xlegend="X",ylegend="Y")
    graph.addPlot(2,2,4,[rocketPath[0],rocketPath[2]],projection=None,xlegend="X",ylegend="Z")
    graph.show()


if __name__ == "__main__":
    main()