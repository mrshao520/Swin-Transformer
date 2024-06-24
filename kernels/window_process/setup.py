from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

# 定义setup函数，这是用于安装包的主要入口点
setup(name='swin_window_process', # 包的名称
    ext_modules=[ # 外部模块列表，这里定义了一个CUDA扩展
        CUDAExtension('swin_window_process', [ # 扩展的名称和源文件
            'swin_window_process.cpp', # C++源文件
            'swin_window_process_kernel.cu', # CUDA核函数源文件
        ])
    ],
    cmdclass={'build_ext': BuildExtension}) # 命令类，用于构建扩展