# 批量打印图片脚本

> v1.0

## 功能

将照片以4张为一组合并，输出到 `output` 文件夹内，然后打印。



## 环境

- windows（打印必须）
- python3

```cmd
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```



## 使用方法

- 打包配置：（如果必要）

```cmd
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
pyinstaller -F -i temp/printer.png run.py
```

打包后将 `dist` 文件夹内的 `run.exe` 文件移到根目录；

- 运行：

1. 将需要打印的照片放在 `buffer` 文件夹内（不需要打印的别放）；
2. 电脑连接打印机；
3. 运行 `python run.py`（或者双击运行 `run.exe`）；
4. 等待运行完毕，照片合并的结果在 output 文件内。



## 参数说明