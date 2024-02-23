# 一个轻量、实用的 FastAPI 项目框架

本项目是一个轻量实用的 FastAPI 项目脚手架，集成了简单的日志，配置文件管理，处理了 python 脚本间的依赖关系，避免重复导入等问题。

项目配置完毕后，你只需要在 src 目录下写代码即可。

本项目是一个脚手架，不是框架，你可以在此基础上进行二次开发，也可以直接使用。

本项目基于以下项目修改：[hansenz42/fastapi-starter: 一个轻量、实用的 FastAPI 项目框架](https://github.com/hansenz42/fastapi-starter)

# 功能

- 集成 fastapi 作为 web 服务器
- 统一返回结构：不论是接口正常还是错误，都会返回统一的 json 消息体
- 错误处理：在接口处理函数中发生的异常，将会自动捕获并返回错误信息
- 依赖管理：使用 miniconda + poetry 管理项目依赖
- 日志管理：统一化日志格式，支持正常日志和错误日志的分割，分别输出到 stdout 和 stderr
- 配置文件管理：根据不同环境加载不同配置文件。
- 测试管理：使用 pytest 管理测试用例。

# 使用方法

## 0 安装 miniconda 实现版本的切换

macOS, Linux, Windows(WSL)：

```bash
wget "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
bash Miniconda3-latest-Linux-x86_64.sh
# 重启计算机
# reboot
# 查看激活版本
conda env list
# 创建 conda 虚拟环境
conda create -n env_name python=3.12
conda create -n -prefix="D:\\my_python\\envs\\my_py_env" env_name python=3.12
# 激活虚拟环境
conda activate env_name
# 退出conda虚拟环境
conda deactivate
# 删除环境
conda remove -n env_name --all
```

## 1 安装 poetry 依赖管理器：

macOS, Linux, Windows(WSL)：

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

其他平台的 poetry 安装方式见：[Introduction | Documentation | Poetry - Python dependency management and packaging made easy](https://python-poetry.org/docs/#installing-with-the-official-installer)

Windows (Powershell)

```sh
# 安装
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
# 卸载
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python - --uninstall

# 配置环境变量
# %APPDATA%\Python\Scripts 加入 path
# 或者
# %APPDATA%\pypoetry\venv\Scripts\poetry 加入 path
poetry --version
```

基本操作：
升级：`poetry self update`
换源：
"""
豆瓣 https://pypi.doubanio.com/simple/
网易 https://mirrors.163.com/pypi/simple/
阿里云 https://mirrors.aliyun.com/pypi/simple/
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
"""
pip 切换安装源:

```sh
pip config set global.index-url https://pypi.doubanio.com/simple/
```

新建或修改配置文件(config.toml):
(该 toml 文件路径是：Linux 系统在~/.config/pypoetry/，Windows 在%APPDATA%\pypoetry\，Mac 在~/Library/Preferences/pypoetry/)

```
[plugins]
[plugins.pypi_mirror]
url = "https://pypi.doubanio.com/simple/"
```

或者？？

```
[[tool.poetry.source]]
name = "aliyun"
url = "http://mirrors.aliyun.com/pypi/simple"
default = true
```

poetry 常用命令

```sh
poetry install # --no-dev 参数以跳过 dev 使用的依赖
poetry add <package> # --dev 参数可以指定为 dev 依赖
poetry env info # 查看虚拟环境信息
poetry env list # 显示虚拟环境所有列表
poetry show --outdated # 查看可以更新的依赖
poetry show # 查看项目安装的依赖
poetry show --tree # 以树形结构查看项目安装的依赖关系
```

conda 结合 poetry：

```sh
# 先全局关闭 poetry 创建虚拟环境
poetry config virtualenvs.create false
poetry config virtualenvs.in-project true

# peotry 使用指定的解释器
# poetry env use C:\ProgramData\miniconda3\envs\py312
conda env list
# 激活虚拟环境
conda activate env_name
# 确认环境
poetry env info

# 使用poetry激活虚拟环境
poetry run python main.py
# 或 poetry shell 激活后直接输入 python main.py
```

## 2 clone 本项目到本地

```bash
git clone git@github.com:hansenz42/python_scaffold.git
```

## 3 （可选）替换 poetry 的 python 版本

修改 pyproject.toml

```toml
[tool.poetry]
name = "PEOJECT NAME"
# ...
authors = ["YOUR NAME <YOUR-EMAIL@xxx.com>"]

[tool.poetry.dependencies]
python = "^3.12"   #替换为你想使用的 python 版本
```

## 4 切换到项目根目录下，安装依赖

```bash
poetry install
```

## 6 添加项目变量

项目变量的配置在 `res` 目录下，默认提供了三个环境：

- `config_dev.yml` 开发环境：在开发时使用
- `config_test.yml` 测试环境：在测试时使用
- `config_prod.yml` 生产环境：在正式环境中使用

变量可以写到对应环境的配置文件中，如开发环境的变量写到， `res/config_dev.yml`。

`config.yml` 文件是所有环境共用的配置，如果在特定环境中配置了相同名称的变量，则会覆盖 `config.yml` 中的配置。

## 7 开始写代码！

- 你自己的代码可以放在 `src` 目录下。
- 测试用例可以统一放在 `test` 目录下。

### 7.1 加入新的路由函数

到 `src/route` 目录下写模版函数，在 `src/app.py` 中引用即可。

```python
# 引入路由函数（你可以在 src/app.py 中找到这个代码）
from route.demo import router as demo_router
app.include_router(demo_router, prefix="/api/v1/demo", tags=["demo"])
```

### 7.2 引入自己写的模块

引入自己编写的模块时，使用 `src` 作为根目录起始的路径，如：

```python
# 例如，在 src/service 目录下写了一个 demo_service.py 文件，在其他文件中引入
# 引入的文件路径不写 src，直接从 service 开始即可
from server.demo_service import foo
```

### 7.3 在代码中引入项目变量

在 `config_xxx.yml` 设置一个项目变量 （xxx 为你要配置的环境）

```yaml
foo:
  bar: "test_paramter"
```

可在代码中使用以下方式引入，yaml 中的层级用字符串列表表示：

```python
# 引入 ConfigManager
from component.ConfigManager import config_manager

# 获取 yaml 中配置的变量 foo.bar
try:
    config_str = config_manager.get_value(['foo', 'bar'])
    # > test_paramter
    print(config_str)
except KeyError:
    # 如未找到该变量，抛出 KeyError 异常
    print('foo.bar 不存在')
```

### 7.4 使用日志

在代码中引入日志：

```python
from component.LogManager import log_manager

# 定义一个 Tag
TAG = 'main'

# 使用 Tag 生成一个 logger
log = log_manager.get_logger(TAG)

# 输出日志
log.debug('debug log')
log.info('info log')
log.warning('warning log')
log.error('error log')
```

debug 和 info level 的日志将输出到 stdout，warning 和 error level 的日志将输出到 stderr。

## 8. 运行

指定运行环境：

1. 环境变量：`PYTHON_SERVICE_ENV` ，如 `PYTHON_SERVICE_ENV=dev poetry run python3 main.py`
2. 命令行实参：如 `poetry run python3 main.py -e dev`

如果程序没有接收到任何参数，或接受了 dev/test/prod 以外的参数，则默认使用 `dev` 环境。

# 高级使用

## 自定义 fastapi 的返回结构

你可以修改 `src/common/response.py` 函数来自定义返回结构。

## 自定义错误处理

错误处理的代码在 `src/app.py` 中，你可以根据自己的需求修改。

## 安装依赖

直接用 poetry 安装，会自动修改 `pyproject.toml` 文件

```bash
poetry add <package-name>
```

## 修改日志打印到控制台的输出 Level

在 res 文件夹中配置各个环境的日志输出等级（可选）

```yaml
# 配置为 info 级别
log_level: info # 支持 debug, info, warning, error, critical 不同等级
```

## 加入更多的运行环境

如果运行环境无法满足你的需求，可以在 `src/common/env.py` 文件中的 `VALID_ENVS` 变量中加入你需要的环境名称。

环境名称加入后，在 `res` 目录下新建一个环境配置文件 yaml

## 写测试

测试文件统一放在 test 目录下，文件名以 `test_` 开头，如 `test_main.py`

# 写在最后

该脚手架是我在写 Python 项目时，为了方便自己管理代码而整理的，如果你有更好的建议，欢迎提 issue 或 PR。

## windows 下强制关闭占用端口

```sh
# 找到与端口相关的 PID
netstat -ano | findstr 8082
# 查找进程名
tasklist | findstr 进程号
# 终止该进程
taskkill /F /PID 9527
```
