import os
import subprocess

def get_project_structure(root_dir):
    """Executes the 'tree -L 2' command and returns the result as text."""
    try:
        result = subprocess.run(["tree", "-L", "2", root_dir], capture_output=True, text=True)
        return result.stdout
    except FileNotFoundError:
        return "The 'tree' command is not available. Install it or use another method."

def extract_text_from_file(file_path):
    """Reads the content of compatible text files."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        return f"Error reading {file_path}: {str(e)}"
