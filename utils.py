# utils.py
# Nossa "caixa de ferramentas" com funções úteis reutilizáveis.

import os
import uuid # Biblioteca para gerar identificadores únicos.

def save_image_upload(upload_field, subfolder):
    """
    Processa um arquivo de imagem enviado por um formulário.
    - upload_field: O objeto do arquivo vindo do 'request.files'.
    - subfolder: A pasta de destino dentro de 'static/uploads/' (ex: 'escudos' ou 'jogadores').
    """
    # Se nenhum arquivo foi enviado, não faz nada.
    if not upload_field:
        return None

    # Monta o caminho completo da pasta de destino.
    upload_dir = os.path.join('static', 'uploads', subfolder)
    # Se a pasta de destino não existir (ex: /static/uploads/escudos), ela é criada.
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Separa o nome do arquivo da sua extensão (ex: 'foto' e '.png').
    name, ext = os.path.splitext(upload_field.filename)
    # Validação simples para garantir que é um tipo de imagem comum.
    if ext.lower() not in ('.png', '.jpg', '.jpeg', '.gif', '.webp'):
        return None 

    # Gera um nome de arquivo único usando UUID.
    # Isso evita que o upload de um 'neymar.jpg' substitua outro 'neymar.jpg' já existente.
    unique_filename = f"{uuid.uuid4()}{ext}"
    save_path = os.path.join(upload_dir, unique_filename)

    # Salva o arquivo no disco do servidor.
    upload_field.save(save_path)

    # Retorna o caminho relativo que será salvo no banco de dados e usado no HTML.
    return f'/static/uploads/{subfolder}/{unique_filename}'