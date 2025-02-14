import os
import subprocess

def get_project_structure(root_dir):
    """Ejecuta el comando 'tree -L 2' y devuelve el resultado como texto."""
    try:
        result = subprocess.run(["tree", "-L", "2", root_dir], capture_output=True, text=True)
        return result.stdout
    except FileNotFoundError:
        return "El comando 'tree' no está disponible. Instálalo o usa otro método."

def extract_text_from_file(file_path):
    """Lee el contenido de archivos de texto plano compatibles."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        return f"Error al leer {file_path}: {str(e)}"
