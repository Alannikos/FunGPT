import os
import re 
import sys
import json
import random
import logging
from tqdm import tqdm
from zhipuai import ZhipuAI

sys.path.append("/root/Project_FunGPT/FunGPT/")
from LLM.templates.template import Template
from Utils.configs import Config


class MyChatGLM:
    def __init__(self, api_key):
        self.model_name = 'GLM4'
        self.model = ZhipuAI(api_key=api_key)  # 请填写自己的APIKey

    def generate(self, key_word="团队合作"):
        response = self.model.chat.completions.create(
            # model="glm-4",
            model="glm-4-plus",
            messages=[
                {"role": "system", "content": Template.TOPIC_GENERATE_DATA_TEMPLATE},
                {"role": "user", "content": f''''''},
            ]
        )
        return response

def postprocessing(topic_data):
    # 数据后处理
    try:
        topic_data = json.loads(topic_data.choices[0].message.content.replace("```json","").replace("```",""))
    except Exception  as exception:
        logging.error("解析json异常:%s, 内容：%s",str(exception), topic_data.choices[0].message.content)
        return {"场景": "在马拉松比赛中坚持跑完全程，观众为你的毅力而欢呼。"}

    return topic_data

def save_question_to_json(data):
    # 将数据保存为JSONL文件
    with open(Config.PROJECT_PATH / 'Data/Kua_LLM/raw/question_100_plus.json', 'w', encoding='utf-8') as f:
        
        # for item in data:
        #     json_str = json.dumps(item, ensure_ascii=False)
        #     f.write(json_str + '\n')

        # 如果需要把数据外面的[]也保存到jsonl文件中，就直接把数据dump进目标文件，否则就是上面这种形式
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    # 1. 生成LLM对象
    my_model = MyChatGLM(api_key='xxx')

    # 场景数据集合
    res = []

    keywords = []

    # 进行循环生成
    for count in tqdm(range(100)):
        # 2. 随机获取一个关键字
        key_word = keywords[random.randint(0, len(keywords) - 1)]
        
        if key_word:
            # 3. 生成以关键字为导向的场景
            scene = my_model.generate(key_word)
            
            # 4. 后处理
            print(scene)
            washed_data = postprocessing(scene)
            res.append(washed_data)

    # 5. 保存数据
    save_question_to_json(res)

if __name__ == "__main__":
    main()