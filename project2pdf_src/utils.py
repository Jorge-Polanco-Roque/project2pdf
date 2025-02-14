import os
import subprocess
import platform

def ensure_tree_installed():
    """Checks if 'tree' is installed; if not, installs it (Linux/macOS/Windows)."""
    try:
        subprocess.run(["tree", "--version"], capture_output=True, check=True)
        return True
    except FileNotFoundError:
        os_system = platform.system()

        if os_system == "Linux":
            return install_tree_linux()
        elif os_system == "Darwin":  # macOS
            return install_tree_macos()
        elif os_system == "Windows":
            return install_tree_windows()
        else:
            print("⚠️ Unsupported OS. Using fallback method.")
            return False

def install_tree_linux():
    """Attempts to install 'tree' on Linux using apt-get."""
    try:
        print("🔧 Installing 'tree' on Linux...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "tree"], check=True)
        return True
    except Exception as e:
        print(f"⚠️ Failed to install 'tree' on Linux: {e}. Using fallback method.")
        return False

def install_tree_macos():
    """Attempts to install 'tree' on macOS using Homebrew."""
    try:
        print("🍏 Installing 'tree' on macOS using Homebrew...")
        subprocess.run(["brew", "install", "tree"], check=True)
        return True
    except Exception as e:
        print(f"⚠️ Failed to install 'tree' on macOS: {e}. Using fallback method.")
        return False

def install_tree_windows():
    """Attempts to install 'tree' on Windows using Chocolatey."""
    try:
        print("🟦 Installing 'tree' on Windows using Chocolatey...")
        subprocess.run(["choco", "install", "-y", "tree"], check=True)
        return True
    except Exception as e:
        print(f"⚠️ Failed to install 'tree' on Windows: {e}. Using fallback method.")
        return False

def get_project_structure(root_dir):
    """Returns the directory structure using 'tree' if available; otherwise, falls back to os.walk."""
    if ensure_tree_installed():
        try:
            result = subprocess.run(["tree", "-L", "2", root_dir], capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            return f"Error running 'tree' command: {str(e)}"
    
    # Fallback if 'tree' is missing
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
