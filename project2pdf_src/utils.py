import os
import subprocess

def ensure_tree_installed():
    """Checks if 'tree' is installed; if not, installs it (Linux only)."""
    try:
        subprocess.run(["tree", "--version"], capture_output=True, check=True)
    except FileNotFoundError:
        if os.name == "posix":  # Linux/macOS
            print("🔧 Installing 'tree' package...")
            subprocess.run(["apt-get", "install", "-y", "tree"], check=True)
        else:
            print("⚠️ The 'tree' command is not available. Using fallback method.")

def get_project_structure(root_dir):
    """Returns the directory structure using 'tree' if available; otherwise, uses os.walk."""
    try:
        # Ensure 'tree' is installed before running it
        ensure_tree_installed()
        result = subprocess.run(["tree", "-L", "2", root_dir], capture_output=True, text=True)
        return result.stdout
    except (FileNotFoundError, subprocess.CalledProcessError):
        # If 'tree' is not available, use fallback method
        return generate_tree_fallback(root_dir)

def generate_tree_fallback(directory, max_depth=2, current_depth=0, prefix=""):
    """Generates a simple tree-like structure if 'tree' is not available."""
    if current_depth >= max_depth:
        return ""

    tree_output = ""
    try:
        entries = sorted(os.listdir(directory))
        for entry in entries:
            path = os.path.join(directory, entry)
            if os.path.isdir(path):
                tree_output += f"{prefix}📂 {entry}/\n"
                tree_output += generate_tree_fallback(path, max_depth, current_depth + 1, prefix + "  ")
            else:
                tree_output += f"{prefix}📄 {entry}\n"
    except PermissionError:
        tree_output += f"{prefix}🚫 [Access Denied]\n"

    return tree_output

def extract_text_from_file(file_path):
    """Reads the content of compatible text files."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        return f"Error reading {file_path}: {str(e)}"
