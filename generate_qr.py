"""
生成“道昭通｜相因动态交互界面”的微信扫码二维码

使用方法：
1. 先把本项目部署到 GitHub Pages。
2. 将 WEB_URL 改成你的 GitHub Pages 真实地址。
3. 安装依赖：pip install qrcode[pil]
4. 运行：python generate_qr.py
5. 得到 dao_zhaotong_xiangyin_qr.png
"""

import qrcode

# 示例：
# WEB_URL = "https://yourusername.github.io/xiangyin/"
WEB_URL = "https://你的用户名.github.io/你的仓库名/"

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=12,
    border=4,
)

qr.add_data(WEB_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="#6b2a38", back_color="#f7dbe0")
img.save("dao_zhaotong_xiangyin_qr.png")

print("二维码已生成：dao_zhaotong_xiangyin_qr.png")
print("二维码链接：", WEB_URL)
