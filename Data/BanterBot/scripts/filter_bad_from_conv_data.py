import json
import os
from tqdm import tqdm


def filter_bad_conversations(data):
    filtered_data = []
    
    for item in tqdm(data, desc="处理对话数据"):
        filtered_conversations = []
        
        for idx, conv in enumerate(item['conversation']):
            if (idx == 0):  # 跳过系统消息
                filtered_conversations.append(conv)
                continue

            bad_data = False

            if conv['input'] == "" or conv['output'] == "":
                bad_data = True

            
            if not bad_data:
                filtered_conversations.append(conv)
            else:
                print(conv)
                print("=======================")
    
        if filtered_conversations:
            filtered_item = item.copy()
            filtered_item['conversation'] = filtered_conversations
            filtered_data.append(filtered_item)

    return filtered_data

def main():
    # 配置路径
    input_file = "/FunGPT/Data/Kua_LLM/feasible_data/ft_data_all.json"
    output_file = "/FunGPT/Data/Dui_LLM/feasible_data/ft_data_all_filtered.json"
    
    # 2. 加载JSON数据
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"找不到输入文件: {input_file}")
        return
    except json.JSONDecodeError as e:
        print(e)
        return

    # 3. 执行过滤
    filtered_data = filter_bad_conversations(data)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=2)
        print(f"\n已将过滤后的数据保存到: {output_file}")
    except Exception as e:
        print(f"保存文件时出错: {str(e)}")

if __name__ == "__main__":
    main()