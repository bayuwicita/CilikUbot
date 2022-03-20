import os

from PIL import Image, ImageDraw, ImageFont
from userbot.utils import cilik_cmd, edit_delete, text_set



@cilik_cmd(pattern="writer(?: |$)(.*)")
async def writer(event):
    if event.reply_to:
        reply = await event.get_reply_message()
        text = reply.message
    elif event.pattern_match.group(1).strip():
        text = event.text.split(maxsplit=1)[1]
    else:
        return await edit_delete(event, "Berikan Beberapa Teks Juga")
    k = await event.edit_or_reply("Sedang Memproses..")
    img = Image.open("resources/kertas.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("resources/assfont.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "cilik.jpg"
    img.save(file)
    await event.reply(file=file)
    os.remove(file)
    await k.delete()
