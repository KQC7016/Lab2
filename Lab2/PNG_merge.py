import pandas as pd
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pathlib import Path
import os

# Load the dataset
relative_data_path = Path('Lab2_Datasets') / 'Lab2d_power.csv'
data_driver_bin = str(relative_data_path.resolve())
data = pd.read_csv(data_driver_bin)

# 将时间列设置为索引
data['Datetime'] = pd.to_datetime(data['Datetime'])
data.set_index('Datetime', inplace=True)

# 图片类别
image_categories = ['Histogram', 'Box_Plot', 'Density_Plot', 'Daily_Mean_Values', 'Monthly_Mean_Values']

# 循环处理每一类图片
for category in image_categories:
    # 打开多张PNG图片
    images = [Image.open(f'PNG/{category}_of__{column}.png') for column in data.columns]

    # 计算每张图片的大小
    widths, heights = zip(*(i.size for i in images))

    # 计算九宫格拼接后的图片大小
    max_width = max(widths)
    max_height = max(heights)
    new_width = 3 * max_width
    new_height = 3 * max_height

    # 创建新的空白图片
    new_image = Image.new('RGB', (new_width, new_height), color='white')

    # # 将前缀名称绘制在左上角
    # prefix_image = Image.new('RGB', (max_width, max_height), color='white')
    # draw = ImageDraw.Draw(prefix_image)
    # font = ImageFont.truetype("arial.ttf", 100)
    # # draw.text((max_width/2, new_height/2), category, fill='black', font=font)
    # draw.text((5, 5), category, fill='black', font=font)
    # new_image.paste(prefix_image, (0, 0))

    # 创建前缀名称图像
    prefix_image = Image.new('RGB', (max_width, max_height), color='white')
    draw = ImageDraw.Draw(prefix_image)
    font_size = 100
    font = ImageFont.truetype("arial.ttf", font_size)
    text = category
    # 获取文本的边界框
    bbox = draw.textbbox((0, 0), text, font=font)
    # 计算边界框的尺寸
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # 自动调整字体大小以适应图像宽度
    while text_width > max_width - 10:  # 保留一些空间
        font_size -= 5
        font = ImageFont.truetype("arial.ttf", font_size)
        # 获取文本的边界框
        bbox = draw.textbbox((0, 0), text, font=font)
        # 计算边界框的尺寸
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

    # 计算文字绘制位置
    x = (max_width - text_width) // 2
    y = (max_height - text_height) // 2

    # 绘制文字，自动换行
    draw.text((x, y), text, fill='black', font=font)

    # 将前缀名称图像粘贴到新图像的左上角
    new_image.paste(prefix_image, (0, 0))

    # 将每张图片粘贴到九宫格对应位置
    x_offset = max_width  # 留白位置
    y_offset = 0  # 留白位置
    for img in images:
        new_image.paste(img, (x_offset, y_offset))
        x_offset += max_width
        if x_offset == 3 * max_width:
            x_offset = 0
            y_offset += max_height

    # 创建保存图像的文件夹
    if not os.path.exists('PNG/Combined'):
        os.makedirs('PNG/Combined')

    # 保存拼接后的图片
    new_image.save(f'PNG/Combined/Combined_Grid_{category}.png')
