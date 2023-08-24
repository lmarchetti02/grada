from grada import graphs as g
import numpy as np

# disable logging
g.Functions.activate_logging(status=False)


def test_addensa_equal_elements():
    _ = np.array([-5, -2, 0, 1, 1, 4, 6])
    res = g.Functions.addensa(_)

    assert np.array_equal(_, res)


def test_addensa():
    _ = np.linspace(-5, 5, num=20)
    res = g.Functions.addensa(_)

    assert len(res) > len(_)


def test_allarga_campo_extremes():
    _ = np.array([-5, -2, 0, 1, 4, 6])
    res = g.Functions.allarga_campo(_, 0, 0)

    assert res[0] == _[0] and res[-1] == _[-1]

    res = g.Functions.allarga_campo(_, 0, 0.1)

    assert res[0] != res[1]

    res = g.Functions.allarga_campo(_, 0.1, 0)

    assert res[-1] != res[-2]


def test_allarga_campo():
    _ = np.array([-5, -2, 0, 1, 4, 6])
    res = g.Functions.allarga_campo(_, 0.1, 0.2)

    assert len(res) > len(_) and res[0] < _[0] and res[-1] > _[-1]


# # DATI
# x = np.linspace(-5, 5, 50)
# y = x**2
# y_err = np.full(50, 0.5)

# x1 = np.linspace(-3, 3, 30)
# y1 = x1**3
# y1_err = np.full(30, 0.5)
# # ---------------------------

# g.Functions.activate_logging()

# canvas = g.Canvas("text.txt", log=True, save="prova")

# scatter = g.ScatterPlot("firebrick", "o")
# scatter.draw(canvas, x, y)

# scatter2 = g.ScatterPlot("navy", "o")
# scatter2.draw(canvas, x1, y1)

# fit = g.Plot("black", ac=(0.01, 0.01))
# fit.draw(canvas, x, lambda x: x**2)

# fit2 = g.Plot("gold", ac=(0.01, 0.01))
# fit2.draw(canvas, x1, lambda x: x**3)

# canvas.mainloop(show=False)
