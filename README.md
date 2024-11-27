# API 接口文档

### 接口地址
```
http://127.0.0.1:9977/api
```

### 请求方法
`POST`

### 请求参数

| 参数            | 描述                          | 可选值                                                                                  |
|-----------------|-------------------------------|-----------------------------------------------------------------------------------------|
| `language`      | 语言代码                       | `zh`（中文）, `en`（英语）, `fr`（法语）, `de`（德语）, `ja`（日语）, `ko`（韩语）<br>`ru`（俄语）, `es`（西班牙语）, `th`（泰语）, `it`（意大利语）<br>`pt`（葡萄牙语）, `vi`（越南语）, `ar`（阿拉伯语）, `tr`（土耳其语）|
| `model`         | 模型名称                       | `base`, `small`, `medium`, `large-v3`                                                     |
| `response_format` | 返回的字幕格式                 | `text`, `json`, `srt`                                                                    |
| `file`          | 音视频文件（二进制上传）        | 音视频文件（二进制数据）                                                                 |

### 示例

#### 请求示例：
```json
{
  "language": "zh",
  "model": "small",
  "response_format": "json",
  "file": "audio_file_binary_data"
}
```

```python
import requests

url = "http://127.0.0.1:9977/api"
files = {'file': open('/path/to/your/audio/file', 'rb')}
data = {
    'language': 'zh',
    'model': 'small',
    'response_format': 'json'
}
response = requests.post(url, files=files, data=data)

print(response.json())  # 打印返回的JSON结果

```
```curl
curl -X POST http://127.0.0.1:9977/api \
  -H "Content-Type: multipart/form-data" \
  -F "language=zh" \
  -F "model=small" \
  -F "response_format=json" \
  -F "file=@/path/to/your/audio/file"
```


Api 请求示例

```python
    import requests
    # 请求地址
    url = "http://127.0.0.1:9977/api"
    # 请求参数  file:音视频文件，language：语言代码，model：模型，response_format:text|json|srt
    # 返回 code==0 成功，其他失败，msg==成功为ok，其他失败原因，data=识别后返回文字
    files = {"file": open("C:/Users/c1/Videos/2.wav", "rb")}
    data={"language":"zh","model":"base","response_format":"json"}
    response = requests.request("POST", url, timeout=600, data=data,files=files)
    print(response.json())
```



# 支持的 返回格式示例！
1. **JSON**
2. **TEXT**
3. **SRT**

### 示例内容

#### 1. JSON 格式
JSON 格式的响应包含一个列表，每个元素是一个字典，包含 `start_time`、`end_time` 和 `text` 字段。

**示例：**
```json
[
    {
        "end_time": "00:00:25,200",
        "line": 1,
        "start_time": "00:00:00,000",
        "text": "从选学的角度来讲,当有一些事上天不让你做成,其实是在保护你,比如车坏了,蓝点了或者你的错过了,这时候我们别生气别抱怨,事件呢,都是有规律,该来的会来,该走的,我们也留不住,有时候得到了规定是好事,失去也不一定是坏事,人间自有英国,残事,机有因素。"
    }
]
```

#### 2. TEXT 格式
TEXT 格式的响应是一个简单的字符串，包含了所有字幕文本。

**示例：**
```
从选学的角度来讲,当有一些事上天不让你做成,其实是在保护你,比如车坏了,蓝点了或者你的错过了,这时候我们别生气别抱怨,事件呢,都是有规律,该来的会来,该走的,我们也留不住,有时候得到了规定是好事,失去也不一定是坏事,人间自有英国,残事,机有因素。
```

#### 3. SRT 格式
SRT 格式的响应是一个符合SRT标准的字幕文件内容。

**示例：**
```
1
00:00:00,000 --> 00:00:25,200
从选学的角度来讲,当有一些事上天不让你做成,其实是在保护你,比如车坏了,蓝点了或者你的错过了,这时候我们别生气别抱怨,事件呢, 都是有规律,该来的会来,该走的,我们也留不住,有时候得到了规定是好事,失去也不一定是坏事,人间自有英国,残事,机有因素。
```



假设我们有一个音频文件 `audio.wav`，并且选择了不同的 `response_format`，下面是每种格式的具体输出示例：

#### JSON 格式
```json
[
    {
        "end_time": "00:00:25,200",
        "line": 1,
        "start_time": "00:00:00,000",
        "text": "从选学的角度来讲,当有一些事上天不让你做成,其实是在保护你,比如车坏了,蓝点了或者你的错过了,这时候我们别生气别抱怨,事件呢,都是有规律,该来的会来,该走的,我们也留不住,有时候得到了规定是好事,失去也不一定是坏事,人间自有英国,残事,机有因素。"
    }
]
```

