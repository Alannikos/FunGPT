import json
import os
from tqdm import tqdm

def load_sensitive_words(folder_path):
    """
    从指定文件夹中加载所有txt文件的敏感词
    每个文件每行一个敏感词
    """
    sensitive_words = set()  # 使用集合去重
    
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"敏感词文件夹不存在: {folder_path}")
    
    # 遍历文件夹中的所有txt文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # 读取每行，去除空白字符，并添加到集合中
                    words = {line.strip() for line in f if line.strip()}
                    sensitive_words.update(words)
                print(f"已加载敏感词文件: {filename}")
            except Exception as e:
                print(f"加载文件 {filename} 时出错: {str(e)}")
    
    return list(sensitive_words)  # 转换回列表

def filter_sensitive_conversations(data, sensitive_words):
    filtered_data = []
    
    for item in tqdm(data, desc="处理对话数据"):
        filtered_conversations = []
        
        for idx, conv in enumerate(item['conversation']):
            if (idx == 0):  # 跳过系统消息
                filtered_conversations.append(conv)
                continue

            try:
                text_to_check = f"{conv['input']} {conv['output']}"
            except:
                # print(conv)
                continue
            contains_sensitive = False
            which_sensitive_word = ""

            for word in sensitive_words:
                if word in text_to_check.lower():
                    contains_sensitive = True
                    which_sensitive_word = word
                    break
            
            if not contains_sensitive:
                filtered_conversations.append(conv)
            else:
                # print(which_sensitive_word)
                # print(conv)
                print("=======================")

    
        if filtered_conversations:
            filtered_item = item.copy()
            filtered_item['conversation'] = filtered_conversations
            filtered_data.append(filtered_item)

    return filtered_data

def main():
    # 配置路径
    sensitive_words_folder = "/FunGPT/Data/Dui_LLM/sensitive_words/words"
    input_file = "/FunGPT/Data/Kua_LLM/sample/multi_conversation_1.jsonl"
    output_file = "/FunGPT/Data/Dui_LLM/feasible_data/ft_data_1_filtered.json"
    
    # 1. 加载敏感词
    try:
        sensitive_words = load_sensitive_words(sensitive_words_folder)
        print(f"总共加载了 {len(sensitive_words)} 个敏感词")
    except Exception as e:
        print(f"加载敏感词失败: {str(e)}")
        return

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
    filtered_data = filter_sensitive_conversations(data, sensitive_words)

    # 4. 保存过滤后的数据
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=2)
        print(f"\n已将过滤后的数据保存到: {output_file}")
    except Exception as e:
        print(f"保存文件时出错: {str(e)}")

if __name__ == "__main__":
    main()