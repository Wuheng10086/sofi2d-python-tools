from dataclasses import dataclass
from collections import OrderedDict
from typing import Any
import json


# ============================================================
# Domain decomposition
# ============================================================

@dataclass
class DomainDecomposition:
    """MPI domain decomposition settings."""
    nprocx: int = 1
    nprocy: int = 1

    def to_dict(self):
        return OrderedDict({
            "Domain Decomposition": "comment",
            "NPROCX": str(self.nprocx),
            "NPROCY": str(self.nprocy),
        })


# ============================================================
# Finite-difference order
# ============================================================

@dataclass
class FDOrder:
    """Finite-difference accuracy settings."""
    fdorder: int = 4
    fdorder_time: int = 2
    max_rel_error: float = 0.0

    def to_dict(self):
        return OrderedDict({
            "FD order": "comment",
            "FDORDER": str(self.fdorder),
            "FDORDER_TIME": str(self.fdorder_time),
            "MAXRELERROR": str(self.max_rel_error),
        })


# ============================================================
# Grid definition
# ============================================================

@dataclass
class Grid2D:
    """2D computational grid."""
    nx: int
    ny: int
    dh: float

    def to_dict(self):
        return OrderedDict({
            "2-D Grid": "comment",
            "NX": str(self.nx),
            "NY": str(self.ny),
            "DH": str(self.dh),
        })


# ============================================================
# Time stepping
# ============================================================

@dataclass
class TimeStepping:
    """Time stepping parameters."""
    time: float
    dt: float

    def to_dict(self):
        return OrderedDict({
            "Time Stepping": "comment",
            "TIME": str(self.time),
            "DT": str(self.dt),
        })


# ============================================================
# Wave equation
# ============================================================

@dataclass
class WaveEquation:
    """Wave equation type."""
    weq: str = "EL_ISO"

    def to_dict(self):
        return OrderedDict({
            "Wave Equation": "comment",
            "WEQ": self.weq,
            "WEQ values: AC_ISO, AC_VTI, AC_TTI": "comment",
            "WEQ values: VAC_ISO, VAC_VTI, VAC_TTI": "comment",
            "WEQ values: EL_ISO, EL_VTI, EL_TTI": "comment",
            "WEQ values: VEL_ISO, VEL_VTI, VEL_TTI": "comment",
        })


# ============================================================
# Source definition
# ============================================================

@dataclass
class Source:
    """Source parameters."""
    source_shape: int = 1
    signal_file: str = "signal_mseis.tz"
    source_type: int = 1
    srcrec: int = 1
    source_file: str = "./Geom/source.dat"
    run_multiple_shots: int = 1
    plane_wave_depth: float = 2106.0
    plane_wave_angle: float = 0.0
    ts: float = 0.2

    def to_dict(self):
        return OrderedDict({
            "Source": "comment",
            "SOURCE_SHAPE": str(self.source_shape),
            "SOURCE_SHAPE values: ricker=1, fumue=2, file=3, sin3=4, berlage=5, klauder=6": "comment",
            "SIGNAL_FILE": self.signal_file,
            "SOURCE_TYPE": str(self.source_type),
            "SOURCE_TYPE values: explosive=1, fx=2, fy=3, custom=4": "comment",
            "SRCREC": str(self.srcrec),
            "SRCREC values: read from SOURCE_FILE=1, plane wave=2": "comment",
            "SOURCE_FILE": self.source_file,
            "RUN_MULTIPLE_SHOTS": str(self.run_multiple_shots),
            "PLANE_WAVE_DEPTH": str(self.plane_wave_depth),
            "PLANE_WAVE_ANGLE": str(self.plane_wave_angle),
            "TS": str(self.ts),
        })


# ============================================================
# Source wavelet output
# ============================================================

@dataclass
class Sigout:
    """Source wavelet output settings."""
    sigout: int = 1
    sigout_file: str = "./OUTPUT/shot"
    sigout_format: int = 3

    def to_dict(self):
        return OrderedDict({
            "SIGOUT": str(self.sigout),
            "Output source wavelet: yes=1, no=else": "comment",
            "SIGOUT_FILE": self.sigout_file,
            "SIGOUT_FORMAT": str(self.sigout_format),
            "Supported formats: SU=1, ASCII=2, BINARY=3": "comment",
        })


# ============================================================
# Model
# ============================================================

@dataclass
class Model:
    """Velocity and density model settings."""
    readmod: int = 1
    mfile: str = "./model/SEAM"
    write_modelfiles: int = 0

    def to_dict(self):
        return OrderedDict({
            "Model": "comment",
            "READMOD": str(self.readmod),
            "MFILE": self.mfile,
            "WRITE_MODELFILES": str(self.write_modelfiles),
        })


# ============================================================
# Q approximation
# ============================================================

@dataclass
class QApproximation:
    """Viscoelastic Q approximation."""
    L: int = 0
    f_ref: float = 50.0
    fl1: float = 50.0

    def to_dict(self):
        return OrderedDict({
            "Q-approximation": "comment",
            "L": str(self.L),
            "F_REF": str(self.f_ref),
            "FL1": str(self.fl1),
        })


# ============================================================
# Boundary conditions
# ============================================================

