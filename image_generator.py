from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
from io import BytesIO
import os


def create_quote_image(quote_text, username, avatar_url):
    
    if not os.path.exists('assets'):
        os.makedirs('assets')

   
    response = requests.get(avatar_url)
    avatar_img = Image.open(BytesIO(response.content)).convert('RGB')
    avatar_img = avatar_img.resize((600, 600)).filter(ImageFilter.GaussianBlur(15))

    
    img = Image.new('RGB', (600, 600), color=(73, 109, 137))
    draw = ImageDraw.Draw(img)

    
    img.paste(avatar_img, (0, 0))

    
    quote_font = ImageFont.truetype("arial.ttf", 40)  
    username_font = ImageFont.truetype("arial.ttf", 30)  

    
    quote_bbox = draw.textbbox((0, 0), quote_text, font=quote_font)
    username_bbox = draw.textbbox((0, 0), f"- {username}", font=username_font)

 
    padding = 50 
    line_spacing = 10  
    
    max_width = 540

    
    lines = []
    current_line = ""
    for word in quote_text.split():
        test_line = f"{current_line} {word}".strip()
        test_line_bbox = draw.textbbox((0, 0), test_line, font=quote_font)
        if test_line_bbox[2] - test_line_bbox[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    total_height = sum(draw.textbbox((0, 0), line, font=quote_font)[3] - draw.textbbox((0, 0), line, font=quote_font)[1] for line in lines) + (line_spacing * (len(lines) - 1))

    
    quote_position_y = (img.height // 2) - (total_height // 2) - 20  
    for line in lines:
        line_bbox = draw.textbbox((0, 0), line, font=quote_font)
        quote_position_x = (img.width - (line_bbox[2] - line_bbox[0])) // 2
        draw.text((quote_position_x, quote_position_y), line, font=quote_font, fill=(255, 255, 255))
        quote_position_y += line_bbox[3] - line_bbox[1] + line_spacing  

    username_position = (
        (img.width - (username_bbox[2] - username_bbox[0])) // 2,
        quote_position_y + padding // 2
    )

    draw.text(username_position, f"- {username}", font=username_font, fill=(255, 255, 255))

    image_path = f'assets/{username}_quote.png'
    img.save(image_path)

    return image_path

def cleanup_image(image_path):
    if os.path.exists(image_path):
        os.remove(image_path)
        print(f"Deleted image: {image_path}")
