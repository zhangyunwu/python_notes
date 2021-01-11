# 虚拟环境
虚拟环境是Python解释器的一个私有副本，在这个环境中安装的包不会影响系统中安装的全局Python解释器。

## virtualenv
### 安装
```
pip install virtualenv
```
### 创建虚拟环境
首先选择一个存放虚拟环境的文件夹，在该文件夹下打开命令行
```
virtualenv venv
```
其中`venv`为虚拟环境的名字。

### 进入虚拟环境
```
cd venv
.\Scripts\activate.bat
```
> 个人实测PowerShell无法进入虚拟环境，CMD可以。

### 退出虚拟环境
```
.\Scripts\deactivate.bat
```


[参考链接](https://zhuanlan.zhihu.com/p/60647332)