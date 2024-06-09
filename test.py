#本代码由luffer-bot倾情打造，需要进行某些其他用途请联系1324117277@qq.com
#谢谢各位了

import os

# 确保目录存在
os.makedirs('./ttf', exist_ok=True)

from PIL import Image, ImageDraw, ImageFont
# 字体文件路径（确保字体文件已下载并放在项目目录中）
font_paths = [
    "./.ttf/NiShiWoDeKeAiBaoBei-2.ttf",
    "./.ttf/NiShiWoDeXingXingTang-2.ttf",
    "./.ttf/NiShiWoWeiYiShouXuan-2.ttf",
    "./.ttf/SanJiMingYuanXingShu-2.ttf",
    "./.ttf/SanJiZeLinKaiShu-2.ttf"
]

# 字体大小
font_size = 20

# 加载字体
fonts = [ImageFont.truetype(font_path, font_size) for font_path in font_paths]

# 创建图像
final_image = Image.new("RGB", (800, 1200), "white")
final_draw = ImageDraw.Draw(final_image)

# 手写内容
text = """
文字填在这里
"""

# 切换字体函数
def draw_text_with_multiple_fonts(draw, text, fonts, start_pos, line_height):
    lines = text.strip().split('\n')
    y = start_pos[1]
    font_index = 0

    for line in lines:
        draw.text((start_pos[0], y), line, font=fonts[font_index], fill="black")
        y += line_height
        font_index = (font_index + 1) % len(fonts)

# 写入图像
draw_text_with_multiple_fonts(final_draw, text, fonts, (10, 10), 30)

# 保存为图片
final_image_path = "./ttf/final.png"
final_image.save(final_image_path)

# 保存为PDF
final_pdf_path = "./ttf/final.pdf"
final_image.save(final_pdf_path, "PDF", resolution=100.0)

print("图片保存为: ", final_image_path)
print("PDF保存为: ", final_pdf_path)
