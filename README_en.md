<div align="center">
  <img src="Assets/svg/FunGPT-logo.svg" width="100"/>

  [📘Documentation](https://github.com/Alannikos/FunGPT) |
  [🛠️Quick Start](https://github.com/Alannikos/FunGPT) |
  [🤔Reporting Issues](https://github.com/Alannikos/FunGPT/issues) 

  [English](README_en.md) | [简体中文](README_zh.md)
</div>

<div align="center">

<!-- PROJECT SHIELDS -->
[![GitHub Issues](https://img.shields.io/github/issues/Alannikos/FunGPT?style=flat&logo=github&color=%23FF5252)](https://github.com/Alannikos/FunGPT/issues)
[![GitHub forks](https://img.shields.io/github/forks/Alannikos/FunGPT?style=flat&logo=github&color=%23FF9800)](https://github.com/Alannikos/FunGPT/forks)
![GitHub Repo stars](https://img.shields.io/github/stars/Alannikos/FunGPT?style=flat&logo=github&color=%23FFEB3B)
![GitHub License](https://img.shields.io/github/license/Alannikos/FunGPT?style=flat&logo=github&color=%234CAF50)
[![Discord](https://img.shields.io/discord/1308061124419260446?style=flat&logo=discord)](https://discord.com/channels/1308061124419260446/)
[![TODO](https://img.shields.io/badge/update%20-todo-blue)](https://github.com/Alannikos/FunGPT)
[![Bilibili](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.bilibili.com%2Fx%2Frelation%2Fstat%3Fvmid%3D3494365446015137&query=%24.data.follower&style=flat&logo=bilibili&label=followers&color=%23FF69B4)](https://space.bilibili.com/3494365446015137)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97Hugging%20Face-Models-yellow)](https://huggingface.co/Alannikos768/BoostBot_1_8b-chat)
[![OpenXLab_Model](https://cdn-static.openxlab.org.cn/header/openxlab_models.svg)](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-7b-chat)
</div>

_____________________________________________________________________


# Latest News 🎉

<details open>
<summary><b>2024</b></summary>

- \[2025/05/29\] 🛠️🎯 Fixed some path-related bugs[fix](https://github.com/Alannikos/FunGPT/commit/b1e25f7addebd91d8ec031a013403365ad495c94)
- \[2024/11/30\] 📢📺 We've released a project introduction video! You can find the video on [Bilibili](https://www.bilibili.com/video/BV1EGBYYtEMA/). If you like it, don't forget to give it a thumbs up 👍 and follow us!
- \[2024/11/19\] 🔒🛡️ Incorporate a sensitive word processing module to prevent the model from outputting harmful viewpoints.
- [2024/11/18] 🔧🌟 Completed **Quick Start** section documentation updates and resolved environment setup bugs.
- [2024/11/14] 🎉✨ Successfully quantized four models using the LMDeploy tool. The FunGPT family welcomes new members! Models are now available on [HuggingFace](https://huggingface.co/Alannikos768).
- [2024/11/13] 🎉✨ Released two new 1.8B models, expanding the FunGPT family! The models are [BanterBot_1_8b-chat](https://huggingface.co/Alannikos768/BanterBot_1_8b-chat) and [BoostBot_1_8b-chat](https://huggingface.co/Alannikos768/BoostBot_1_8b-chat).
- [2024/11/10] 🎉✨ Launched two brand-new 7B models, adding new members to the FunGPT family! The models are [BanterBot-7b-chat](https://huggingface.co/Alannikos768/BanterBot-7b-chat) and [BoostBot-7b-chat](https://huggingface.co/Alannikos768/BoostBot-7b-chat).
- [2024/11/10] 🛠️🎯 Major project updates completed, including fixing known absolute path bugs.
- [2024/10/28] 🎈🥳 Achieved fine-tuning large language models using xtuner and released the first version of [BoostBot_v1](https://huggingface.co/Alannikos768/Kua_LLM)!
- [2024/10/19] 🎉💬 Developed a toolchain to generate fine-tuned dialogue data using the Chat-GLM4 series.
- [2024/10/03] 🎨🐞 Beautified the system interface and fixed some known bugs.
- [2024/10/02] 🚀💻 Added model loading and unloading mechanisms to optimize GPU memory usage.
- [2024/10/01] 😄🐍 Integrated an exception handling module to enhance application stability.
- [2024/09/28] 👋👋 Completed initial testing and evaluation of individual functionalities for LLM ([InternLM2.5_1.8b](https://huggingface.co/internlm/internlm2_5-1_8b-chat)), ASR ([Sensevoice](https://www.modelscope.cn/models/iic/sensevoicesmall)), and TTS ([ChatTTS](https://huggingface.co/2Noise/ChatTTS)).

</details>

_____________________________________________________________________


# 🌟 Project Introduction

$\quad$ In this fast-paced world 🌍, we all need a little spice to balance our lives. Whether you’re looking for some **sweet compliments** 🍭 to lift your spirits ✨ or a dose of **sharp retorts** 💥 to blow off steam 😤, **FunGPT**, developed based on the InternLM2.5 series models 🤖, is here to meet your needs 🎯!

🍬 Sweet Compliment Mode:

- **Mood Booster 🌟✨**: When you’re feeling down, our Sweet Compliment Mode will instantly lift your spirits, just like tasting an incredibly sweet candy.
- **Confidence Fuel Station 💪🌈**: Meanwhile, our **Praise Master** will compliment you in the most suitable and unique ways, making your confidence soar.

🔪 Sharp Retort Mode:

- **Stress Release Valve 💥😤**: When you’re feeling overwhelmed, our Retort Mode provides an outlet to blow off steam while delivering sharp remarks.
- **Humorous Roasting Machine 😂👅**: The words of the **Roast Master** are not only sharp but also humorous and imaginative, letting you experience brain-twisting comebacks while having fun.

_____________________________________________________________________

# 🤔 Project Highlights

$\quad$**FunGPT** is built on the cutting-edge InternLM2.5 series models. Using [Xtuner](https://github.com/InternLM/xtuner), we performed both instruction and full fine-tuning, enabling the models to meet personalized user needs. To enhance accessibility, we released the 1.8B series of lightweight models, which deliver exceptional performance despite their reduced size. Additionally, we employed **AWQ quantization** using LMDeploy on multiple models, saving GPU memory while boosting inference speed! ⚡

$\quad$ This project caters to every users by focusing on the two scenarios of praise and roasting, allowing users to chat with our two "Masters" to regulate their moods. For developers just entering the world of LLMs, we provide extensive documentation and video tutorials covering LLM, ASR, and TTS, making this project an ideal entry point for mastering large model development skills.

$\quad$ Our advantages include, but are not limited to:

1. 🤗 **Master of Compliments**: Generate sweet words to brighten your daily life.
2. 🗯️ **Roasting Expert**: Tailored responses with sharp wit, engaging in a battle of wits with "me."
3. 📊 **Data Collection Guide**: Fully open-source, helping you quickly grasp the creation of fine-tuning datasets.
4. 📖 **Complete LLM Workflow Guide**: Comprehensive code and documentation, open-source, making it easy to get started.
5. 🔊 **Complete ASR Workflow Guide**: Open everything to help you realize your dream of speech recognition.
6. 🎙️ **Complete TTS Workflow Guide**: From basics to advanced, fully open-source with no reservations!
7. 📂 **Clear Structure**: Detailed annotations and documentation ensure seamless onboarding.
8. ⚡ **Model Quantization**: Lower the usage barrier and experience the magic of AI anytime, anywhere.
9. 🎥 **Video Tutorials**: Stay tuned for our complete project introduction videos!

# 🖼️ Screenshots

|Original_7b_BoostBot|BoostBot-7b|
|:---:|:---:|
|<img src="./Assets/gif/Original_7b_BoostBot.gif" width="400">|<img src="./Assets/gif/BoostBot-7b.gif" width="400">|

|Original_7b_BanterBot|BanterBot-7b|
|:---:|:---:|
|<img src="./Assets/gif/Original_7b_BanterBot.gif" width="400">|<img src="./Assets/gif/BanterBot-7b.gif" width="400">|

# 🏗️ Project Architecture Diagram

![Project Architecture Diagram](Docs/pictures/FunGPT.png)



# 🧳 Model Collection

| Model                          | Base                  | Type                       | Link                                                          |
| ------------------------------ | --------------------- | -------------------------- | ------------------------------------------------------------ |
| BanterBot-7b-chat              | internlm2_5_chat_7b   | Pre-trained + QLoRA fine-tuning | [HuggingFace](https://huggingface.co/Alannikos768/BanterBot-7b-chat)<br/>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-7b-chat) |
| BoostBot-7b-chat               | internlm2_5_chat_7b   | Pre-trained + QLoRA fine-tuning | [HuggingFace](https://huggingface.co/Alannikos768/BoostBot-7b-chat)<br/>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-7b-chat) |
| BanterBot_1_8b-chat            | internlm2_5_chat_1_8b | Pre-trained + QLoRA fine-tuning | [HuggingFace](https://huggingface.co/Alannikos768/BanterBot_1_8b-chat)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-1_8b-chat) |
| BoostBot_1_8b-chat             | internlm2_5_chat_1_8b | Pre-trained + QLoRA fine-tuning | [HuggingFace](https://huggingface.co/Alannikos768/BoostBot_1_8b-chat)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-1_8b-chat) |
| BanterBot-7b-chat-w4a16-4bit   | internlm2_5_chat_7b   | Pre-trained + QLoRA fine-tuning + w4a16 quantization | [HuggingFace](https://huggingface.co/Alannikos768/BanterBot-7b-chat-w4a16-4bit)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-7b-chat-w4a16-4bit) |
| BoostBot-7b-chat-w4a16-4bit    | internlm2_5_chat_7b   | Pre-trained + QLoRA fine-tuning + w4a16 quantization | [HuggingFace](https://huggingface.co/Alannikos768/BoostBot-7b-chat-w4a16-4bit)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-7b-chat-w4a16-4bit) |
| BanterBot_1_8b-chat-w4a16-4bit | internlm2_5_chat_1_8b | Pre-trained + QLoRA fine-tuning + w4a16 quantization | [HuggingFace](https://huggingface.co/Alannikos768/BanterBot_1_8b-chat-w4a16-4bit)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-1_8b-chat-w4a16-4bit) |
| BoostBot_1_8b-chat-w4a16-4bit  | internlm2_5_chat_1_8b | Pre-trained + QLoRA fine-tuning + w4a16 quantization | [HuggingFace](https://huggingface.co/Alannikos768/BoostBot_1_8b-chat-w4a16-4bit)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-1_8b-chat-w4a16-4bit) |



# 📂 Project Structure
```
.
|-- ASR
|   |-- __init__.py
|   |-- models
|   |   `-- sensevoice.py
|   |-- readme.md
|   `-- weights
|       `-- readme.md
|-- Assets
|   |-- animation
|   |   `-- Animation_1.json
|   |-- avatar
|   |   |-- BanterBot.jpg
|   |   |-- BoostBot.jpg
|   |   |-- BoostBot_v2.jpg
|   |   |-- User_v1.jpg
|   |   |-- person1.png
|   |   `-- person2.png
|   |-- gif
|   |   |-- BanterBot-7b.gif
|   |   |-- BoostBot-7b.gif
|   |   |-- Original_7b_BanterBot.gif
|   |   `-- Original_7b_BoostBot.gif
|   |-- image
|   |-- svg
|   |   |-- FunGPT-logo.svg
|   |   `-- openxlab_logo.svg
|   `-- video
|       |-- BanterBot-7b.mp4
|       |-- BoostBot-7b.mp4
|       |-- Original_7b_BanterBot.mp4
|       `-- Original_7b_BoostBot.mp4
|-- Data
|   |-- BanterBot
|   |   |-- feasible_data
|   |   |   `-- readme.md
|   |   |-- raw
|   |   |   `-- readme.md
|   |   |-- readme.md
|   |   |-- sample
|   |   |   `-- readme.md
|   |   |-- scripts
|   |   |   |-- filter_bad_from_conv_data.py
|   |   |   |-- filter_sensitive_words_from_conv_data.py
|   |   |   |-- generate_mutil_conv_chatglm.py
|   |   |   |-- generate_mutil_topic_chatglm.py
|   |   |   |-- generate_self_congnitive_data.py
|   |   |   `-- merge_conv_data_finetune.py
|   |   `-- sensitive_words
|   |       `-- readme.md
|   `-- BoostBot
|       |-- feasible_data
|       |   `-- readme.md
|       |-- raw
|       |   `-- topic.txt
|       |-- sample
|       |   `-- multi_conversation.jsonl
|       `-- scripts
|           |-- generate_mutil_conv_chatglm.py
|           |-- generate_mutil_topic_chatglm.py
|           |-- generate_self_congnitive_data.py
|           `-- merge_conv_data_finetune.py
|-- Docs
|   |-- pictures
|   |   `-- FunGPT.png
|   |-- readme.md
|   `-- user_guides
|       `-- readme.md
|-- Finetune
|   |-- BanterBot
|   |   `-- internlm2_5_chat_7b_qlora_alpaca_e3_copy.py
|   |-- BaseModel
|   |   `-- readme.md
|   `-- BoostBot
|       `-- internlm2_5_chat_7b_qlora_alpaca_e3_copy.py
|-- LICENSE
|-- LLM
|   |-- __init__.py
|   |-- models
|   |   `-- internlm2_5_7b_chat.py
|   |-- readme.md
|   |-- templates
|   |   `-- template.py
|   `-- weights
|       `-- readme.md
|-- README.md
|-- README_en.md
|-- README_zh.md
|-- TTS
|   |-- __init__.py
|   |-- models
|   |   `-- chattts.py
|   |-- readme.md
|   `-- weights
|       `-- readme.md
|-- Test
|   |-- ASR
|   |   |-- example.py
|   |   `-- test_wav.wav
|   |-- TTS
|   |   `-- example.ipynb
|   `-- readme.md
|-- Utils
|   |-- common_utils.py
|   |-- configs.py
|   |-- convert_gif.sh
|   |-- data_utils.py
|   |-- model_settings.py
|   |-- model_utils.py
|   `-- readme.md
|-- Work_dirs
|   |-- ASR
|   |   `-- readme.md
|   `-- TTS
|       `-- readme.md
|-- __init__.py
|-- app.py
|-- env.yaml
|-- pages
|   |-- 1_🍬💖_甜言模式.py
|   |-- 2_💥😤_怼语模式.py
|   `-- 3_🚀💫_待开发ing.py
|-- project_structure.txt
`-- requirements.txt

44 directories, 79 files

```

# ⚡ Quick Start
### 1. Deployment Environment

- Operating System: Ubuntu 20.04.6 LTS
- CPU: Intel(R) Xeon(R) Platinum 8369B CPU @ 2.90GHz (Online GPU Server)
- GPU: NVIDIA A100-SXM4-80GB, NVIDIA-SMI 535.54.03, Driver Version: 535.54.03, CUDA Version: 12.2
- Python: 3.10.0


### 2. Key Dependency Information
```
Python==3.10.0
torch==2.4.1
torch-complex==0.4.4
torchaudio==2.4.1
torchvision==0.16.2
chattts==0.1.1
streamlit==1.38.0
audio-recorder-streamlit==0.0.10
```

### 3. Deployment Steps

#### 3.1. Clone the Code or Manually Download the Code to Place on the Server:

```shell
git clone https://github.com/Alannikos/FunGPT
```

#### 3.2. Configure the Python Environment (Recommended to Use Conda)

- Enter the root directory of the project

```
cd FunGPT
```

- Create a conda environment

```
conda create -n FunGPT python==3.10.0
```

- Install third-party libraries
```
pip install -r requirements.txt

# This will take approximately 1 hour

```

#### 3.3 Download Models

##### 3.3.1 TTS Models (Required if using TTS)

- Install git-lfs
As model files need to be downloaded, please ensure `git-lfs` is already installed. Linux users can install it using the following command:

```
apt install git-lfs
```

- Initialize `LFS`
```
git lfs install
```
- Download the TTS model to the specified path

```
# 1. Navigate to the specific directory
cd /FunGPT/TTS/weights

# 2. Download the model from huggingface
git clone https://huggingface.co/2Noise/ChatTTS
```

- For users unable to access HuggingFace, download from the mirror source

```
# 2. Download the model from the mirror source
git clone https://hf-mirror.com/2Noise/ChatTTS
```

##### 3.3.2 ASR Models (Required if using ASR)

As model files need to be downloaded, please ensure `git-lfs` is already installed. Linux users can install it using the following command:


```
# Users who have already downloaded can ignore this command

apt install git-lfs
```

- Initialize `LFS`
```
git lfs install
```

- Download the ASR model to the specified path

```
# 1. 进入指定目录
cd /FunGPT/ASR/weights

# 2. Navigate to the specific directory
git clone https://huggingface.co/FunAudioLLM/SenseVoiceSmall

```

- For users unable to access HuggingFace, download from the mirror source

```
# 2. Download the model from the mirror source
git clone https://hf-mirror.com/FunAudioLLM/SenseVoiceSmall
```

##### 3.3.3 LLM Models (Required)
$\quad$ For selecting LLM models, we provide many options. The models with the best performance are [BanterBot-7b-chat](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-7b-chat/tree/main) and [BoostBot-7b-chat](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-7b-chat/tree/main). The quantized models also perform very well. Among the 1_8B models, the performance is also quite good. To save on download time, we have chosen these two 1_8B models: [BanterBot-1_8b-chat](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-1_8b-chat/tree/main) and [BoostBot-1_8b-chat](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-1_8b-chat/tree/main) as examples, but you can replace them as needed.


- Initialize `LFS`
```
git lfs install
```

- Download the LLM models to the specified path

```
# 1. Navigate to the specific directory
cd /FunGPT/LLM/weights

# 2. Download the BanterBot-1_8b-chat model from huggingface

https://huggingface.co/Alannikos768/BanterBot_1_8b-chat

# 3. Download the BoostBot-1_8b-chat model from huggingface

https://huggingface.co/Alannikos768/BoostBot_1_8b-chat

```

- For users unable to access HuggingFace, download from OpenXLab

```

# 2. Download the BanterBot-1_8b-chat model from OpenXLab (for users in China)
git clone https://code.openxlab.org.cn/Alannikos/BanterBot-1_8b-chat.git

# 3. Download the BoostBot-1_8b-chat model from OpenXLab (for users in China)
git clone https://code.openxlab.org.cn/Alannikos/BoostBot-1_8b-chat.git
```


#### 3.4 Run the Web Script
```
conda activate FunGPT

streamlit run app.py --server.address=127.0.0.1 --server.port=7860
```

### 4. Model Experience

- If running on a remote server, port forwarding is needed
```
ssh -p 46411 user@ip -CNg -L 7860:127.0.0.1:7860 -o StrictHostKeyChecking=no
```

- Then, to experience the application

Open your browser, input `http://127.0.0.1:7860`, and click the corresponding interface to experience `FunGPT`.

# 📚 Detailed Guide

### Data Generation Guide
$\quad$ In the fine-tuning process of large models, we can utilize various algorithms for SFT, whether through native techniques like LoRA fine-tuning or using packaged tools such as [Xtuner](https://github.com/InternLM/xtuner) and [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory). We need to prepare high-quality fine-tuning data. However, the cost of manual data annotation is relatively high, which is inefficient for most individual developers. Thus, this project uses [ChatGLM4-Flash](https://bigmodel.cn/), available for free from Zhipu, to generate the multi-turn dialogue datasets we need. This approach is simple and easy to control. Generally, the generated datasets can achieve satisfactory fine-tuning results. For the specific data generation guide, you can refer to the [data_generation](Data/BoostBot/scripts/generate_mutil_conv_chatglm.py).

$\quad$ In our documentation, we will mainly introduce the process of creating a multi-turn dialogue dataset and how to construct a self-awareness dataset. With these two parts of the dataset, you can basically fine-tune a large language model for downstream tasks.

### LLM Usage Guide
$\quad$ The large language model is the core component of this project. We selected the open-source InternLM2.5 series as the base model. InternLM2.5 has strong understanding and generation capabilities, supports an 8K context window, and has good Chinese language understanding capabilities. In actual deployment, we use a 4bit quantized version to reduce resource consumption while maintaining model performance. For detailed deployment and usage methods, please refer to the [LLM_Usage](LLM/models/internlm2_5_7b_chat.py) document.

$\quad$ In this project, the LLM is primarily responsible for understanding user input and generating responses. It also needs to handle multi-modal input and coordinate with ASR and TTS modules.

### ASR Usage Guide
$\quad$ The speech recognition module uses the open-source SenseVoice model, which has excellent multilingual speech recognition capabilities. The model supports multiple languages, including Chinese and English, with high accuracy and good ability to handle background noise. For specific deployment and usage instructions, please check the [ASR_Usage](ASR/models/sensevoice.py) document.

$\quad$ In practical applications, the ASR module is responsible for converting user voice input into text and passing it to the LLM for processing. We provide a streaming recognition interface and support real-time speech transcription.

### TTS Usage Guide
$\quad$ The speech synthesis module uses the open-source ChatTTS model, which can generate natural and smooth speech. We use a bilingual model for Chinese and English, supporting multi-speaker synthesis and adjustable parameters like speed and timbre. For detailed configuration and usage methods, please refer to the [TTS_Usage](TTS/models/chattts.py) document.

$\quad$ The TTS module is mainly responsible for converting text generated by the LLM into speech output, supporting batch synthesis mode. We also provide an emotion control interface that can automatically adjust the tone and pitch according to the text content for more natural output.

### Model Fine-Tuning Guide
$\quad$ To meet the needs of specific scenarios, we provide a complete model fine-tuning process. We mainly use parameter-efficient fine-tuning methods like LoRA and QLoRA, which can be trained on consumer-grade graphics cards. The fine-tuning process uses the [Xtuner](https://github.com/InternLM/xtuner) tool, which offers friendly configuration templates and comprehensive training monitoring. For specific fine-tuning processes and parameter settings, please refer to the [Xtuner_Usage](Finetune/BoostBot/internlm2_5_chat_7b_qlora_alpaca_e3_copy.py) document.

$\quad$ Fine-tuning supports various task types such as instruction alignment, multi-turn dialogue, and role-playing. We provide pre-processing scripts to convert data formats and also support incremental training for further optimization on existing models.

### Model Quantization Guide
$\quad$ Quantization is an important optimization method to deploy large models with limited computing resources. We use the [LMDeploy](https://github.com/InternLM/lmdeploy) tool for model quantization, supporting INT4 quantization to significantly reduce memory usage while maintaining model performance. For detailed quantization processes, refer to the [LMDeploy_Usage](https://github.com/InternLM/lmdeploy) document.

$\quad$ The quantization process supports weight quantization and activation value quantization, and provides tools to verify the accuracy of quantized models. LMDeploy also offers performance comparison data of different quantization strategies to help users choose the most suitable quantization plan.


# 🔮 Future Development Plans

1. - [x] ~~Recording Project Video~~
2. - [ ] Support GPT-Sovits
3. - [ ] Support API access for large language models
4. - [ ] Improve the data generation guide section
5. - [ ] Enhance the large language model usage section
6. - [ ] Refine the text-to-speech module introduction section
7. - [ ] Improve the speech recognition usage section
8. - [x] ~~Add Sensitive Words Module~~

# 🙏 Acknowledgments

Thanks to the following open-source tools and projects for their support:

| Tool | Description |
|---|---|
| [InternLM-Tutorial](https://github.com/InternLM/Tutorial) | An active and open large model training camp |
| [Xtuner](https://github.com/InternLM/xtuner) | Tool for model training and fine-tuning |
| [LMDeploy](https://github.com/InternLM/lmdeploy) | Tool for model quantization and deployment |
| [Streamlit](https://streamlit.io/) | Tool for efficiently building AI applications |
| [DeepSpeed](https://github.com/microsoft/DeepSpeed) | Tool for model training and inference acceleration |
| [Pytorch](https://pytorch.org/) | Widely used deep learning framework |

## Related Projects

| Project | Description |
|---|---|
| [InternLM](https://github.com/InternLM/InternLM) | A series of advanced open-source large language models |
| [ChatTTS](https://github.com/2noise/ChatTTS) | An open-source text-to-speech project |
| [SenseVoice](https://github.com/FunAudioLLM/SenseVoice) | A speech recognition open-source project by Alibaba |
| [LangGPT](https://github.com/langgptai/LangGPT) | An open-source project about structured prompts. |
| [GangLLM](https://github.com/boss-mao/GangLLM) |  An open-source project about engaging in banter with users |
| [Linly-Talker](https://github.com/Kedreamix/Linly-Talker) | An open-source project on artificial intelligence systems |
| [Yanjie](https://github.com/Alannikos/Yanjie) | An open-source project for enhancing English learning with an AI assistant |
| [wulewule](https://github.com/xzyun2011/wulewule) | An open-source project featuring an AI assistant themed on Black Myth: Wukong |
| [ChatSensitiveWords](https://github.com/kaixindelele/ChatSensitiveWords/) | An  project concerning SensitiveWords |

## Special Thanks

| Organization | Description |
|---|---|
| [Shanghai Artificial Intelligence Laboratory](https://www.shlab.org.cn/) | Thanks for the technical and platform support |

# ⚖️ Disclaimer

$\quad$ Thank you for your interest in and use of the FunGPT project. This project aims to provide users with an enjoyable and engaging interaction experience. Please be aware of the following points:

- **Research Purposes**: The FunGPT project and its associated resources are intended solely for academic research purposes and are strictly prohibited from any commercial use. If any third-party code is involved, please adhere strictly to its respective open-source license.

- **Accuracy of Generated Content**: Due to the influence of factors such as model algorithms, randomness, and quantization precision limitations, FunGPT cannot guarantee the accuracy or applicability of the generated content. Please exercise caution and independently assess the suitability of the content when using it.

- **Legal Responsibility**: This project does not assume any responsibility for the legality of the model's output content and its consequences. Users should ensure that their behavior complies with relevant laws and regulations and are responsible for the outcomes of their use.

$\quad$ By using FunGPT, you indicate that you have accepted these disclaimer terms. We hope FunGPT can bring fun and vitality to your daily life. Thank you for your support and use.


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Alannikos/FunGPT&type=Date)](https://star-history.com/#Alannikos/FunGPT&Date)
