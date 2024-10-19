import os
import re 
import sys
import json
import random
import logging
from tqdm import tqdm
from zhipuai import ZhipuAI
sys.path.append("/root/Project_FunGPT/Developing/")

from LLM.templates.template import Template


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
                {"role": "user", "content": f'''
                目标: 1. 请生成""{key_word}""为主题的场景
                      2. 确保生成的场景多样化，有趣味性，有脾气
                      3. 请保证质量，只生成一个场景，并且场景的主人公为：'你'
                      4. 严格遵循规则: 请严格以如下格式返回生成的数据, 确保只返回JSON格式，json模板:  
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
        return {"场景": "在马拉松比赛中坚持跑完全程，观众为你的毅力而欢呼。"}

    return topic_data

def save_question_to_json(data):
    # 将数据保存为JSONL文件
    with open('/root/Project_FunGPT/Developing/Data/Kua_LLM/raw/question_100_plus.json', 'w', encoding='utf-8') as f:
        
        # for item in data:
        #     json_str = json.dumps(item, ensure_ascii=False)
        #     f.write(json_str + '\n')

        # 如果需要把数据外面的[]也保存到jsonl文件中，就直接把数据dump进目标文件，否则就是上面这种形式
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    # 1. 生成LLM对象
    my_model = MyChatGLM(api_key='479dc4c9611acd56f0b7981f126a3411.tNS782K8hcuk1UeO')

    # 场景数据集合
    res = []

    keywords = ['创新',
                '领导力',
                '团队合作',
                '适应性',
                '专注',
                '热情',
                '耐心',
                '诚信',
                '坚韧',
                '乐观',
                '同理心',
                '责任感',
                '自律',
                '效率',
                '沟通',
                '决策',
                '学习',
                '适应',
                '专注',
                '激励',
                '考试失利',
                '感情不顺',
                '发生矛盾',
                '误解',
                '担心',
                '失望',
                '压力大',
                "成长",
                "勇气",
                "变化",
                "信任",
                "感恩",
                "创造力",
                "灵活性",
                "情绪管理",
                "说服力",
                "团队精神",
                "危机处理",
                "方向感",
                "协作",
                "机遇",
                "竞争",
                "成就感",
                "满足",
                "反思",
                "内省",
                "友谊",
                "偏见",
                "独立性",
                "承诺",
                "内疚",
                "羞愧",
                "焦虑",
                "倦怠",
                "挑战",
                "坚持",
                "信心",
                "魅力",
                "责任心",
                "可靠性",
                "优先级",
                "目标设定",
                "冒险",
                "兼容性",
                "稳定性",
                "和解",
                "韧性",
                "乐趣",
                "自我价值",
                "好奇心",
                "开放性",
                "社交能力",
                "负责任",
                "妥协",
                "承受力",
                "信服",
                "目标",
                "包容",
                "决心",
                "直觉",
                "自信",
                "慷慨",
                "团结",
                "感知",
                "冷静",
                "协同",
                "适应能力",
                "毅力",
                "宽容",
                "倾听",
                "忠诚",
                "欣赏",
                "演讲",
                "表达",
                "机智",
                "公正",
                "持久力",
                "勤奋",
                "领导",
                "内在动机",
                "灵感",
                "识别",
                "洞察力",
                "远见",
                "策略",
                "同情心",
                "聪颖",
                "信念",
                "增长",
                "毅然",
                "情感",
                "责任意识",
                "坚毅",
                "宽心",
                "可持续性",
                "克服",
                "儒雅",
                "欣快",
                "启发",
                "自省",
                "尊重",
                "审慎",
                "灵魂",
                "思维",
                "管理",
                "幸福感",
                "乐观主义",
                "独创性",
                "围绕",
                "精确",
                "贪婪",
                "幽默感",
                "细心",
                "协商",
                "容忍",
                "远虑",
                "勇敢",
                "规范",
                "怀疑",
                "无畏",
                "警惕",
                "耐力",
                "忠诚度",
                "自动性",
                "细致",
                "宁静",
                "果断",
                "追求",
                "敏锐",
                "机智",
                "展望",
                "觉察",
                "探究",
                "观察力",
                "分辨力",
                "公义",
                "强韧",
                "乐观精神",
                "支持",
                "自发性",
                "流畅",
                "渗透力",
                "慎重",
                "协调",
                "理智",
                "争议",
                "自主",
                "可靠",
                "圆融",
                "激昂",
                "公平",
                "悟性",
                "灵敏",
                "毅力",
                "丰富",
                "包容性",
                "孤独",
                "失落",
                "悲伤",
                "忧虑",
                "怯懦",
                "烦恼",
                "无助",
                "迷茫",
                "怀疑自我",
                "孤立",
                "绝望",
                "挫败感",
                "痛苦",
                "怨恨",
                "压抑",
                "懊悔",
                "恐惧",
                "脆弱",
                "沮丧",
                "苦涩",
                "困惑",
                "不安",
                "冷漠",
                "妒忌",
                "憎恨",
                "迷失",
                "不满",
                "悲观",
                "冷酷",
                "质疑",
                "窘迫",
                "混乱",
                "鄙夷",
                "疲惫",
                "羞辱",
                "不确定",
                "焦躁",
                "不幸",
                "忧愁",
                "乏味",
                "抱怨",
                "失意",
                "困苦",
                "悔恨",
                "痛楚",
                "压迫感",
                "微不足道",
                "不值得",
                "心灰意冷"
            ]

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