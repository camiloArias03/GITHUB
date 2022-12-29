import secrets

password = secrets.token_hex(8)  # Genera una contraseña de 16 caracteres
print(password)
