"""
Output and geometry utilities for sofi2d-python-tools.

This module handles:
- Writing source.dat
- Writing receiver.dat
- Reading receiver.dat
"""

import numpy as np


# =============================================================================
# Source & receiver geometry
# =============================================================================

def write_source_dat(fname: str, sources):
    """
    Write SOFI2D source.dat file.

    Each source is defined as:
        (x, z, td, fc, amp)

    Output format (one source per line):
        XSRC  ZSRC  TD  FC  AMP  SOURCE_AZIMUTH  SOURCE_TYPE

    Notes
    -----
    - Fixed-width columns
    - Space separated (no tabs)
    - No empty lines
    """
    with open(fname, "w") as f:
        for src in sources:
            x, z, td, fc, amp = src
            azimuth = 0.0
            stype = 1

            line = (
                f"{x:10.2f} "
                f"{z:10.2f} "
                f"{td:10.2f} "
                f"{fc:10.2f} "
                f"{amp:10.2f} "
                f"{azimuth:10.2f} "
                f"{stype:10.2f}"
            )
            f.write(line + "\n")


def write_receiver_dat(
    fname: str,
    rec_x: np.ndarray,
    rec_z: np.ndarray,
):
    """
    Write SOFI2D receiver.dat file.

    Parameters
    ----------
    fname : str
        Output filename.
    rec_x, rec_z : ndarray
        Receiver coordinates in meters.
    """
    if len(rec_x) != len(rec_z):
        raise ValueError("rec_x and rec_z must have the same length")

    with open(fname, "w") as f:
        for x, z in zip(rec_x, rec_z):
            f.write(f"{x:.6f} {z:.6f}\n")


def read_receiver_dat(fname: str):
    """
    Read SOFI2D receiver.dat file.

    Parameters
    ----------
    fname : str
        Path to receiver.dat.

    Returns
    -------
    rec_x, rec_z : ndarray
        Receiver coordinates in meters.
    """
    data = np.loadtxt(fname)

    if data.ndim != 2 or data.shape[1] < 2:
        raise ValueError(
            "receiver.dat format error: expected at least two columns (x z)"
        )

    rec_x = data[:, 0]
    rec_z = data[:, 1]

    return rec_x, rec_z
