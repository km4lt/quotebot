import discord
from image_generator import create_quote_image, cleanup_image

intents = discord.Intents.default()
intents.message_content = True  
intents.members = True 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
   
    if message.author == client.user:
        return

    if message.reference: 
        referenced_message = await message.channel.fetch_message(message.reference.message_id)
        
        # Check if the bot is mentioned in the reply
        if client.user.mentioned_in(message):
            # The user who sent the original message (your friend)
            friend = referenced_message.author  
            text = referenced_message.content 

            if text:
                display_name = friend.display_name  
                avatar_url = str(friend.display_avatar.url) 
                
                image_path = create_quote_image(text, display_name, avatar_url)
                await message.channel.send(file=discord.File(image_path))
                cleanup_image(image_path)


client.run(token)
