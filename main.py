import os
import json
import csv
from dotenv import load_dotenv
from datetime import datetime
from telethon import TelegramClient, events


#Forçar o Python a olhar para a pasta onde este arquivo main.py está
basedir = os.path.abspath(os.path.dirname(__file__))
env_path = os.path.join(basedir, '.env')
json_path = os.path.join(basedir, 'keywords.json')

load_dotenv(env_path)
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Ler o arquivo JSON
with open(json_path, 'r', encoding='utf-8') as f:
    dicionario_keywords = json.load(f)

print(f"DEBUG: API_ID carregado: {api_id}")

client = TelegramClient('sessao_felipe', api_id, api_hash)

print('Bot iniciado 2! Monitorando os grupos de promoção')
 
@client.on(events.NewMessage)
async def my_event_handler(event):
    # ESPIÃO 1: Verifica se o bot está a reagir a novas mensagens
    print(f"👀 MENSAGEM RECEBIDA: {event.raw_text}")

    message_text = event.raw_text.lower()
    categorias_encontradas = None
    chat_destino = None

    # ESPIÃO 2: Verifica o que ele carregou do ficheiro JSON
    print(f"📂 Lendo JSON... Categorias disponíveis: {list(dicionario_keywords.keys())}")

    try:
        for categoria, dados in dicionario_keywords.items():
            # 1. Pega a lista, não importa se você escreveu 'keywords' ou 'palavras' no JSON
            lista_busca = dados.get('keywords') or dados.get('palavras')
            
            if lista_busca:
                # 2. Força a palavra do JSON a ficar minúscula na hora da comparação
                if any(str(palavra).lower() in message_text for palavra in lista_busca):
                    categorias_encontradas = categoria
                    chat_destino = dados['destino']
                    print(f"🎯 MATCH ENCONTRADO! Categoria: {categoria} | Destino: {chat_destino}")
                    break
            else:
                print(f"⚠️ Aviso: A categoria '{categoria}' não tem uma lista de palavras configurada no JSON.")
                
    except Exception as e:
        print(f"❌ ERRO NO LOOP: {e}")

    if categorias_encontradas:
        chat = await event.get_chat()
        nome_chat = chat.title if hasattr(chat, 'title') else 'Privado/Desconhecido' 

        agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        texto_limpo = event.raw_text.replace('\n', ' | ')

        with open('historico de produtos.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow([agora, nome_chat, categorias_encontradas, texto_limpo])

        print(f"✅ A enviar notificação para o grupo {chat_destino}...")
        
        await client.send_message(
            chat_destino, 
            f'🚨 OPORTUNIDADE - {categorias_encontradas.upper()}:\nGrupo: {nome_chat}\n\n{event.raw_text}'
        )

with client:
    client.run_until_disconnected()