#### TEXT 格式
```
从选学的角度来讲,当有一些事上天不让你做成,其实是在保护你,比如车坏了,蓝点了或者你的错过了,这时候我们别生气别抱怨,事件呢,都是有规律,该来的会来,该走的,我们也留不住,有时候得到了规定是好事,失去也不一定是坏事,人间自有英国,残事,机有因素。
```

#### SRT 格式
```
1
00:00:00,000 --> 00:00:25,200
从选学的角度来讲,当有一些事上天不让你做成,其实是在保护你,比如车坏了,蓝点了或者你的错过了,这时候我们别生气别抱怨,事件呢, 都是有规律,该来的会来,该走的,我们也留不住,有时候得到了规定是好事,失去也不一定是坏事,人间自有英国,残事,机有因素。
```


# CUDA 加速支持

**安装CUDA工具** [详细安装方法](https://juejin.cn/post/7318704408727519270)

如果你的电脑拥有 Nvidia 显卡，先升级显卡驱动到最新，然后去安装对应的 
   [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)  和  [cudnn for CUDA11.X](https://developer.nvidia.com/rdp/cudnn-archive)。
   
   安装完成成，按`Win + R`,输入 `cmd`然后回车，在弹出的窗口中输入`nvcc --version`,确认有版本信息显示，类似该图
   ![image](https://github.com/jianchang512/pyvideotrans/assets/3378335/e68de07f-4bb1-4fc9-bccd-8f841825915a)

   然后继续输入`nvidia-smi`,确认有输出信息，并且能看到cuda版本号，类似该图
   ![image](https://github.com/jianchang512/pyvideotrans/assets/3378335/71f1d7d3-07f9-4579-b310-39284734006b)

    然后执行 `python testcuda.py`，如果提示成功，说明安装正确，否则请仔细检查重新安装
    
    默认使用 cpu 运算，如果确定使用英伟达显卡，并且配置好了cuda环境，请修改 set.ini 中 `devtype=cpu`为 `devtype=cuda`,并重新启动，可使用cuda加速

# 注意事项

0. 如果没有英伟达显卡或未配置好CUDA环境，不要使用 large/large-v3 模型，可能导致内存耗尽死机
1. 中文在某些情况下会输出繁体字
2. 有时会遇到“cublasxx.dll不存在”的错误，此时需要下载 cuBLAS，然后将dll文件复制到系统目录下，[点击下载 cuBLAS](https://github.com/jianchang512/stt/releases/download/0.0/cuBLAS_win.7z)，解压后将里面的dll文件复制到 C:/Windows/System32下
3. 如果控制台出现"[W:onnxruntime:Default, onnxruntime_pybind_state.cc:1983 onnxruntime::python::CreateInferencePybindStateModule] Init provider bridge failed.", 可忽略，不影响使用
4. 默认使用 cpu 运算，如果确定使用英伟达显卡，并且配置好了cuda环境，请修改 set.ini 中 `devtype=cpu`为 `devtype=cuda`,并重新启动，可使用cuda加速



5. 尚未执行完毕就闪退

如果启用了cuda并且电脑已安装好了cuda环境，但没有手动安装配置过cudnn，那么会出现该问题，去安装和cuda匹配的cudnn。比如你安装了cuda12.3，那么就需要下载cudnn for cuda12.x压缩包，然后解压后里面的3个文件夹复制到cuda安装目录下。具体教程参考 https://juejin.cn/post/7318704408727519270

如果cudnn按照教程安装好了仍闪退，那么极大概率是GPU显存不足，可以改为使用 medium模型，显存不足8G时，尽量避免使用largev-3模型，尤其是视频大于20M时，否则可能显存不足而崩溃

# 相关联项目

[视频翻译配音工具:翻译字幕并配音](https://github.com/jianchang512/pyvideotrans)

[声音克隆工具:用任意音色合成语音](https://github.com/jianchang512/clone-voice)

[人声背景乐分离:极简的人声和背景音乐分离工具，本地化网页操作](https://github.com/jianchang512/vocal-separate)

# 致谢

本项目主要依赖的其他项目

1. https://github.com/SYSTRAN/faster-whisper
2. https://github.com/pallets/flask
3. https://ffmpeg.org/
4. https://layui.dev

