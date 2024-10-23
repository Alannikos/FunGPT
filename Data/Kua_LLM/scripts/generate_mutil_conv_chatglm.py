import os
import re 
import sys
import json
import logging  
from zhipuai import ZhipuAI
sys.path.append("/root/Project_FunGPT/Developing/")

from LLM.templates.template import Template

"""
数据格式：

    [
        {
            "conversation": [
                {
                    "system": "",
                    "input": "xxx",
                    "output": "xxx"
                },
                {
                    "input": "xxx",
                    "output": "xxx"
                }
            ]
        },
    ...
    ]
"""

class MyChatGLM:
    def __init__(self, api_key):
        self.model_name = 'GLM4'
        self.model = ZhipuAI(api_key=api_key)  # 请填写自己的APIKey

    def generate(self, question="我最近有点不开心，别人说我长得有点丑"):
        response = self.model.chat.completions.create(
            model="glm-4",
            messages=[
                {"role": "system", "content": Template.KUA_GENERATE_DATA_TEMPLATE},
                {"role": "user", "content": f'''
                目标: 1. 请生成""{question}""为场景的连续多轮对话记录
                      2. 严格遵循, 请以如下格式返回生成的数据, 只返回JSON格式，json模板:  
                            [  
                                {{
                                    "input":"AAA","output":"BBBB" 
                                }}
                            ] 
                         其中input字段表示正常提问者, output字段表示马屁精'''},
            ]
        )
        return response

def postprocessing(conversation_data):
    # 数据后处理
    conversation_data = json.loads(conversation_data.choices[0].message.content)
    # print("type: ", type(conversation_data))
    # print(conversation_data);exit()

    result = {"conversation": []}
    
    for idx, data in enumerate(conversation_data):
        if idx == 0:
            data['system'] = Template.KUA_GENERATE_DATA_TEMPLATE
        result["conversation"].append(data)

    return result

def save_dialogue_to_jsonl(data):
    # 将数据保存为JSONL文件
    with open('/root/Project_FunGPT/Developing/Data/Kua_LLM/sample/multi_conversation.jsonl', 'w', encoding='utf-8') as f:
        
        # for item in data:
        #     json_str = json.dumps(item, ensure_ascii=False)
        #     f.write(json_str + '\n')
        
        # 如果需要把数据外面的[]也保存到jsonl文件中，就直接把数据dump进目标文件，否则就是上面这种形式
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    # 1. 生成LLM对象
    my_model = MyChatGLM(api_key='xxx')

    # 多轮对话数据列表（元素是一个对话记录）
    res = []

    # 2. 遍历获取到的每个问题
    with  open("/root/Project_FunGPT/Developing/Data/Kua_LLM/raw/question.txt",  "r") as f:
        # 依次读取每一行数据
        for question in f:
            question = question.strip()

            if question:
                # 3. 生成回复
                conversation_data = my_model.generate(question)
                # 4. 后处理
                washed_data = postprocessing(conversation_data=conversation_data)
                res.append(washed_data)

    # 5. 保存数据
    save_dialogue_to_jsonl(res)

if __name__ == "__main__":
    main()
