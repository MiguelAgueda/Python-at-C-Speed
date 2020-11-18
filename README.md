# Python at C-Speed

How can the C and Python programming languages be used, together, to form more efficient software?
Optimizing Python run time performance can be achieved with the following methods;

- [Cython](http://docs.cython.org/en/latest/src/tutorial/cdef_classes.html#extension-types-aka-cdef-classes)

- [Extension Programming](https://docs.python.org/3/extending/extending.html#extending-python-with-c-or-c)

- [Numba](https://numba.readthedocs.io/en/stable/index.html#numba-documentation)

- [NumPy](https://numpy.org/doc/stable/)

Currently, comparisons between pure Python, Numba, and NumPy have been implemented in
[Source Code/comparison_plotter.py](<Source Code/comparison_plotter.py>)

## Running the Demonstration

### Dependencies

To run `comparison_plotter.py`, a few dependencies must first be installed.

The version number may or may not affect the results of the program.
They are included for the reproducibility of experimental results.

- `Python` ver. 3.8.5
- `matplotlib` ver. 3.3.3
- `numba` ver. 0.51.2
- `numpy` ver. 1.17.4

### The Program

To run the Python program, first navigate to this project's root folder.

Next, run the following command to start the program.

```bash
python3 Source\ Code/comparison_plotter.py
```

Alternatively, from the `Source Code` folder, the following command will start the program.

```bash
python3 comparison_plotter.py
```

### Results

Upon completion of all processes, MatPlotLib will generate and display a graph for each process's run time.
Within the MatPlotLib window, the graph can be zoomed in and moved for further analysis.
