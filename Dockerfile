# Usa imagem oficial Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos para dentro do container
COPY . .

# Instala dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expõe a porta padrão do Flask
EXPOSE 8080

# Comando para iniciar o app com gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "application:application"]