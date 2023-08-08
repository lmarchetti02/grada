import numpy as np
import graph as g
from modules.text import Text

# DATI
x = np.linspace(-5, 5, 50)
y = x**2
y_err = np.full(50, 0.5)

x1 = np.linspace(-5, 5, 50)
y1 = x**3
y1_err = np.full(50, 0.5)
# ---------------------------

text = "text.txt"

# canvas = g.Canvas((12, 8), 150, text, save="prova3")

# scatter = g.ScatterPlot("firebrick", "o", text)
# scatter.draw(canvas, x, y)

# scatter2 = g.ScatterPlot("navy", "o", text)
# scatter2.draw(canvas, x1, y1)

# fit = g.Plot("black", text, ac=(0.01, 0.01))
# fit.draw(canvas, x, lambda x: x**2)

# fit2 = g.Plot("gold", text, ac=(0.01, 0.01))
# fit2.draw(canvas, x1, lambda x: x**3)

# canvas.mainloop(show=True)
