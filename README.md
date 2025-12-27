# SOFI2D Python Tools

[中文说明 🇨🇳](README_zh.md)

A lightweight Python toolkit for **preprocessing, configuring, running, and post-processing**
[SOFI2D](https://github.com/seismic-ldeo-columbia/sofi2d) simulations, with a focus on  
**elastic 2D modeling** and **reproducible workflows**.

SOFI2D is a powerful finite-difference seismic forward modeling code based on  
**staggered grids** and **cPML absorbing boundary conditions**. It supports a wide range of
wave equations:

- Acoustic isotropic / VTI / TTI  
- Viscoacoustic isotropic / VTI / TTI  
- Elastic isotropic / VTI / TTI  
- Viscoelastic isotropic / VTI / TTI  

However, its traditional Fortran/C-style workflow and parameter handling can be difficult
for beginners and rapid prototyping.

This project provides a **Python-based interface and workflow** to make SOFI2D easier to use,
configure, and reproduce.

---

## Features

This toolkit provides:

- Python-based configuration and automation for SOFI2D
- JSON-driven parameter management
- Model and geometry preprocessing utilities
- Output handling and visualization tools
- Ready-to-run **elastic 2D examples** (SEAM model)
- Reproducible, script-based workflows

---

## Project Structure

```text
sofi2d/
├── sofi2d-pythontools/
│   ├── sofi2dpy/              # Core Python modules
│   │   ├── __init__.py
│   │   ├── config.py          # JSON & parameter configuration
│   │   ├── model_utils.py     # Model reading, resampling, processing
│   │   ├── output_utils.py    # SOFI2D output handling
│   │   └── plot_utils.py      # Visualization utilities
│   │
│   └── examples/
│       └── SEAM_elastic/      # Fully working elastic example
│           ├── Geom/          # Source & receiver geometry
│           ├── SEAM/          # Resampled model files
│           ├── *.sgy          # Original SEAM SGY models
│           ├── example_SEAM.json
│           ├── run_sofi.py    # Main execution script
│           └── output/        # Simulation results
│
├── src/                       # SOFI2D source code
├── bin/                       # SOFI2D executables
├── doc/                       # Documentation
└── examples/                  # Native SOFI2D examples

```

---

## Requirements

- Linux (tested on Ubuntu)
- Python ≥ 3.8
- NumPy
- Matplotlib
- SEG-Y reader (e.g. `obspy` or custom SGY reader)
- Compiled **SOFI2D** executable

> ⚠️ This repository does **not** compile SOFI2D for you.
> Make sure `sofi2d` is built and available before running examples.

---

## Installation
first, you need to install SOFI2D.
1. Clone SOFI2D:
```bash
git clone https://git.scc.kit.edu/GPIAG-Software/SOFI2D.git
```
2. Load Openmpi 3 GCC:
```bash
module load openmpi3/gcc
```
3. Unload the default C compiler:
```bash
module unload gcc
```
4. Compile SOFI2D:
```bash
cd build
make all
```
Clone the repository at the root directory:

```bash
cd sofi2d
git clone https://github.com/zswh10086/sofi2d-pythontools.git
cd sofi2d/sofi2d-pythontools
pip install -e .
```

---
## Quick Start (SEAM Elastic Example)

```bash
cd examples/SEAM_elastic
python run_sofi.py
```

This will:
1. Read SEAM elastic models (Vp, Vs, density)
2. Resample and format them for SOFI2D
3. Generate geometry and parameter files
4. Run SOFI2D
5. Save and visualize outputs

---
## Core Modules

`config.py`
* JSON-based parameter management
* Consistent mapping to SOFI2D input files

`model_utils.py`
* Read SEG-Y models
* Resample models to SOFI2D grid
* Save binary model files

`output_utils.py`
* Handle SOFI2D outputs
* Generate receiver and source files

`plot_utils.py`
* Model visualization
* Shot gathers and wavefield plotting

---
## Author's Notes
    zswh's words

This is a simple Python toolkit for SOFI2D, but it was not a simple task for me.

I am just an undergraduate student, and I am still learning how to write clean and robust code.

This project was created to make SOFI2D easier to use for myself and others, and I will continue to improve it step by step.

If you have any suggestions, improvements, or feedback, I would really appreciate it.

I hope this project can be helpful to someone.

