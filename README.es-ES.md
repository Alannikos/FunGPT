

<div align="center">
  <img src="Assets/svg/FunGPT-logo.svg" width="100"/>

  [📘Documentación](https://github.com/Alannikos/FunGPT) |
  [🛠️Inicio Rápido](https://github.com/Alannikos/FunGPT) |
  [🤔Reportar Problemas](https://github.com/Alannikos/FunGPT/issues) 

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


# Últimas Noticias 🎉

<details open>
<summary><b>2024</b></summary>

- \[2025/05/30\] 🤗📊 Publicamos en código abierto el conjunto de datos de afinamiento de cumplidos para BoostBot. [ComplimentCorpus](https://huggingface.co/datasets/Alannikos768/ComplimentCorpus)
- \[2025/05/29\] 🛠️🎯 Se corrigieron algunos errores relacionados con rutas [FIX](https://github.com/Alannikos/FunGPT/commit/b1e25f7addebd91d8ec031a013403365ad495c94)
- \[2024/11/30\] 📢📺 ¡Hemos publicado un video de presentación del proyecto! Pueden encontrarlo en [Bilibili](https://www.bilibili.com/video/BV1EGBYYtEMA/). Si les gusta, no olviden darle un 👍 y seguirnos.
- \[2024/11/19\] 🔒🛡️ Se incorporó un módulo de procesamiento de palabras sensibles para evitar que el modelo genere opiniones perjudiciales.
- [2024/11/18] 🔧🌟 Se completaron las actualizaciones de la documentación de la sección **Inicio Rápido** y se resolvieron errores de configuración del entorno.
- [2024/11/14] 🎉✨ Cuatro modelos cuantizados exitosamente utilizando la herramienta LMDeploy. ¡La familia FunGPT da la bienvenida a nuevos miembros! Los modelos ya están disponibles en [HuggingFace](https://huggingface.co/Alannikos768).
- [2024/11/13] 🎉✨ Lanzamiento de dos nuevos modelos de 1.8B, ¡expandiendo la familia FunGPT! Los modelos son [BanterBot_1_8b-chat](https://huggingface.co/Alannikos768/BanterBot_1_8b-chat) y [BoostBot_1_8b-chat](https://huggingface.co/Alannikos768/BoostBot_1_8b-chat).
- [2024/11/10] 🎉✨ Lanzamiento de dos nuevos modelos de 7B, añadiendo nuevos miembros a la familia FunGPT! Los modelos son [BanterBot-7b-chat](https://huggingface.co/Alannikos768/BanterBot-7b-chat) y [BoostBot-7b-chat](https://huggingface.co/Alannikos768/BoostBot-7b-chat).
- [2024/11/10] 🛠️🎯 Actualizaciones importantes del proyecto completadas, incluyendo la corrección de errores conocidos de rutas absolutas.
- [2024/10/28] 🎈🥳 Se logró el afinamiento de grandes modelos de lenguaje utilizando xtuner y se lanzó la primera versión de [BoostBot_v1](https://huggingface.co/Alannikos768/Kua_LLM)!
- [2024/10/19] 🎉💬 Se desarrolló una cadena de herramientas para generar datos de diálogo afinados utilizando la serie Chat-GLM4.
- [2024/10/03] 🎨🐞 Se mejoró la interfaz del sistema y se corrigieron algunos errores conocidos.
- [2024/10/02] 🚀💻 Se añadieron mecanismos de carga y descarga de modelos para optimizar el uso de la memoria de la GPU.
- [2024/10/01] 😄🐍 Se integró un módulo de manejo de excepciones para mejorar la estabilidad de la aplicación.
- [2024/09/28] 👋👋 Se completaron las pruebas y evaluaciones iniciales de las funcionalidades individuales para LLM ([InternLM2.5_1.8b](https://huggingface.co/internlm/internlm2_5-1_8b-chat)), ASR ([Sensevoice](https://www.modelscope.cn/models/iic/sensevoicesmall)) y TTS ([ChatTTS](https://huggingface.co/2Noise/ChatTTS)).

</details>

_____________________________________________________________________


# 🌟 Introducción del Proyecto

$\quad$ En este mundo de ritmo acelerado 🌍, todos necesitamos un poco de sabor para equilibrar nuestra vida. Ya sea que busques algunos **dulces cumplidos** 🍭 para animarte ✨ o una dosis de **respuestas agudas** 💥 para desahogarte 😤, **FunGPT**, desarrollado sobre la base de los modelos de la serie InternLM2.5 🤖, ¡está aquí para satisfacer tus necesidades 🎯!

🍬 Modo de Cumplidos Dulces:

- **Impulsor de Ánimo 🌟✨**: Cuando te sientas decaído, nuestro Modo de Cumplidos Dulces levantará instantáneamente tu estado de ánimo, como probar un dulce increíblemente delicioso.
- **Estación de Combustible de Confianza 💪🌈**: Mientras tanto, nuestro **Maestro del Elogio** te complimentará de las maneras más adecuadas y únicas, haciendo que tu confianza se eleve.

🔪 Modo de Respuestas Agudas:

- **Válvula de Liberación de Estrés 💥😤**: Cuando te sientas abrumado, nuestro Modo de Respuestas proporciona una salida para desahogarte mientras entrega comentarios agudos.
- **Máquina de Tobos Humorísticos 😂👅**: Las palabras del **Maestro del Tobo** no solo son agudas, sino también humorísticas e imaginativas, permitiéndote experimentar respuestas ingeniosas mientras te diviertes.



# 💬 Únete a Nuestro Grupo de WeChat

¡Escanea el código QR a continuación para unirte a nuestro grupo de discusión de WeChat y comunicarte con más desarrolladores y usuarios!

<div align="center">
  <img src="Assets/image/wechat_group.jpg" width="200"/>
</div>


# 🤔 Puntos Destacados del Proyecto

$\quad$**FunGPT** se basa en los modelos de vanguardia de la serie InternLM2.5. Utilizando [Xtuner](https://github.com/InternLM/xtuner), realizamos afinamiento tanto por instrucciones como completo, permitiendo que los modelos satisfagan necesidades personalizadas de los usuarios. Para mejorar la accesibilidad, lanzamos la serie 1.8B de modelos ligeros, que ofrecen un rendimiento excepcional a pesar de su reducido tamaño. Además, empleamos **cuantización AWQ** mediante LMDeploy en múltiples modelos, ahorrando memoria de GPU mientras aumentamos la velocidad de inferencia! ⚡

$\quad$ Este proyecto atiende a todos los usuarios centrándose en los dos escenarios de elogio y tobo, permitiendo a los usuarios chatear con nuestros dos "Maestros" para regular sus estados de ánimo. Para desarrolladores que recién se adentran en el mundo de los LLM, proporcionamos amplia documentación y tutoriales en video que cubren LLM, ASR y TTS, haciendo de este proyecto un punto de entrada ideal para dominar habilidades de desarrollo de grandes modelos.

$\quad$ Nuestras ventajas incluyen, pero no se limitan a:

1. 🤗 **Maestro de Cumplidos**: Genera palabras dulces para iluminar tu vida diaria.
2. 🗯️ **Experto en Tobos**: Respuestas personalizadas con ingenio agudo, participando en una batalla de ingenios conmigo.
3. 📊 **Guía de Recopilación de Datos**: Totalmente de código abierto, te ayuda a comprender rápidamente la creación de conjuntos de datos para afinamiento.
4. 📖 **Guía Completa del Flujo de Trabajo de LLM**: Código y documentación integrales, de código abierto, facilitando el inicio.
5. 🔊 **Guía Completa del Flujo de Trabajo de ASR**: Abrimos todo para ayudarte a realizar tu sueño del reconocimiento de voz.
6. 🎙️ **Guía Completa del Flujo de Trabajo de TTS**: Desde lo básico hasta lo avanzado, completamente de código abierto sin reservaciones.
7. 📂 **Estructura Clara**: Anotaciones y documentación detalladas aseguran una incorporación sin problemas.
8. ⚡ **Cuantización de Modelos**: Reduce la barrera de uso y experimenta la magia de la IA en cualquier momento y lugar.
9. 🎥 **Tutoriales en Video**: ¡Síguenos para nuestros videos completos de introducción al proyecto!

# 🖼️ Capturas de Pantalla

|Original_7b_BoostBot|BoostBot-7b|
|:---:|:---:|
|<img src="./Assets/gif/Original_7b_BoostBot.gif" width="400">|<img src="./Assets/gif/BoostBot-7b.gif" width="400">|

|Original_7b_BanterBot|BanterBot-7b|
|:---:|:---:|
|<img src="./Assets/gif/Original_7b_BanterBot.gif" width="400">|<img src="./Assets/gif/BanterBot-7b.gif" width="400">|

# 🏗️ Diagrama de Arquitectura del Proyecto

![Project Architecture Diagram](Docs/pictures/FunGPT.png)



# 🧳 Colección de Modelos

| Modelo                          | Base                  | Tipo                       | Enlace                                                          |
| ------------------------------ | --------------------- | -------------------------- | ------------------------------------------------------------ |
| BanterBot-7b-chat              | internlm2_5_chat_7b   | Preentrenado + afinamiento QLoRA | [HuggingFace](https://huggingface.co/Alannikos768/BanterBot-7b-chat)<br/>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-7b-chat) |
| BoostBot-7b-chat               | internlm2_5_chat_7b   | Preentrenado + afinamiento QLoRA | [HuggingFace](https://huggingface.co/Alannikos768/BoostBot-7b-chat)<br/>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-7b-chat) |
| BanterBot_1_8b-chat            | internlm2_5_chat_1_8b | Preentrenado + afinamiento QLoRA | [HuggingFace](https://huggingface.co/Alannikos768/BanterBot_1_8b-chat)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-1_8b-chat) |
| BoostBot_1_8b-chat             | internlm2_5_chat_1_8b | Preentrenado + afinamiento QLoRA | [HuggingFace](https://huggingface.co/Alannikos768/BoostBot_1_8b-chat)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-1_8b-chat) |
| BanterBot-7b-chat-w4a16-4bit   | internlm2_5_chat_7b   | Preentrenado + afinamiento QLoRA + cuantización w4a16 | [HuggingFace](https://huggingface.co/Alannikos768/BanterBot-7b-chat-w4a16-4bit)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-7b-chat-w4a16-4bit) |
| BoostBot-7b-chat-w4a16-4bit    | internlm2_5_chat_7b   | Preentrenado + afinamiento QLoRA + cuantización w4a16 | [HuggingFace](https://huggingface.co/Alannikos768/BoostBot-7b-chat-w4a16-4bit)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-7b-chat-w4a16-4bit) |
| BanterBot_1_8b-chat-w4a16-4bit | internlm2_5_chat_1_8b | Preentrenado + afinamiento QLoRA + cuantización w4a16 | [HuggingFace](https://huggingface.co/Alannikos768/BanterBot_1_8b-chat-w4a16-4bit)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-1_8b-chat-w4a16-4bit) |
| BoostBot_1_8b-chat-w4a16-4bit  | internlm2_5_chat_1_8b | Preentrenado + afinamiento QLoRA + cuantización w4a16 | [HuggingFace](https://huggingface.co/Alannikos768/BoostBot_1_8b-chat-w4a16-4bit)<br>[OpenXLab](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-1_8b-chat-w4a16-4bit) |


# 📂 Estructura del Proyecto
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

# ⚡ Inicio Rápido
### 1. Entorno de Despliegue

- Sistema Operativo: Ubuntu 20.04.6 LTS
- CPU: Intel(R) Xeon(R) Platinum 8369B CPU @ 2.90GHz (Servidor GPU en Línea)
- GPU: NVIDIA A100-SXM4-80GB, NVIDIA-SMI 535.54.03, Versión del Controlador: 535.54.03, Versión de CUDA: 12.2
- Python: 3.10.0


### 2. Información Clave de Dependencias
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

### 3. Pasos de Despliegue

#### 3.1. Clonar el Código o Descargar Manualmente el Código para Colocarlo en el Servidor:

```shell
git clone https://github.com/Alannikos/FunGPT
```

#### 3.2. Configurar el Entorno de Python (Se Recomienda Usar Conda)

- Ingresar al directorio raíz del proyecto

```
cd FunGPT
```

- Crear un entorno conda

```
conda create -n FunGPT python==3.10.0
```

- Instalar bibliotecas de terceros
```
pip install -r requirements.txt

# Esto tomará aproximadamente 1 hora

```

#### 3.3 Descargar Modelos

##### 3.3.1 Modelos TTS (Requerido si se usa TTS)

- Instalar git-lfs
Dado que es necesario descargar archivos de modelos, asegúrese de que `git-lfs` ya esté instalado. Los usuarios de Linux pueden instalarlo con el siguiente comando:

```
apt install git-lfs
```

- Inicializar `LFS`
```
git lfs install
```
- Descargar el modelo TTS a la ruta especificada

```
# 1. Navegar al directorio específico
cd /FunGPT/TTS/weights

# 2. Descargar el modelo desde huggingface
git clone https://huggingface.co/2Noise/ChatTTS
```

- Para usuarios que no puedan acceder a HuggingFace, descargue desde el espejo

```
# 2. Descargar el modelo desde el espejo
git clone https://hf-mirror.com/2Noise/ChatTTS
```

##### 3.3.2 Modelos ASR (Requerido si se usa ASR)

Dado que es necesario descargar archivos de modelos, asegúrese de que `git-lfs` ya esté instalado. Los usuarios de Linux pueden instalarlo con el siguiente comando:


```
# Los usuarios que ya lo descargaron pueden ignorar este comando

apt install git-lfs
```

- Inicializar `LFS`
```
git lfs install
```

- Descargar el modelo ASR a la ruta especificada

```
# 1. Navegar al directorio específico
cd /FunGPT/ASR/weights

# 2. Navegar al directorio específico
git clone https://huggingface.co/FunAudioLLM/SenseVoiceSmall

```

- Para usuarios que no puedan acceder a HuggingFace, descargue desde el espejo

```
# 2. Descargar el modelo desde el espejo
git clone https://hf-mirror.com/FunAudioLLM/SenseVoiceSmall
```

##### 3.3.3 Modelos LLM (Requerido)
$\quad$ Para la selección de modelos LLM, ofrecemos muchas opciones. Los modelos con el mejor rendimiento son [BanterBot-7b-chat](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-7b-chat/tree/main) y [BoostBot-7b-chat](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-7b-chat/tree/main). Los modelos cuantizados también funcionan muy bien. Entre los modelos de 1_8B, el rendimiento también es bastante bueno. Para ahorrar tiempo de descarga, hemos elegido estos dos modelos de 1_8B: [BanterBot-1_8b-chat](https://openxlab.org.cn/models/detail/Alannikos/BanterBot-1_8b-chat/tree/main) y [BoostBot-1_8b-chat](https://openxlab.org.cn/models/detail/Alannikos/BoostBot-1_8b-chat/tree/main) como ejemplos, pero puede reemplazarlos según sea necesario.


- Inicializar `LFS`
```
git lfs install
```

- Descargar los modelos LLM a la ruta especificada

```
# 1. Navegar al directorio específico
cd /FunGPT/LLM/weights

# 2. Descargar el modelo BanterBot-1_8b-chat desde huggingface

https://huggingface.co/Alannikos768/BanterBot_1_8b-chat

# 3. Descargar el modelo BoostBot-1_8b-chat desde huggingface

https://huggingface.co/Alannikos768/BoostBot_1_8b-chat

```

- Para usuarios que no puedan acceder a HuggingFace, descargue desde OpenXLab

```

# 2. Descargar el modelo BanterBot-1_8b-chat desde OpenXLab (para usuarios en China)
git clone https://code.openxlab.org.cn/Alannikos/BanterBot-1_8b-chat.git

# 3. Descargar el modelo BoostBot-1_8b-chat desde OpenXLab (para usuarios en China)
git clone https://code.openxlab.org.cn/Alannikos/BoostBot-1_8b-chat.git
```


#### 3.4 Ejecutar el Script Web
```
conda activate FunGPT

streamlit run app.py --server.address=127.0.0.1 --server.port=7860
```

### 4. Experiencia del Modelo

- Si se ejecuta en un servidor remoto, se requiere reenvío de puerto
```
ssh -p 46411 user@ip -CNg -L 7860:127.0.0.1:7860 -o StrictHostKeyChecking=no
```

- Luego, para experimentar la aplicación

Abra su navegador, ingrese `http://127.0.0.1:7860` y haga clic en la interfaz correspondiente para experimentar `FunGPT`.

# 📚 Guía Detallada

### Guía de Generación de Datos
$\quad$ En el proceso de afinamiento de grandes modelos, podemos utilizar diversos algoritmos para SFT, ya sea mediante técnicas nativas como el afinamiento LoRA o utilizando herramientas empaquetadas como [Xtuner](https://github.com/InternLM/xtuner) y [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory). Necesitamos preparar datos de afinamiento de alta calidad. Sin embargo, el costo de la anotación manual de datos es relativamente alto, lo cual es ineficiente para la mayoría de los desarrolladores individuales. Por lo tanto, este proyecto utiliza [ChatGLM4-Flash](https://bigmodel.cn/), disponible gratuitamente de Zhipu, para generar los conjuntos de datos de diálogo multiturn que necesitamos. Este enfoque es simple y fácil de controlar. Generalmente, los conjuntos de datos generados pueden lograr resultados de afinamiento satisfactorios. Para la guía específica de generación de datos, puede consultar [data_generation](Data/BoostBot/scripts/generate_mutil_conv_chatglm.py).

$\quad$ En nuestra documentación, introduciremos principalmente el proceso de creación de un conjunto de datos de diálogo multiturn y cómo construir un conjunto de datos de autoconciencia. Con estas dos partes del conjunto de datos, básicamente puede afinar un modelo de lenguaje grande para tareas descendentes.

### Guía de Uso de LLM
$\quad$ El modelo de lenguaje grande es el componente central de este proyecto. Seleccionamos la serie de código abierto InternLM2.5 como modelo base. InternLM2.5 tiene fuertes capacidades de comprensión y generación, soporta una ventana de contexto de 8K y posee buenas capacidades de comprensión del idioma chino. En el despliegue real, utilizamos una versión cuantizada de 4 bits para reducir el consumo de recursos manteniendo el rendimiento del modelo. Para métodos detallados de despliegue y uso, consulte el documento [LLM_Usage](LLM/models/internlm2_5_7b_chat.py).

$\quad$ En este proyecto, el LLM es principalmente responsable de comprender la entrada del usuario y generar respuestas. También necesita manejar entradas multimodales y coordinarse con los módulos ASR y TTS.

### Guía de Uso de ASR
$\quad$ El módulo de reconocimiento de voz utiliza el modelo de código abierto SenseVoice, que posee excelentes capacidades de reconocimiento de voz multilingüe. El modelo soporta múltiples idiomas, incluyendo chino e inglés, con alta precisión y buena capacidad para manejar ruido de fondo. Para instrucciones específicas de despliegue y uso, consulte el documento [ASR_Usage](ASR/models/sensevoice.py).

$\quad$ En aplicaciones prácticas, el módulo ASR es responsable de convertir la entrada de voz del usuario en texto y pasarla al LLM para su procesamiento. Proporcionamos una interfaz de reconocimiento en streaming y soportamos transcripción de voz en tiempo real.

### Guía de Uso de TTS
$\quad$ El módulo de síntesis de voz utiliza el modelo de código abierto ChatTTS, que puede generar un habla natural y fluida. Utilizamos un modelo bilingüe para chino e inglés, soportando síntesis multivoz y parámetros ajustables como velocidad y timbre. Para métodos detallados de configuración y uso, consulte el documento [TTS_Usage](TTS/models/chattts.py).

$\quad$ El módulo TTS es principalmente responsable de convertir el texto generado por el LLM en salida de voz, soportando modo de síntesis por lotes. También proporcionamos una interfaz de control emocional que puede ajustar automáticamente el tono y el pitch según el contenido del texto para una salida más natural.

### Guía de Afinamiento de Modelos
$\quad$ Para satisfacer las necesidades de escenarios específicos, proporcionamos un proceso completo de afinamiento de modelos. Utilizamos principalmente métodos de afinamiento eficientes en parámetros como LoRA y QLoRA, que pueden entrenarse en tarjetas gráficas de consumo. El proceso de afinamiento utiliza la herramienta [Xtuner](https://github.com/InternLM/xtuner), que ofrece plantillas de configuración amigables y monitoreo integral del entrenamiento. Para procesos específicos de afinamiento y configuraciones de parámetros, consulte el documento [Xtuner_Usage](Finetune/BoostBot/internlm2_5_chat_7b_qlora_alpaca_e3_copy.py).

$\quad$ El afinamiento admite varios tipos de tareas como alineación de instrucciones, diálogo multiturn y role-playing. Proporcionamos scripts de preprocesamiento para convertir formatos de datos y también soportamos entrenamiento incremental para optimización adicional en modelos existentes.

### Guía de Cuantización de Modelos
$\quad$ La cuantización es un método de optimización importante para desplegar grandes modelos con recursos de computación limitados. Utilizamos la herramienta [LMDeploy](https://github.com/InternLM/lmdeploy) para la cuantización de modelos, soportando cuantización INT4 para reducir significativamente el uso de memoria mientras se mantiene el rendimiento del modelo. Para procesos detallados de cuantización, consulte el documento [LMDeploy_Usage](https://github.com/InternLM/lmdeploy).

$\quad$ El proceso de cuantización soporta cuantización de pesos y cuantización de valores de activación, y proporciona herramientas para verificar la precisión de los modelos cuantizados. LMDeploy también ofrece datos de comparación de rendimiento de diferentes estrategias de cuantización para ayudar a los usuarios a elegir el plan de cuantización más adecuado.


# 🔮 Planes de Desarrollo Futuro

1. - [x] ~~Grabación del Video del Proyecto~~
2. - [ ] Soporte para GPT-Sovits
3. - [ ] Soporte para acceso API a grandes modelos de lenguaje
4. - [ ] Mejorar la sección de la guía de generación de datos
5. - [ ] Mejorar la sección de uso de grandes modelos de lenguaje
6. - [ ] Refinar la sección de introducción del módulo de texto a voz
7. - [ ] Mejorar la sección de uso de reconocimiento de voz
8. - [x] ~~Añadir Módulo de Palabras Sensibles~~

# 🙏 Agradecimientos

Gracias a las siguientes herramientas y proyectos de código abierto por su soporte:

| Herramienta | Descripción |
|---|---|
| [InternLM-Tutorial](https://github.com/InternLM/Tutorial) | Un campamento de entrenamiento de grandes modelos activo y abierto |
| [Xtuner](https://github.com/InternLM/xtuner) | Herramienta para entrenamiento y afinamiento de modelos |
| [LMDeploy](https://github.com/InternLM/lmdeploy) | Herramienta para cuantización y despliegue de modelos |
| [Streamlit](https://streamlit.io/) | Herramienta para construir eficientemente aplicaciones de IA |
| [DeepSpeed](https://github.com/microsoft/DeepSpeed) | Herramienta para aceleración de entrenamiento e inferencia de modelos |
| [Pytorch](https://pytorch.org/) | Marco de trabajo de aprendizaje profundo ampliamente utilizado |

## Proyectos Relacionados

| Proyecto | Descripción |
|---|---|
| [InternLM](https://github.com/InternLM/InternLM) | Una serie de avanzados modelos de lenguaje grande de código abierto |
| [ChatTTS](https://github.com/2noise/ChatTTS) | Un proyecto de texto a voz de código abierto |
| [SenseVoice](https://github.com/FunAudioLLM/SenseVoice) | Un proyecto de reconocimiento de voz de código abierto de Alibaba |
| [LangGPT](https://github.com/langgptai/LangGPT) | Un proyecto de código abierto sobre indicaciones estructuradas. |
| [GangLLM](https://github.com/boss-mao/GangLLM) | Un proyecto de código abierto sobre interactuar con bromas y usuarios |
| [Linly-Talker](https://github.com/Kedreamix/Linly-Talker) | Un proyecto de código abierto sobre sistemas de inteligencia artificial |
| [Yanjie](https://github.com/Alannikos/Yanjie) | Un proyecto de código abierto para mejorar el aprendizaje del inglés con un asistente de IA |
| [wulewule](https://github.com/xzyun2011/wulewule) | Un proyecto de código abierto que presenta un asistente de IA con temática de Black Myth: Wukong |
| [ChatSensitiveWords](https://github.com/kaixindelele/ChatSensitiveWords/) | Un proyecto sobre Palabras Sensibles |

## Agradecimientos Especiales

| Organización | Descripción |
|---|---|
| [Shanghai Artificial Intelligence Laboratory](https://www.shlab.org.cn/) | Gracias por el soporte técnico y de plataforma |

# ⚖️ Descargo de Responsabilidad

$\quad$ Gracias por su interés y uso del proyecto FunGPT. Este proyecto tiene como objetivo proporcionar a los usuarios una experiencia de interacción agradable y atractiva. Tenga en cuenta los siguientes puntos:

- **Fines de Investigación**: El proyecto FunGPT y sus recursos asociados están destinados únicamente a fines de investigación académica y está estrictamente prohibido su uso comercial. Si se involucra algún código de terceros, por favor adhiérase estrictamente a su respectiva licencia de código abierto.

- **Precisión del Contenido Generado**: Debido a la influencia de factores como algoritmos de modelo, aleatoriedad y limitaciones de precisión de cuantización, FunGPT no puede garantizar la precisión o aplicabilidad del contenido generado. Por favor, tenga precaución y evalúe independientemente la idoneidad del contenido al utilizarlo.

- **Responsabilidad Legal**: Este proyecto no asume ninguna responsabilidad por la legalidad del contenido de salida del modelo y sus consecuencias. Los usuarios deben asegurarse de que su comportamiento cumpla con las leyes y regulaciones pertinentes y son responsables de los resultados de su uso.

$\quad$ Al utilizar FunGPT, indica que ha aceptado estos términos de descargo de responsabilidad. Esperamos que FunGPT pueda traer diversión y vitalidad a su vida diaria. Gracias por su soporte y uso.


## Historial de Estrellas

[![Star History Chart](https://api.star-history.com/svg?repos=Alannikos/FunGPT&type=Date)](https://star-history.com/#Alannikos/FunGPT&Date)