@dataclass
class Boundary:
    """Boundary and absorbing layer settings."""
    free_surf: int = 1
    boundary: int = 0
    fw: int = 40
    abs_type: int = 1
    npower: float = 4.0
    k_max_cpml: float = 1.0
    vppml: float = 4800.0
    fpml: float = 30.0
    damping: float = 8.0

    def to_dict(self):
        return OrderedDict({
            "Boundary": "comment",
            "FREE_SURF": str(self.free_surf),
            "BOUNDARY": str(self.boundary),
            "FW": str(self.fw),
            "ABS_TYPE": str(self.abs_type),
            "ABS_TYPE values: CPML=1, damping=2": "comment",
            "CPML parameters": "comment",
            "NPOWER": str(self.npower),
            "K_MAX_CPML": str(self.k_max_cpml),
            "VPPML": str(self.vppml),
            "FPML": str(self.fpml),
            "Damping boundary parameters": "comment",
            "DAMPING": str(self.damping),
        })


# ============================================================
# Snapshots
# ============================================================

@dataclass
class Snapshots:
    """Wavefield snapshot output."""
    snap: int = 1
    tsnap1: float = 0.0
    tsnap2: float = 0.0
    tsnapinc: float = 0.04
    idx: int = 1
    idy: int = 1
    snap_format: int = 3
    snap_file: str = "./OUTPUT/snap"

    def to_dict(self):
        return OrderedDict({
            "Snapshots": "comment",
            "SNAP": str(self.snap),
            "TSNAP1": f"{self.tsnap1:.6f}",
            "TSNAP2": f"{self.tsnap2:.6f}",
            "TSNAPINC": f"{self.tsnapinc:.6f}",
            "IDX": str(self.idx),
            "IDY": str(self.idy),
            "SNAP_FORMAT": str(self.snap_format),
            "SNAP_FILE": self.snap_file,
        })


# ============================================================
# Receiver
# ============================================================

@dataclass
class Receiver:
    """Receiver geometry and recording options."""
    seismo: int = 4
    readrec: int = 1
    rec_file: str = "./Geom/receiver.dat"
    refrec: str = "0.0 , 0.0"
    rec1: str = "100.0 , 15.0"
    rec2: str = "21850.0 , 1.0"
    ngeoph: int = 120
    rec_array: int = 0
    rec_array_depth: float = 70.0
    rec_array_dist: float = 40.0
    drx: int = 4

    def to_dict(self):
        return OrderedDict({
            "Receiver": "comment",
            "SEISMO": str(self.seismo),
            "READREC": str(self.readrec),
            "REC_FILE": self.rec_file,
            "REFRECX, REFRECY": self.refrec,
            "XREC1,YREC1": self.rec1,
            "XREC2,YREC2": self.rec2,
            "NGEOPH": str(self.ngeoph),
            "Receiver array": "comment",
            "REC_ARRAY": str(self.rec_array),
            "REC_ARRAY_DEPTH": str(self.rec_array_depth),
            "REC_ARRAY_DIST": str(self.rec_array_dist),
            "DRX": str(self.drx),
        })


# ============================================================
# Seismograms
# ============================================================

@dataclass
class Seismograms:
    """Seismogram output settings."""
    ndt: int = 10
    seis_format: int = 3
    seis_file: str = "./OUTPUT/seis"

    def to_dict(self):
        return OrderedDict({
            "Seismograms": "comment",
            "NDT": str(self.ndt),
            "SEIS_FORMAT": str(self.seis_format),
            "SEIS_FILE": self.seis_file,
        })


# ============================================================
# Logging
# ============================================================

@dataclass
class Logging:
    """Runtime logging options."""
    log_file: str = "./log/sofi2d.log"
    log: int = 0
    log_verbosity: str = "INFO"
    out_timestep_info: int = 100

    def to_dict(self):
        return OrderedDict({
            "Monitoring the simulation": "comment",
            "LOG_FILE": self.log_file,
            "LOG": str(self.log),
            "LOG_VERBOSITY": self.log_verbosity,
            "OUT_TIMESTEP_INFO": str(self.out_timestep_info),
        })


# ============================================================
# Top-level configuration
# ============================================================

@dataclass
class Sofi2DConfig:
    domain: DomainDecomposition
    fd: FDOrder
    grid: Grid2D
    time: TimeStepping
    weq: WaveEquation
    source: Source
    sigout: Sigout
    model: Model
    q: QApproximation
    boundary: Boundary
    snapshots: Snapshots
    receiver: Receiver
    seismograms: Seismograms
    logging: Logging

    def to_ordered_json(self) -> OrderedDict:
        cfg = OrderedDict()
        for block in (
            self.domain,
            self.fd,
            self.grid,
            self.time,
            self.weq,
            self.source,
            self.model,
            self.q,
            self.boundary,
            self.snapshots,
            self.receiver,
            self.seismograms,
            self.logging,
        ):
            cfg.update(block.to_dict())
        return cfg

    def dump(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                self.to_ordered_json(),
                f,
                indent=2,
                ensure_ascii=False
            )


# ============================================================
# Factory
# ============================================================

def make_default_config(nx: int, ny: int, dh: float) -> Sofi2DConfig:
    """
    Factory function to create a complete Sofi2DConfig with sane defaults.
    Grid parameters (nx, ny, dh) are mandatory.
    """
    return Sofi2DConfig(
        domain=DomainDecomposition(),
        fd=FDOrder(),
        grid=Grid2D(nx=nx, ny=ny, dh=dh),
        time=TimeStepping(time=2.0, dt=0.001),
        weq=WaveEquation(),
        source=Source(),
        sigout=Sigout(),
        model=Model(),
        q=QApproximation(),
        boundary=Boundary(),
        snapshots=Snapshots(),
        receiver=Receiver(),
        seismograms=Seismograms(),
        logging=Logging(),
    )
