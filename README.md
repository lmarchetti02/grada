# GraDA: Graphs for Data Analysis

> A library for rendering beautiful plots of analyzed data: scatter plot with error bars and fit curves.

## Description

This library

## Installation

Follow the steps below to install _grada_:

1. Clone the repository in a directory:

   ```bash
    git clone https://github.com/lmarchetti02/grada
   ```

2. Install `wheel`, `setuptools`, `twine`

   ```bash
    pip3 install wheel
   ```

   ```bash
    pip3 install setuptools
   ```

   ```bash
    pip3 install twine
   ```

3. Build the library by running:

   ```bash
    python3 setup.py bdist_wheel
   ```

   This will create a folder named 'dist' in the working directory, which contains a file
   with '.whl' extension

4. Install the library by running:

   ```bash
   pip install /path/to/wheelfile.whl
   ```

## Usage

For a basic graph, try the following piece of code.

```python
from grada import graphs as g
import numpy as np

# dataset to be drawn
x = np.linspace(-5, 5, 50)
y = x**2
y_err = np.full(50, 0.5)

# log the process
g.Functions.activate_logging()

# create a canvas
canvas = g.Canvas("text.txt", log=True, save="prova")

# create a scatter plot of the data (with error bars)
scatter = ScatterPlot("firebrick", "o")
scatter.draw(canvas, x, y, yerr=y_err)

# create a fit curve
fit = Plot("black", ac=(0.01, 0.01))
fit.draw(canvas, x, lambda x: x**2)

# render the canvas
canvas.mainloop()
```

For information about `matplotlib` colors and marker types see the directory 'info'.

## License

See the [LICENCE](LICENCE) file for licence rights and limitations.
