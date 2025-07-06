# utils.py
import os
import uuid # Biblioteca para gerar nomes únicos.

def save_image_upload(upload_field, subfolder):
    """
    Salva um arquivo de imagem enviado pelo usuário em uma pasta específica
    e retorna o caminho relativo para ser salvo no banco de dados.
    """
    # Se nenhum arquivo foi enviado, não faz nada.
    if not upload_field:
        return None

    # Define o caminho completo da pasta de destino.
    upload_dir = os.path.join('static', 'uploads', subfolder)
    # Se a pasta não existir (ex: /static/uploads/escudos), ela é criada.
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Pega o nome e a extensão do arquivo original.
    name, ext = os.path.splitext(upload_field.filename)
    # Validação simples para garantir que é uma imagem.
    if ext.lower() not in ('.png', '.jpg', '.jpeg', '.gif', '.webp'):
        return None 

    # Gera um nome de arquivo único usando UUID para evitar que dois arquivos com o
    # mesmo nome (ex: 'foto.jpg') se sobreponham.
    unique_filename = f"{uuid.uuid4()}{ext}"
    save_path = os.path.join(upload_dir, unique_filename)

    # Salva o arquivo no disco do servidor.
    upload_field.save(save_path)

    # Retorna o caminho que será usado no HTML (ex: /static/uploads/escudos/...).
    return f'/static/uploads/{subfolder}/{unique_filename}'