# Telegram bot promo
Bot automatizado para salvar e enviar promoções em tempo real utilizando de Python e a API do Telegram

# Contexto
Na busca de um novo monitor, desenvolvi um bot para que fosse mais fácil encontrar promoções de produtos específicos, nesse caso, monitores. Transformando dados não estruturados de mensagens em alertas no meu próprio celular.

Com o desenvolvimento do projeto foi pensado em uma forma simplês e eficiente de separar os diferentes produtos-alvo, com isso foi criado um roteamento multicanais inteligente via JSON. Nada mais é que direcionar as ofertas de produtos para um grupo que corresponde à que tipo de produto estou buscando.

Além disso, todas as ofertas agora são salvas em uma base de dados e geram um arquivo em formato CSV, visando futuros dashboards e analises para encontrar lojas com históricos bons e produtos com preços ainda melhores.

# Tecnologias 
* Python 3.12
* Telethon (Interface com Telegram API)
* Python dotenv (Segurança das minhas credenciais)
* JSON para gerenciamento das palavras-chave 

# Passo a Passo
- Clone o repositório.
- Crie um ambiente virtual: 'python3 -m -venv .venv'
- Instale as dependências: 'pip install -r requiriments.txt'
- Configure com suas chaves no arquivo '.env' .