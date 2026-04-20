![Language](https://img.shields.io/badge/language-Python-blue) ![License](https://img.shields.io/badge/license-MIT-green)

# demo-Python-BCI-Experiment-Scripts

**SSVEP / FBCCA 脑机接口实验用脚本集合，包含滤波器组、刺激呈现与机器人控制示例。**

## 功能特性

- FBCCA（滤波器组典型相关分析）频率识别
- 刺激序列生成与呈现（stim.py）
- EEG 数据读取与实时处理
- TCP 客户端机器人控制接口
- 轻量脚本，适合快速实验验证

## 快速开始

### 环境要求

- Python >= 3.8
- numpy, scipy, matplotlib, pyserial

### 安装步骤

```bash
git clone https://github.com/joeeei11/demo-Python-BCI-Experiment-Scripts.git
cd demo-Python-BCI-Experiment-Scripts
pip install numpy scipy matplotlib pyserial
```

### 基础用法

```bash
python fbcca.py   # FBCCA 频率识别
python stim.py    # 启动刺激程序
```
