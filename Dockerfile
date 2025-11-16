# 使用一个官方的、轻量级的Python 3.11作为基础镜像
FROM python:3.11-slim

# 设置工作目录，之后的所有命令都在这个目录里执行
WORKDIR /app

# 复制依赖文件到工作目录
COPY requirements.txt .

# 安装依赖。--no-cache-dir 参数可以减小镜像体积
RUN pip install --no-cache-dir -r requirements.txt

# 复制所有项目文件到工作目录
COPY . .

# 容器启动时要执行的命令
CMD ["python", "main.py"]
