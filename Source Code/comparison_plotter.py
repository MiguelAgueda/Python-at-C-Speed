"""
Author: Miguel Agueda-Cabral
Date: 15 November 2020
Assignment: CS4100 Term Project - Supplemental Materials
Description: 
    This program executes several implementations of two calculators.
Each implementation is executed and timed. 
After executing each function on the entire dataset, the timing data is graphed using MatPlotLib.
The dataset used in this program is generated at runtime.
"""

import matplotlib.pyplot as plt
from numba import jit
import numpy
import time


def time_it(function, parameter):
    """ Measure `function` total run time in seconds, when passed `parameter`.

    Parameters
    ----------
        function: Function to execute. Should be a process-blocking function.
        parameter: Parameters to pass into `function`.

    Returns
    -------
        run_time: Total run time of `function`, measured in seconds.
    """

    start_time = time.time()  # Time in seconds.
    function(parameter)  # Call blocking function.
    # Get total time elapsed during function call.
    run_time = time.time() - start_time

    return run_time


def plot_it(n_data, np_t_data, py_t_data=None, nb_t_data=None, title=""):
    """ Generate Matplotlib plot to graph results.

    Parameters
    ----------
        NAME_t_data: (2xN) NumPy array containing plot data.
            NAME_t_data[0,m] contains the m^th number of samples.
            NAME_t_data[1,m] contains the m^th total run time in seconds.
                Where `NAME` takes on either `nb`, `np`, or `py` to represent 
                Numba's function, NumPy's function, or a pure Python function, respectively. 
    """

    plt.plot(n_data, np_t_data, 'r', label="NumPy")
    if py_t_data is not None:
        plt.plot(n_data, py_t_data, 'b', label="Python")
    if nb_t_data is not None:
        plt.plot(n_data, nb_t_data, 'g', label="Numba")
    plt.xlabel("number of samples")
    plt.ylabel("run time [s]")
    plt.ticklabel_format(style='plain')
    plt.legend()
    plt.title(title)
    plt.show()


def numpy_find_avg(samples):
    """ NumPy implementation of the Average function."""
    average = numpy.mean(samples)  # Get average using NumPy's `mean` function.
    return average


def python_find_avg(samples):
    """ Python implementation of the Average function."""
    total_sum = 0  # Initialize sum to 0.
    for x in samples:  # Loop over all samples.
        total_sum += x  # Add sample to sum counter.
    count = len(samples)  # Get number of elements in `samples`.
    average = total_sum / count
    return average


@jit  # Numba's JIT decorator.
def numba_find_avg(samples):
    """ Pure Python implementation of the Average function."""

    assert samples is not None, "Samples is None"
    total_sum = 0  # Initialize sum to 0.
    for x in samples:  # Loop over all samples.
        total_sum += x  # Add sample to sum counter.

    count = len(samples)  # Get number of elements in `samples`.
    average = total_sum / count
    return average


def numpy_rms(samples):
    """ NumPy implementation of the Root Mean Squared function."""
    square = numpy.power(samples, 2)
    mean_square = numpy.mean(square)
    rms = numpy.sqrt(mean_square)
    return rms


def python_rms(samples):
    """ Python implementation of the Root Mean Squared function."""
    square_sum = 0  # Initialize counter for sum of squares.
    for x in samples:  # Loop over every sample in list.
        square_sum += (x ** 2)  # Add squared sample to counter.

    # Get total number of samples for average calculation.
    count = len(samples)
    mean_square = square_sum / count  # Compute average of squares.
    rms = mean_square ** 0.5  # Take square root, raise to 1/2 power.

    return rms


@jit  # Numba's JIT decorator.
def numba_rms(samples):
    """ Numba supplemented implementation of the Root Mean Squared function."""
    square_sum = 0  # Initialize counter for sum of squares.
    for x in samples:  # Loop over every sample in list.
        square_sum += (x ** 2)  # Add squared sample to counter.
    # Get total number of samples for average calculation.
    count = len(samples)
    mean_square = square_sum / count  # Compute average of squares.
    rms = mean_square ** 0.5  # Take square root, raise to 1/2 power.

    return rms


# Generate samples for final analysis. Longer load time.
samples = numpy.arange(1, 10, 1e-6)  # Generates ~ 9M samples in range [1, 10].

# Generate samples for testing program. Short load time.
# samples = numpy.arange(1000)  # Generates sequential integer samples [0, 1000].

sample_list = []
n = 20
for i in range(1, n):
    n_samples = int(i * len(samples) / n)
    temp_samples = samples[:n_samples].copy()
    sample_list.append(temp_samples)


# Initialize empty lists to hold resulting timing data.
n_list = []
t_np_avg_list = []
t_np_rms_list = []
t_py_avg_list = []
t_py_rms_list = []
t_nb_avg_list = []
t_nb_rms_list = []

# Loop over sample list, recording time to execute each function.
for sample in sample_list:
    n_list.append(len(sample))
    t_np_avg_list.append(time_it(numpy_find_avg, sample))
    t_py_avg_list.append(time_it(python_find_avg, sample))
    t_nb_avg_list.append(time_it(numba_find_avg, sample))
    t_np_rms_list.append(time_it(numpy_rms, sample))
    t_py_rms_list.append(time_it(python_rms, sample))
    t_nb_rms_list.append(time_it(numba_rms, sample))

# Plot resulting data.
plot_it(n_list, t_np_avg_list, t_py_avg_list,
        title="NumPy and Python 'Average' Computation")
plot_it(n_list, t_np_rms_list, t_py_rms_list,
        title="NumPy and Python 'Root Mean Squared' Computation")
plot_it(n_list, t_np_avg_list, t_py_avg_list, t_nb_avg_list,
        title="Numba, NumPy, and Python 'Average' Computation")
plot_it(n_list, t_np_rms_list, t_py_rms_list, t_nb_rms_list,
        title="Numba, NumPy, and Python 'Root Mean Squared' Computation")
plot_it(n_list, t_np_avg_list, nb_t_data=t_nb_avg_list,
        title="Numba and NumPy 'Average' Computation")
plot_it(n_list, t_np_rms_list, nb_t_data=t_nb_rms_list,
        title="Numba and NumPy 'Root Mean Squared' Computation")
