## 语雀导出的Lake文档转为Markdown文档

> 环境:
> python 3.11
> pip



### 使用方法

生成依赖(使用时可以忽略该步骤)：
```shell script
# 安装
pip install pipreqs
# 在当前目录生成
pipreqs . --encoding=utf8 --force
```

安装依赖：
```shell script
pip install -r requirements.txt
```



1. 导出lakebook文件
   - 具体在  知识库管理->更多功能->导出  中

2. 将下载后的lakebook使用解压软件先解压
   - 7-zip等工具
3. 更改TODO然后运行代码
