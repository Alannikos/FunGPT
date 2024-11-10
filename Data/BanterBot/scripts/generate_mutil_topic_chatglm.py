import os
import re 
import sys
import json
import random
import logging
from tqdm import tqdm
from zhipuai import ZhipuAI
sys.path.append("/FunGPT")

from LLM.templates.template import Template


class MyChatGLM:
    def __init__(self, api_key):
        self.model_name = 'GLM4'
        self.model = ZhipuAI(api_key=api_key)  # 请填写自己的APIKey

    def generate(self, key_word="讽刺"):
        response = self.model.chat.completions.create(
            # model="glm-4",
            model="glm-4-plus",
            messages=[
                {"role": "system", "content": Template.Dui_TOPIC_GENERATE_DATA_TEMPLATE},
                {"role": "user", "content": f'''
                目标: 1. 请生成一个和""{key_word}""这句话最符合的场景，只生成场景。
                    2. 你需要结合这句话思考最合适的场景，同时确保生成的场景多样化。
                    3. 请保证这个场景的质量，只生成一个场景。
                    4. 具有强烈反对意图，带有故意贬低或讽刺的意味。
                    5. 请保证场景简洁且真实，无需出现特定地点限制。
                    6. 请勿使用明显的人物代名词。
                    7. 请注意是你发现了某件事，然后你使用上面这句话讽刺他的场景。
                    8. 严格遵循规则: 请严格以如下格式返回生成的数据, 确保只返回JSON格式，json模板:
                    {{"场景": "AAA"}}
                    其中AAA代表对应关键字的场景'''},
  
            ]
        )
        return response

def postprocessing(topic_data):
    # 数据后处理
    try:
        topic_data = json.loads(topic_data.choices[0].message.content.replace("```json","").replace("```",""))
    except Exception  as exception:
        logging.error("解析json异常:%s, 内容：%s",str(exception), topic_data.choices[0].message.content)
        return {"场景": "在朋友谈论最近的电影时，小刚反驳道：“你觉得结尾好？那简直就是毫无逻辑！”"}

    return topic_data

def save_question_to_json(data):
    # 将数据保存为JSONL文件
    with open('FunGPT/Data/Dui_LLM/raw/scene.json', 'w', encoding='utf-8') as f:
        
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

    with open('FunGPT/Data/Dui_LLM/raw/key_word.txt', 'r', encoding='utf-8') as file:
        lines_list = file.readlines()
        # 去掉每行末尾的换行符
        keywords = [line.strip() for line in lines_list]

    # 进行循环生成
    for count in tqdm(range(1000)):
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