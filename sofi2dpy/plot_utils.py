"""
plot_utils.py
=============

Visualization utilities for SOFI2D models and outputs.

Coordinate convention:
- Array shape: (nx, nz)
- (0, 0) is the TOP-LEFT corner
- x increases to the right, z increases downward
"""

from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------
# Model plotting
# ----------------------------------------------------------------------

def plot_model(
    arr: np.ndarray,
    title: str,
    outfile: str,
    cmap: str = "jet"
):
    """
    Plot a 2D model array.

    Parameters
    ----------
    arr : np.ndarray
        Model array with shape (nx, nz).
    title : str
        Title and colorbar label.
    outfile : str
        Output image filename.
    cmap : str
        Matplotlib colormap.
    """
    plt.figure(figsize=(8, 4))
    plt.imshow(arr.T, aspect="auto", origin="upper", cmap=cmap)
    plt.colorbar(label=title)
    plt.xlabel("x index")
    plt.ylabel("z index")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()


def plot_model_with_geom(
    arr: np.ndarray,
    dx: float,
    dz: float,
    sources: np.ndarray | list | None = None,
    rec_x: np.ndarray | list | None = None,
    rec_z: np.ndarray | list | None = None,
    title: str = "Model with geometry",
    outfile: str = "model_geom.png",
    cmap: str = "jet"
):
    """
    Plot a model and overlay source/receiver geometry.

    Parameters
    ----------
    arr : np.ndarray
        Model array with shape (nx, nz).
    dx, dz : float
        Grid spacing in x and z (meters).
    sources : array-like, optional
        Source coordinates, shape (Ns, >=2), columns [x, z] in meters.
    rec_x, rec_z : array-like, optional
        Receiver coordinates in meters.
    """
    plt.figure(figsize=(8, 4))
    plt.imshow(arr.T, aspect="auto", origin="upper", cmap=cmap)

    # Sources
    if sources is not None:
        sources = np.asarray(sources)
        xs = sources[:, 0] / dx
        zs = sources[:, 1] / dz
        plt.scatter(xs, zs, c="red", marker="*", s=120, label="Source")

    # Receivers
    if rec_x is not None and rec_z is not None:
        plt.scatter(
            np.asarray(rec_x) / dx,
            np.asarray(rec_z) / dz,
            c="white",
            s=6,
            label="Receiver"
        )

    plt.colorbar(label=title)
    plt.xlabel("x index")
    plt.ylabel("z index")
    plt.title(title)

    if sources is not None or (rec_x is not None and rec_z is not None):
        plt.legend(loc="upper right")

    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()


# ----------------------------------------------------------------------
# Seismogram plotting
# ----------------------------------------------------------------------

def plot_seismogram(
    file_path: str,
    nrec: int,
    dt: float = 0.0015,
    title: str = "Seismogram",
    outfile: str | None = None,
    normalize: bool = False,
    cmap: str = "gray"
):
    """
    Plot a shot gather / seismogram from binary file.

    Parameters
    ----------
    file_path : str
        Path to binary file (float32).
    nrec : int
        Number of receivers.
    dt : float
        Time sampling interval (seconds).
    title : str
        Figure title.
    outfile : str, optional
        Output image filename. If None, use title.
    normalize : bool
        Normalize each trace independently.
    cmap : str
        Colormap.
    """
    data = np.fromfile(file_path, dtype=np.float32)
    if data.size % nrec != 0:
        raise ValueError(
            f"Data size {data.size} not divisible by nrec={nrec}"
        )

    nt = data.size // nrec
    data = data.reshape(nrec, nt)

    if normalize:
        max_amp = np.max(np.abs(data), axis=1)
        max_amp[max_amp == 0.0] = 1.0
        data = data / max_amp[:, None]

    time = np.arange(nt) * dt
    rec = np.arange(nrec)

    plt.figure(figsize=(12, 6))
    plt.imshow(
        data[:, ::-1].T,
        cmap=cmap,
        aspect="auto",
        origin="lower",
        extent=[time[0], time[-1], rec[0], rec[-1]]
    )
    plt.colorbar(label="Amplitude")
    plt.xlabel("Time (s)")
    plt.ylabel("Receiver index")
    plt.title(title + (" (normalized)" if normalize else ""))

    if outfile is None:
        outfile = title.replace(" ", "_") + ".png"

    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()
