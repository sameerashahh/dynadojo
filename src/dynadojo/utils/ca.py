import cellpylib as cpl
import numpy as np


def plot(datasets: list[np.ndarray], labels: list[str]):
    datasets = [x[0] for x in datasets]
    cpl.plot_multiple(datasets, labels, vmin=0)
