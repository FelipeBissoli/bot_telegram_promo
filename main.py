import os
import json
from dotenv import load_dotenv
from telethon import TelegramClient, events


#Força o Python a olhar para a pasta onde este arquivo main.py está
basedir = os.path.abspath(os.path.dirname(__file__))
env_path = os.path.join(basedir, '.env')
json_path = os.path.join(basedir, 'keywords.json')

load_dotenv(env_path)
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Ler o arquivo JSON
with open('keywords.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)
dados['keywords'] = [i.lower() for i in dados['keywords']]
lista_keywords = dados['keywords']

print(f"DEBUG: API_ID carregado: {api_id}")

client = TelegramClient('sessao_felipe', api_id, api_hash)

print('Bot iniciado! Monitorando os grupos de promoção')

@client.on(events.NewMessage)
async def my_event_handler(event):
    # Converter tudo para minúsculo para facilitar a busca
    message_text = event.raw_text.lower()

    # Verificar se alguma palavra-chave está na mensagem
    if any(key in message_text for key in lista_keywords):
        print(f'Produto detectado!!!')
        # Enviar a mensagem para o meu "Mensagens Salvas" no Telegram
        await client.send_message('me', f'OPORTUNIDADE DE MONITOR:\n\n{event.raw_text}')

with client:
    client.run_until_disconnected()