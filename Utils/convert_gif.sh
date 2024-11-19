#!/bin/bash

if [ ! -d "/root/Project_FunGPT/FunGPT/Assets/video" ]; then
    echo "错误：输入文件夹 'a' 不存在"
    exit 1
fi

mkdir -p gif

total_files=$(ls -1 /root/Project_FunGPT/FunGPT/Assets/video/*.mp4 2>/dev/null | wc -l)

if [ $total_files -eq 0 ]; then
    echo "错误：在 'a' 文件夹中没有找到MP4文件"
    exit 1
fi

echo "找到 $total_files 个MP4文件需要处理"
echo "开始转换..."

# 计数器
count=0

for video in /root/Project_FunGPT/FunGPT/Assets/video/*.mp4; do
    [ -f "$video" ] || continue
    
    filename=$(basename "$video" .mp4)
    
    count=$((count + 1))
    
    echo "正在处理 ($count/$total_files): $filename.mp4"
    
    ffmpeg -i "$video" \
           -vf "fps=20,scale=1080:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
           -loop 0 \
           "/root/Project_FunGPT/FunGPT/Assets/gif/$filename.gif" \
           -hide_banner \
           -loglevel warning
    
    if [ $? -eq 0 ]; then
        echo "✓ 成功转换: $filename.gif"
    else
        echo "✗ 转换失败: $filename.mp4"
    fi
done

echo "转换完成！"
echo "成功处理了 $count 个文件"
echo "输出文件保存在 'gif' 文件夹中"