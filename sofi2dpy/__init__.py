"""
sofi2dpy
========

Python tools for preparing, running, and post-processing SOFI2D simulations.

Public API:
    - Configuration I/O
    - Model preprocessing
    - Geometry and output control
    - Visualization
"""

# ---- Configuration ----
from .config import (
    make_default_config as load_config 
)

# ---- Model utilities ----
from .model_utils import (
    read_sgy,
    save_bin,
    resample_model,
    pad_model_to_multiple,
    suggest_domain_decomposition_sofi,
    
)

# ---- Output / geometry ----
from .output_utils import (
    write_source_dat,
    write_receiver_dat,
)

# ---- Plotting ----
from .plot_utils import (
    plot_model,
    plot_model_with_geom,
)

__all__ = [
    # config
    "load_config",
    "save_config",
    "update_basic_params",

    # model
    "read_sgy",
    "save_bin",
    "resample_model",
    "resample_model_iso",
    "recommend_dd",
    "suggest_domain_decomposition",

    # output / geometry
    "write_source_dat",
    "write_receiver_dat",
    "set_sigout",
    "set_snap",

    # plotting
    "plot_model",
    "plot_model_with_geom",
]
