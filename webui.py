import requests
import gradio as gr

def transcribe_audio_video(file_path, language, model, response_format):
    url = "http://127.0.0.1:9977/api"
    files = {"file": open(file_path.name, "rb")}
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
            return f"Transcription failed: {result.get('msg', 'Unknown error')}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def parse_response(data, response_format):
    if response_format == 'json':
        return str(data)
    elif response_format == 'text':
        if isinstance(data, list):
            return ''.join(item['text'] for item in data)
        elif isinstance(data, str):
            return data
        else:
            raise ValueError(f"Unexpected data type for text format: {type(data)}")
    elif response_format == 'srt':
        if isinstance(data, list):
            srt_content = ""
            for i, item in enumerate(data, start=1):
                srt_content += f"{i}\n{item['start_time']} --> {item['end_time']}\n{item['text']}\n\n"
            return srt_content
        elif isinstance(data, str):
            return data
        else:
            raise ValueError(f"Unexpected data type for srt format: {type(data)}")
    else:
        raise ValueError(f"Unsupported response format: {response_format}")

# Gradio interface
iface = gr.Interface(
    fn=transcribe_audio_video,
    inputs=[
        gr.File(label="unsiao-语音转文字-由unsiao 构建"),
        gr.Radio(["zh", "en", "fr", "de", "ja", "ko", "ru", "es", "th", "it", "pt", "vi", "ar", "tr"], label="Language", value="zh"),
        gr.Dropdown(["tiny","base", "small", "medium", "large-v3"], label="Model", value="base"),
        gr.Radio(["json", "text", "srt"], label="返回格式(默认为json)", value="json")
    ],
    outputs=gr.Textbox(label="Transcription Result"),
    title="Audio/Video Transcription",
    description="上传音频或者视频文件-将会转换为文字内容 由unsiao构建"
)

# Launch the interface
iface.launch()
