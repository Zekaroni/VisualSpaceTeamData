import numpy as np
from scipy.interpolate import CubicSpline

class Smooth:
    def __init__(self):
        pass

    @staticmethod
    def cubicSplineInterpolation(data,subdivisons=1):
        _functions = [] # Initalizes a variable for functions created by CubicSplines
        _sample_amount = len(data[0]) # Creates a varibale for the amount of points there are
        for plane in data:
            # Initalizes CubicSpline functions from the input data
            _functions.append(CubicSpline(range(_sample_amount), plane))

        # Condensed formula of what we worked out on the whitehboard at the meet that one time
        _total_points = (2**subdivisons)*(_sample_amount- 1)+1

        _new_data = []
        _interpolated_points = np.linspace(0, _sample_amount - 1, _total_points)
        # Caluculates new points
        for func in _functions:
            _new_data.append(func(_interpolated_points))
        return _new_data
