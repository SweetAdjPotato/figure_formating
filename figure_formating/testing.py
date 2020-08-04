
import numpy as np
from FormatPlot import FormatPlot
x = np.arange(0, 10, 0.1)
y = np.sin(x)
FormatPlot.plot(x,y)

x1 = np.random.rand(100,1)
FormatPlot.hist(x1)


FormatPlot.bar(x,y)
