# SOFI2D Python Tools

一个轻量级的 Python 工具集，用于 **SOFI2D 的前处理、参数配置、运行控制与后处理**，  
主要面向 **二维弹性波正演** 与 **可复现的数值模拟流程**。

[SOFI2D](https://github.com/seismic-ldeo-columbia/sofi2d) 是一套功能非常强大的有限差分地震正演程序，
采用 **交错网格（staggered grid）** 与 **cPML 吸收边界条件**，支持多种波动方程形式，包括：

- 声学各向同性 / VTI / TTI  
- 粘声学各向同性 / VTI / TTI  
- 弹性各向同性 / VTI / TTI  
- 粘弹性各向同性 / VTI / TTI  

但 SOFI2D 仍然保持着较为“传统”的 Fortran/C 风格输入与工作流，
对初学者而言，上手成本较高，也不利于快速试验与批量自动化。

本项目通过 **Python 工具链** 的方式，对 SOFI2D 的使用流程进行了封装与整理，
使其更易配置、更易复现，也更适合现代科研工作流。

---

## 项目特性

本工具集提供：

- 基于 Python 的 SOFI2D 参数配置与自动化运行
- 基于 JSON 的统一参数管理
- 模型与观测系统（震源 / 检波器）前处理工具
- 输出结果的整理与可视化
- 可直接运行的 **二维弹性波示例（SEAM 模型）**
- 脚本化、可复现的正演流程

---

## 项目结构

```text
sofi2d/
├── sofi2d-pythontools/
│   ├── sofi2dpy/              # Python 核心模块
│   │   ├── __init__.py
│   │   ├── config.py          # JSON 参数管理与配置
│   │   ├── model_utils.py     # 模型读取、重采样与处理
│   │   ├── output_utils.py    # SOFI2D 输出管理
│   │   └── plot_utils.py      # 可视化工具
│   │
│   └── examples/
│       └── SEAM_elastic/      # 完整可运行的弹性波示例
│           ├── Geom/          # 震源与检波器几何
│           ├── SEAM/          # 重采样后的模型文件
│           ├── *.sgy          # 原始 SEAM SEG-Y 模型
│           ├── example_SEAM.json
│           ├── run_sofi.py    # 主运行脚本
│           └── output/        # 模拟输出结果
│
├── src/                       # SOFI2D 源码
├── bin/                       # SOFI2D 可执行文件
├── doc/                       # 官方文档
└── examples/                  # SOFI2D 自带示例
```


## 运行环境要求

- Linux (已在 Ubuntu 上测试)
- Python ≥ 3.8
- NumPy
- Matplotlib
- SEG-Y 读取工具（如 obspy 或自定义 SGY 读取函数）
- 已编译完成的 **SOFI2D 可执行程序**

> ⚠️ 本仓库 **不负责编译 SOFI2D 本体**。
> Make sure `sofi2d` is built and available before running examples.

---

## 安装说明

1. 安装并编译 SOFI2D
克隆 SOFI2D 官方仓库：
```bash
git clone https://git.scc.kit.edu/GPIAG-Software/SOFI2D.git
```
在 HPC 或服务器环境下，加载 MPI 与编译器模块（示例）：
```bash
module load openmpi3/gcc

module unload gcc
```
4. 编译SOFI2D:
```bash
cd build
make all
```
请确保 sofi2d 可执行文件已生成并可被调用。

2. 安装 SOFI2D Python Tools

```bash
cd sofi2d
git clone https://github.com/zswh10086/sofi2d-pythontools.git
cd sofi2d/sofi2d-pythontools
pip install -e .
```

---
## 快速开始：SEAM 弹性波示例

```bash
cd examples/SEAM_elastic
python run_sofi.py
```

该脚本将自动完成以下步骤：
1. 读取 SEAM 弹性模型（Vp、Vs、密度）
2. 重采样并转换为 SOFI2D 所需网格格式
3. 自动生成几何文件与参数文件
4. 调用 SOFI2D 执行正演
5. 保存并可视化模拟结果

---
## 核心模块说明

`config.py`
* 基于 JSON 的参数管理
* 将 Python 参数统一映射到 SOFI2D 输入文件
* 便于参数复现与批量实验

`model_utils.py`
* 读取 SEG-Y 格式模型
* 将模型重采样到 SOFI2D 网格
* 保存为 SOFI2D 可识别的二进制格式

`output_utils.py`
* SOFI2D 输出结果管理
* 生成震源与检波器文件

`plot_utils.py`
* 模型可视化
* 炮集绘制
* 波场快照显示

---
## 作者说明
    zswh 的话

这只是一个针对 SOFI2D 的简单 Python 工具集，但对我来说并不是一件简单的工作。

我目前仍是一名地球物理专业的本科生，还在学习如何编程。
写这个项目的初衷，是希望让 SOFI2D 的使用过程更加清晰、直观，也更适合现代流程，让我能更轻松地复现自己的工作。

如果你对代码结构、功能设计或数值实现有任何建议，欢迎指出。
希望这个项目，能在某些时候对别人有所帮助。

