"""
Model utilities for sofi2d-python-tools.

This module provides:
- SGY model I/O
- Binary model export for SOFI2D
- Grid resampling
- Model padding for FD / domain decomposition
- Safe domain decomposition suggestion for SOFI2D
"""

import numpy as np
import obspy
from scipy.interpolate import RegularGridInterpolator


# =============================================================================
# I/O
# =============================================================================

def read_sgy(fname: str) -> np.ndarray:
    """
    Read a 2D SGY model using ObsPy.

    Parameters
    ----------
    fname : str
        Path to SGY file.

    Returns
    -------
    model : ndarray, shape (nx, nz)
    """
    st = obspy.read(fname)
    ntr = len(st)
    npts = st[0].stats.npts

    model = np.zeros((ntr, npts), dtype=np.float32)
    for i, tr in enumerate(st):
        model[i, :] = tr.data.astype(np.float32)

    return model


def save_bin(fname: str, array: np.ndarray):
    """
    Save model to SOFI2D-compatible binary file (float32).

    Parameters
    ----------
    fname : str
        Output filename.
    array : ndarray
        Model array.
    """
    array.astype(np.float32).tofile(fname)


# =============================================================================
# Grid processing
# =============================================================================

def resample_model(
    model: np.ndarray,
    dx: float,
    dz: float,
    dh: float,
) -> np.ndarray:
    """
    Resample a 2D model to a new uniform grid spacing.

    Parameters
    ----------
    model : ndarray (nx, nz)
    dx, dz : float
        Original grid spacing.
    dh : float
        Target grid spacing.

    Returns
    -------
    model_new : ndarray
        Resampled model.
    """
    if dx == dh and dz == dh:
        return model

    nx_old, nz_old = model.shape

    x_old = np.arange(nx_old) * dx
    z_old = np.arange(nz_old) * dz

    nx_new = int(round(x_old[-1] / dh)) + 1
    nz_new = int(round(z_old[-1] / dh)) + 1

    interp = RegularGridInterpolator(
        (x_old, z_old),
        model,
        bounds_error=False,
        fill_value=None,
    )

    Xn, Zn = np.meshgrid(
        np.arange(nx_new) * dh,
        np.arange(nz_new) * dh,
        indexing="ij",
    )

    pts = np.stack([Xn.ravel(), Zn.ravel()], axis=-1)
    model_new = interp(pts).reshape(nx_new, nz_new)

    return model_new


def pad_model_to_multiple(
    *models: np.ndarray,
    multiple: int,
    mode: str = "edge",
):
    """
    Pad one or more 2D models to the same shape,
    where both dimensions are multiples of `multiple`.

    Parameters
    ----------
    models : ndarray(s)
        One or more 2D model arrays with identical shape.
    multiple : int
        Target multiple (e.g. 8, 16, 32).
    mode : str
        Padding mode for np.pad.

    Returns
    -------
    padded_models : ndarray or tuple of ndarray
        If a single model is passed, returns ndarray.
        If multiple models, returns a tuple of ndarrays.
    """
    nx, nz = models[0].shape

    nx_pad = int(np.ceil(nx / multiple) * multiple)
    nz_pad = int(np.ceil(nz / multiple) * multiple)

    pad_x = nx_pad - nx
    pad_z = nz_pad - nz

    pad_left  = pad_x // 2
    pad_right = pad_x - pad_left
    pad_top   = pad_z // 2
    pad_bot   = pad_z - pad_top

    padded = [np.pad(m, ((pad_left, pad_right), (pad_top, pad_bot)), mode=mode)
              for m in models]

    if len(padded) == 1:
        return padded[0]  # 单模型直接返回 ndarray
    else:
        return tuple(padded)  # 多模型返回 tuple


# =============================================================================
# Domain decomposition
# =============================================================================

def suggest_domain_decomposition_sofi(nx, nz, max_cores, fw, fdorder):
    """
    SOFI2D-safe domain decomposition suggestion.

    Parameters
    ----------
    nx, nz : int
        Grid points in x and z directions.
    max_cores : int
        Maximum available MPI cores.
    fw : int
        Boundary width (points).
    fdorder : int
        FD stencil order.

    Returns
    -------
    NPROCX, NPROCY : int
        Number of MPI ranks in x and z directions.
    threads_per_proc : int
        Threads per MPI rank.
    total_procs : int
        Total number of MPI ranks.
    """
    min_block = 2 * fw + 2 * fdorder
    best = (1, 1)
    best_procs = 1

    for nproc in range(1, max_cores + 1):
        for fx in range(1, nproc + 1):
            if nproc % fx != 0:
                continue
            fy = nproc // fx

            # 必须整除
            if nx % fx != 0 or nz % fy != 0:
                continue

            local_nx = nx // fx
            local_nz = nz // fy

            # 子域最小尺寸
            if local_nx < min_block or local_nz < min_block:
                continue

            # 合法方案，选进程数最多的
            if fx * fy > best_procs:
                best = (fx, fy)
                best_procs = fx * fy

    threads_per_proc = max(1, max_cores // best_procs)
    return best[0], best[1], threads_per_proc, best_procs


def pad_model_to_multiple(model, multiple, mode="edge"):
    """
    Pad 2D model to nearest larger multiple.

    Parameters
    ----------
    model : 2D ndarray
        Model array.
    multiple : int
        Target multiple (e.g. 8, 16, 32)
    mode : str
        np.pad mode, recommend "edge"

    Returns
    -------
    padded_model : ndarray
    pad_info : tuple
        (pad_left, pad_right, pad_top, pad_bottom)
    """
    nx, nz = model.shape

    nx_pad = int(np.ceil(nx / multiple) * multiple)
    nz_pad = int(np.ceil(nz / multiple) * multiple)

    pad_x = nx_pad - nx
    pad_z = nz_pad - nz

    pad_left  = pad_x // 2
    pad_right = pad_x - pad_left
    pad_top   = pad_z // 2
    pad_bot   = pad_z - pad_top

    padded = np.pad(
        model,
        ((pad_left, pad_right), (pad_top, pad_bot)),
        mode=mode
    )

    return padded, (pad_left, pad_right, pad_top, pad_bot)