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
[![OpenXLab_Model](https://cdn-static.openxlab.org.cn/header/openxlab_models.svg)](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-7b-chat)
</div>

_____________________________________________________________________

# 🚀 最新动态

<details open>
<summary><b>2024</b></summary>

- \[2024/11/19\] 🔒🛡️ 加入敏感词处理模块，防止模型输出有害观点 
- \[2024/11/18\] 🔧🌟 完成**快速使用**部分的文档更新，解决关于环境搭建的bug。
- \[2024/11/14\] 🎉✨ 利用LMDeploy工具完成对四个模型的量化工作，FunGPT家族喜添新成员！模型已发布在[HuggingFace](https://huggingface.co/Alannikos768)。
- \[2024/11/13\] 🎉✨ 项目推出两款1.8B模型，FunGPT家族喜添新成员！模型分别为[BanterBot_1_8b-chat](https://huggingface.co/Alannikos768/BanterBot_1_8b-chat)，以及[BoostBot_1_8b-chat](https://huggingface.co/Alannikos768/BoostBot_1_8b-chat)。
- \[2024/11/10\] 🎉✨ 重磅推出两款全新7B模型，FunGPT家族喜添新成员！模型分别为[BanterBot-7b-chat](https://huggingface.co/Alannikos768/BanterBot-7b-chat)，以及[BoostBot-7b-chat](https://huggingface.co/Alannikos768/BoostBot-7b-chat)。
- \[2024/11/10\] 🛠️🎯 项目完成了重大更新，并修复已知的绝对路径bug问题~
- \[2024/10/28\] 🎈🥳 项目实现利用xtuner来实现微调大语言模型，同时发布第一版[BoostBot_v1](https://huggingface.co/Alannikos768/Kua_LLM)!
- \[2024/10/19\] 🎉💬 实现利用Chat-GLM4系列生成微调对话数据的工具链。
- \[2024/10/03\] 🎨🐞 项目对系统界面进行了一系列的美化工作，同时还修复一些已知的错误。
- \[2024/10/02\] 🚀💻 项目中加入了模型加载与释放机制，合理利用GPU显存。
- \[2024/10/01\] 😄🐍 项目中加入了异常处理模块，增加应用的稳定性。
- \[2024/09/28\] 👋👋 初步完成LLM（[InternLM2.5_1.8b](https://huggingface.co/internlm/internlm2_5-1_8b-chat)）, ASR([Sensevoice](https://www.modelscope.cn/models/iic/sensevoicesmall))以及TTS([ChatTTS](https://huggingface.co/2Noise/ChatTTS))各个部分的单功能测试以及效果检测。

</details>

# 🌟 项目简介

$\quad$在这个快节奏的世界里，我们都需要一点调味剂来调和生活。无论是需要一点**甜言蜜语**来提振精神，还是需要一剂**犀利怼语**来释放压力，基于InternLM2.5系列大模型开发出的**FunGPT**都能满足您的需求。

🍬 甜言蜜语模式：

- **心情提升器🌟✨**：当您感到低落，我们的甜言蜜语模式能让您的心情瞬间飙升，就像尝了一颗超级甜的蜜糖。
- **自信加油站💪🌈**：同时我们的**赞师傅**会用合适且独特的方式夸奖您，让您的自信心爆棚。

🔪 犀利怼语模式：

- **压力释放阀💥😤**：当您感到压力山大，我们的怼人模式能让您在怼人的同时，找到释放的出口。
- **幽默吐槽机😂👅**：**怼师傅**的言语不仅犀利，而且幽默风趣，在怼人的过程中，您还能体会到脑洞大开的怼人方式。

# 🤔 项目亮点

$\quad$**FunGPT**采用的是先进的InternLM2.5系列模型。我们利用[Xtuner](https://github.com/InternLM/xtuner)进行指令和全量微调，使模型能够满足用户的个性化要求。同时为了方便用户，我们发布了1.8B系列小模型，减量不减效果；此外，利用LMDeploy还对多个模型进行了**AWQ量化**操作，既节省显存又提升推理速度！⚡

$\quad$在此项目中，我们对日常使用的用户，针对赞美和怼人这两个场景进行了针对性的考察，使得用户能够在日常生活中通过和我们的两位“师傅”进行交谈，达到调节心情的目的；此外，对于初入LLM世界的开发者，我们在LLM，ASR以及TTS方面都拥有文档与视频支持，希望此项目能够成为引领各位大佬进阶AI世界的第一个入门项目，帮助各位快速掌握大模型开发技能。

$\quad$我们具有以下优势（包括但不局限于）：

  1. 🤗 **夸人高手**：生成甜言蜜语，陪伴您生活的每一天。
  2. 🗯️ **怼人大师**：针对性应答，妙语连珠，与“我”斗智斗勇。
  3. 📊 **数据收集指南**：开源核心流程及代码，帮你快速掌握微调数据制作。
  4. 📖 **LLM全流程指南**：开源LLM模块代码，带你轻松入门。
  5. 🔊 **ASR全流程指南**：开源ASR模块代码，助力你实现语音识别梦想。
  6. 🎙️ **TTS全流程指南**：开源TTS模块代码，助力你实现语音合成梦想。
  7. 📂 **结构清晰**：详细注释与解释文档，并且具有清晰的项目结构！
  8. ⚡ **模型量化**：降低使用门槛，随时随地体验AI的魅力。
  9. 🎥 **视频教程**：敬请期待我们的完整项目介绍视频！


# 🖼️ 效果图

|Original_7b_BoostBot|BoostBot-7b|
|:---:|:---:|
|<img src="./Assets/gif/Original_7b_BoostBot.gif" width="400">|<img src="./Assets/gif/BoostBot-7b.gif" width="400">|

|Original_7b_BanterBot|BanterBot-7b|
|:---:|:---:|
|<img src="./Assets/gif/Original_7b_BanterBot.gif" width="400">|<img src="./Assets/gif/BanterBot-7b.gif" width="400">|

# 🏗️ 项目架构图

![项目架构图](Docs/pictures/FunGPT.png)

# 🧳 模型集

| 模型                           | 基座                  | 类型                       | 地址                                                         |
| ------------------------------ | --------------------- | -------------------------- | ------------------------------------------------------------ |
| BanterBot-7b-chat              | internlm2_5_chat_7b   | 预训练+QLoRA微调           | [HuggingFace](https://huggingface.co/Alannikos768/BanterBot-7b-chat)<br/>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-7b-chat) |
| BoostBot-7b-chat               | internlm2_5_chat_7b   | 预训练+QLoRA微调           | [HuggingFace](https://huggingface.co/Alannikos768/BoostBot-7b-chat)<br/>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-7b-chat) |
| BanterBot_1_8b-chat            | internlm2_5_chat_1_8b | 预训练+QLoRA微调           | [HuggingFace](https://huggingface.co/Alannikos768/BanterBot_1_8b-chat)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-1_8b-chat) |
| BoostBot_1_8b-chat             | internlm2_5_chat_1_8b | 预训练+QLoRA微调           | [HuggingFace](https://huggingface.co/Alannikos768/BoostBot_1_8b-chat)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-1_8b-chat) |
| BanterBot-7b-chat-w4a16-4bit   | internlm2_5_chat_7b   | 预训练+QLoRA微调+w4a16量化 | [HuggingFace](https://huggingface.co/Alannikos768/BanterBot-7b-chat-w4a16-4bit)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-7b-chat-w4a16-4bit) |
| BoostBot-7b-chat-w4a16-4bit    | internlm2_5_chat_7b   | 预训练+QLoRA微调+w4a16量化 | [HuggingFace](https://huggingface.co/Alannikos768/BoostBot-7b-chat-w4a16-4bit)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-7b-chat-w4a16-4bit) |
| BanterBot_1_8b-chat-w4a16-4bit | internlm2_5_chat_1_8b | 预训练+QLoRA微调+w4a16量化 | [HuggingFace](https://huggingface.co/Alannikos768/BanterBot_1_8b-chat-w4a16-4bit)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-1_8b-chat-w4a16-4bit) |
| BoostBot_1_8b-chat-w4a16-4bit  | internlm2_5_chat_1_8b | 预训练+QLoRA微调+w4a16量化 | [HuggingFace](https://huggingface.co/Alannikos768/BoostBot_1_8b-chat-w4a16-4bit)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-1_8b-chat-w4a16-4bit) |

# ⚡ 快速使用
### 1. 部署环境

- 操作系统：Ubuntu 20.04.6 LTS
- CPU：Intel(R) Xeon(R) Platinum 8369B CPU @ 2.90GHz（在线 GPU 服务器）
- 显卡：NVIDIA A100-SXM4-80GB， NVIDIA-SMI 535.54.03，Driver Version: 535.54.03，CUDA Version: 12.2
- Python: 3.10.0

### 2. 关键依赖信息
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

### 3. 部署步骤

#### 3.1. Clone 代码或者手动下载代码放置服务器：

```shell
git clone https://github.com/Alannikos/FunGPT
```

#### 3.2. 配置Python环境(推荐使用conda)

- 进入项目的根目录

```
cd FunGPT
```

- 创建conda环境

```
conda create -n FunGPT python==3.10.0
```

- 安装第三方库
```
pip install -r requirements.txt

# 大概需要1h左右

```

#### 3.3 下载模型

##### 3.3.1 TTS模型(若使用则必选)

- git-lfs安装
由于涉及到模型文件的下载，首先需要保证`git-lfs`已经成功安装。对于`Linux`用户来说，可按照下面的命令安装：
```
apt install git-lfs
```

- 启动`LFS`
```
git lfs install
```
- 下载TTS模型到指定路径

```
# 1. 进入指定目录
cd /FunGPT/TTS/weights

# 2. 从huggingface下载模型
git clone https://huggingface.co/2Noise/ChatTTS
```

- 无法访问HuggingFace用户，可从镜像源下载

```
# 2. 从镜像源下载模型
git clone https://hf-mirror.com/2Noise/ChatTTS
```

##### 3.3.2 ASR模型(若使用则必选)
由于涉及到模型文件的下载，首先需要保证`git-lfs`已经成功安装。对于`Linux`用户来说，可按照下面的命令安装：

```
# 已下载用户可忽略此条命令
apt install git-lfs
```

- 启动`LFS`
```
git lfs install
```

- 下载TTS模型到指定路径

```
# 1. 进入指定目录
cd /FunGPT/ASR/weights

# 2. 从huggingface下载模型
git clone https://huggingface.co/FunAudioLLM/SenseVoiceSmall

```

- 无法访问HuggingFace用户，可从镜像源下载

```
# 2. 从镜像源下载模型
git clone https://hf-mirror.com/FunAudioLLM/SenseVoiceSmall
```

##### 3.3.3 LLM模型(必选)
$\quad$对于LLM模型的选择，我们提供了很多选择，效果最佳的模型为[BanterBot-7b-chat](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-7b-chat/tree/main)和[BoostBot-7b-chat](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-7b-chat/tree/main)，其次量化的模型效果也非常不错；此处为了节约大家的下载时间，我们选择了这两个1_8B模型: [BanterBot-1_8b-chat](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-1_8b-chat/tree/main)和[BoostBot-1_8b-chat](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-1_8b-chat/tree/main)来作为示例，大家可以按照需求自由进行替换即可。

- 启动`LFS`
```
git lfs install
```

- 下载LLM模型到指定路径

```
# 1. 进入指定目录
cd /FunGPT/LLM/weights

# 2. 从huggingface下载BanterBot-1_8b-chat模型
https://huggingface.co/Alannikos768/BanterBot_1_8b-chat

# 3. 从huggingface下载BoostBot-1_8b-chat模型
https://huggingface.co/Alannikos768/BoostBot_1_8b-chat

```

- 无法访问HuggingFace用户，可从OpenXLab下载

```

# 2. 从OpenXLab下载BanterBot-1_8b-chat模型(国内用户)
git clone https://code.openxlab.org.cn/Alannikos/BanterBot-1_8b-chat.git

# 3. 从OpenXLab下载BoostBot-1_8b-chat模型(国内用户)
git clone https://code.openxlab.org.cn/Alannikos/BoostBot-1_8b-chat.git
```


#### 3.4 运行网页脚本
```
conda activate FunGPT

streamlit run app.py --server.address=127.0.0.1 --server.port=7860
```

### 4. 模型体验
- 如果是在远程服务器上运行的，需要进行端口映射
```
ssh -p 46411 user@ip -CNg -L 7860:127.0.0.1:7860 -o StrictHostKeyChecking=no
```

- 然后在体验应用
打开浏览器，输入`http://127.0.0.1:7860`，然后点击对应界面即可体验`FunGPT`


# 📚 详细指南

### 数据生成指南
$\quad$在大模型微调过程中，我们可以借助许多算法进行SFT，不论是通过原生的LoRA微调等技术，还是通过封装好的工具，比如[Xtuner](https://github.com/InternLM/xtuner)，[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)等，我们都需要准备高质量的微调数据，但是通过人工手动标注数据的成本较高，对于大部分个人开发者来说，效率还是比较低下，所以本项目采用智谱免费使用的[ChatGLM4-Flash](https://bigmodel.cn/)来生成我们所需要的多轮对话数据集，这样的方式简单且易于控制。通常来说，生成的数据集还是能够达到较好的微调效果，具体的数据生成指南可以参考[data_generation](Data/Kua_LLM/scripts/generate_mutil_conv_chatglm.py)。

$\quad$在我们的文档中，我们将主要介绍关于多轮对话数据集制作过程以及如何去构造自我认知数据集，通过这两部分数据集，基本可以微调出一个用于下游任务的大语言模型。

### LLM 使用指南
$\quad$大语言模型是本项目的核心组件，我们选用了开源的InternLM2.5系列作为基础模型。InternLM2.5具有强大的理解和生成能力，支持长上下文窗口，并且具有较好的中文理解能力。在实际部署中，我们采用了4bit量化版本以降低资源占用，同时保持模型性能。详细的使用方法请参考[LLM_Usage](LLM/models/internlm2_5_7b_chat.py)。

$\quad$在本项目中，LLM主要负责对用户输入进行理解和回复生成，同时还需要处理多模态输入，并与ASR和TTS模块进行协同工作。

### ASR 使用指南
$\quad$语音识别模块采用了开源的SenseVoice模型，该模型具有优秀的多语言语音识别能力。模型支持中英文等多语言识别，准确率较高，且能够较好地处理背景噪声。具体的部署和使用说明请查看[ASR_Usage](ASR/models/sensevoice.py)文档。

$\quad$在实际应用中，ASR模块负责将用户的语音输入转换为文本，并传递给LLM进行处理。我们提供了流式识别接口，也支持实时语音转写。

### TTS 使用指南
$\quad$语音合成模块使用了开源的ChatTTS模型，该模型能够生成自然流畅的语音。支持多说话人合成，并且可以调节语速和音色等参数。详细的配置和使用方法请参考[TTS_Usage](TTS/models/chattts.py)文档。

$\quad$TTS模块主要负责将LLM生成的文本转换为语音输出，支持批量合成模式。我们还提供了情感控制接口，可以根据文本内容自动调整语气和语调，使输出更加自然。

### 模型微调指南
$\quad$为了适应特定场景的需求，我们提供了完整的模型微调流程。主要采用了LoRA和QLoRA等参数高效的微调方法，可以在消费级显卡上进行训练。微调过程使用了[Xtuner](https://github.com/InternLM/xtuner)工具，该工具提供了友好的配置模板和完善的训练监控。具体的微调流程和参数设置请参考docs中的[Xtuner_Usage](Finetune/Kua_LLM/scripts/internlm2_5_chat_7b_qlora_alpaca_e3_copy.py)文档。

$\quad$微调支持指令对齐、多轮对话、角色扮演等多种任务类型。我们提供了预处理脚本来转换数据格式，同时也支持增量训练，可以在已有模型基础上继续优化。

### 模型量化指南
$\quad$为了在有限的计算资源下部署大模型，量化是一个重要的优化手段。我们使用[LMDeploy](https://github.com/InternLM/lmdeploy)工具进行模型量化，支持INT4量化，在保持模型性能的同时减少显存占用，详细的量化流程请参考[LMDeploy_Usage](https://github.com/InternLM/lmdeploy)文档。

$\quad$量化过程支持权重量化和激活值量化，并提供了量化后的精度验证工具。LMDeploy还提供了不同量化策略的性能对比数据，帮助用户选择最适合的量化方案。

# 🔮 未来开发计划

1. - [×] 录制项目视频
2. - [ ] 支持GPT-Sovits
3. - [ ] 支持API接入大语言模型
4. - [ ] 完善数据生成指南部分
5. - [ ] 完善大语言模型使用部分
6. - [ ] 完善文本转语音模块介绍部分
7. - [ ] 完善语音识别使用部分
8. - [×] 加入敏感词模块

# 🙏 致谢

非常感谢下列开源工具和开源项目的支持：

| 项目 | 描述 |
|---|---|
| [InternlM-Tutorial](https://github.com/InternLM/Tutorial) | 活跃且开源的大模型训练营 |
| [Xtuner](https://github.com/InternLM/xtuner) | 用于模型训练和微调的工具 |
| [LMDeploy](https://github.com/InternLM/lmdeploy) | 用于模型量化和部署的工具 |
| [Streamlit](https://streamlit.io/) | 高效构建AI应用的工具 |
| [DeepSpeed](https://github.com/microsoft/DeepSpeed) | 用于模型训练和推理加速的工具 |
| [Pytorch](https://pytorch.org/) | 广泛使用的深度学习框架 |

## 相关开源项目

| 项目 | 描述 |
|---|---|
| [InternLM](https://github.com/InternLM/InternLM) | 一系列先进的开源大语言模型 |
| [ChatTTS](https://github.com/2noise/ChatTTS) | 一个文本转语音的开源项目 |
| [SenseVoice](https://github.com/FunAudioLLM/SenseVoice) | 一个由阿里巴巴出品的一个语音识别的开源项目 |
| [LangGPT](https://github.com/langgptai/LangGPT) | 一个关于结构化提示词的开源项目 |
| [GangLLM](https://github.com/boss-mao/GangLLM) | 一个关于与用户抬杠的开源项目 |
| [Linly-Talker](https://github.com/Kedreamix/Linly-Talker) | 一款关于人工智能系统的开源项目 |
| [Yanjie](https://github.com/Alannikos/Yanjie) | 一个关于促进英语学习的人工智能助手的开源项目 |
| [wulewule](https://github.com/xzyun2011/wulewule) | 一个关于黑神话悟空的人工智能助手的开源项目 |
| [ChatSensitiveWords](https://github.com/kaixindelele/ChatSensitiveWords/) | 一个关于敏感词过滤的开源项目 |

## 特别鸣谢
| 机构 | 描述 |
|---|---|
| [上海人工智能实验室](https://www.shlab.org.cn/) | 感谢提供的技术支持以及平台支持 |

# ⚖️ 免责声明

$\quad$感谢您对FunGPT项目的关注与使用。本项目旨在为用户提供轻松有趣的交流体验，以下几点事项请您务必知悉：

- **研究用途**：FunGPT项目及其相关资源仅限用于学术研究目的，严禁将其用于任何商业用途。如有使用涉及到第三方代码的部分，请严格遵循其对应的开源协议。

- **内容生成准确性**：由于内容生成过程受到模型算法、随机性和量化精度限制等因素的影响，FunGPT无法对生成内容的准确性和适用性作出保证。请在使用时保持审慎，并自行判断内容的适用性。

- **法律责任**：本项目不对模型输出内容的合法性和相关后果承担责任。用户应确保自身的使用行为符合相关法律法规，并对使用结果负责。

$\quad$使用FunGPT即表示您已接受本免责声明条款。我们希望FunGPT能够为您的日常生活增添乐趣与活力，感谢您的支持与使用。

