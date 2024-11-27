import os
import requests
import gradio as gr

def transcribe_audio_video(file_path, language, model, response_format):
    """
    发送音频或视频文件到API进行转录。
    
    参数:
    - file_path: 文件路径
    - language: 转录的语言
    - model: 使用的模型
    - response_format: 返回的结果格式
    
    返回:
    - 处理后的转录结果
    """
    url = "http://127.0.0.1:9977/api"
    files = {"file": open(file_path, "rb")}
    data = {
        "language": language,
        "model": model,
        "response_format": response_format
    }
    
    try:
        response = requests.post(url, timeout=600, data=data, files=files)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        result = response.json()
        
        if result['code'] == 0:
            return parse_response(result['data'], response_format)
        else:
            return f"转录失败: {result.get('msg', '未知错误')}"
    except requests.exceptions.RequestException as e:
        return f"发生错误: {e}"

def parse_response(data, response_format):
    """
    解析API返回的数据。
    
    参数:
    - data: API返回的数据
    - response_format: 返回的结果格式
    
    返回:
    - 格式化后的结果字符串
    """
    if response_format == 'json':
        return str(data)
    elif response_format == 'text':
        if isinstance(data, list):
            return ''.join(item['text'] for item in data)
        elif isinstance(data, str):
            return data
        else:
            raise ValueError(f"不支持的文本格式数据类型: {type(data)}")
    elif response_format == 'srt':
        if isinstance(data, list):
            srt_content = ""
            for i, item in enumerate(data, start=1):
                srt_content += f"{i}\n{item['start_time']} --> {item['end_time']}\n{item['text']}\n\n"
            return srt_content
        elif isinstance(data, str):
            return data
        else:
            raise ValueError(f"不支持的SRT格式数据类型: {type(data)}")
    else:
        raise ValueError(f"不支持的返回格式: {response_format}")

def process_folder(folder_path, language, model, response_format):
    """
    处理指定文件夹中的所有音频和视频文件，并将结果保存到一个文件中。
    
    参数:
    - folder_path: 文件夹路径
    - language: 转录的语言
    - model: 使用的模型
    - response_format: 返回的结果格式
    
    返回:
    - 处理结果的汇总字符串
    """
    supported_extensions = ('.mp3', '.wav', '.mp4', '.avi')
    output_dir = "./output/"
    output_file_path = os.path.join(output_dir, "transcription_results.txt")
    
    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    results = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(supported_extensions):
                file_path = os.path.join(root, file)
                result = transcribe_audio_video(file_path, language, model, response_format)
                if result.strip():  # 只添加非空结果
                    results.append(result)
    
    # 将所有结果合并并保存到一个文件中，每个结果之间用三个换行符分隔
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write("\n\n\n".join(results))
    
    # 读取并返回输出文件的内容
    with open(output_file_path, "r", encoding="utf-8") as output_file:
        final_output = output_file.read()
    
    return final_output

# Gradio界面配置
iface = gr.Interface(
    fn=process_folder,
    inputs=[
        gr.Textbox(label="文件夹路径 (例如: C:\\Users\\unsia\\Music\\Playlists)"),
        gr.Radio(["zh", "en", "fr", "de", "ja", "ko", "ru", "es", "th", "it", "pt", "vi", "ar", "tr"], label="语言", value="zh"),
        gr.Dropdown(["tiny","base", "small", "medium", "large-v3"], label="模型", value="base"),
        gr.Radio(["json", "text", "srt"], label="返回格式(默认为json)", value="json")
    ],
    outputs=gr.Textbox(label="转录结果"),
    title="音频/视频转录工具",
    description="上传音频或视频文件-将会转换为文字内容 或者 输入文件夹路径批量处理 文件由unsiao构建"
)

# 启动Gradio界面
iface.launch()



