FROM python:3.12-alpine3.19
LABEL maintainer="gustavoleandrogorges@gmail.com"

# Essa variável de ambiente é usada para controlar se o Python deve 
# gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

# Define que a saída do Python será exibida imediatamente no console ou em 
# outros dispositivos de saída, sem ser armazenada em buffer.
# Em resumo, você verá os outputs do Python em tempo real.
ENV PYTHONUNBUFFERED 1

# Copia a pasta "djangoapp" e "scripts" para dentro do container.
COPY djangoapp /djangoapp
COPY scripts /scripts

# Entra na pasta djangoapp no container
WORKDIR /djangoapp

# A porta 8000 estará disponível para conexões externas ao container
# É a porta que vamos usar para o Django.
EXPOSE 8000

# Instala as dependências necessárias para compilar Pillow
RUN apk add --no-cache \
    build-base \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev \
    libimagequant-dev

# RUN executa comandos em um shell dentro do container para construir a imagem. 
# O resultado da execução do comando é armazenado no sistema de arquivos da 
# imagem como uma nova camada.
# Agrupar os comandos em um único RUN pode reduzir a quantidade de camadas da 
# imagem e torná-la mais eficiente.
# RUN python -m venv /venv && \
#     /venv/bin/pip install --upgrade pip && \
#     /venv/bin/pip install -r /djangoapp/requirements.txt && \
#     adduser --disabled-password --no-create-home duser && \
#     mkdir -p /data/web/static && \
#     mkdir -p /data/web/media && \
#     chown -R duser:duser /venv && \
#     chown -R duser:duser /data/web/static && \
#     chown -R duser:duser /data/web/media && \
#     chmod -R 777 /data && \
#     chmod -R 755 /data/web/static && \
#     chmod -R 755 /data/web/media && \
#     chmod  -R 755 /data/web/static/admin && \
#     chmod -R +x /scripts

# Cria e ativa o ambiente virtual
RUN python -m venv /venv

# Atualiza o pip
RUN /venv/bin/pip install --upgrade pip

# Instala as dependências do projeto
RUN /venv/bin/pip install -r /djangoapp/requirements.txt

# Cria os diretórios necessários e ajusta permissões
RUN mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    mkdir -p /data/web/static/admin && \
    chmod -R 777 /data/web/static && \
    chmod -R 777 /data/web/media && \
    chmod -R 777 /data/web/static/admin && \
    chmod -R +x /scripts

# Adiciona a pasta scripts e venv/bin 
# no $PATH do container.
ENV PATH="/scripts:/venv/bin:$PATH"

# Executa o arquivo scripts/commands.sh
CMD ["commands.sh"]