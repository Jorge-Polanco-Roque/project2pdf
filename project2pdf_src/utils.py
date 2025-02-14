import os
import platform
import subprocess

def ensure_tree_installed():
    """
    Checks if 'tree' is installed. If not, attempts to install it automatically
    on Linux, macOS, or Windows. Falls back if the OS or installation method is unsupported.
    """
    if is_tree_available():
        return True

    # Try OS-specific installations
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

def is_tree_available():
    """Checks if 'tree' is already installed by calling 'tree --version'."""
    try:
        subprocess.run(["tree", "--version"], capture_output=True, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def install_tree_linux():
    """Attempts to install 'tree' on Linux using apt-get or yum/dnf if apt-get is unavailable."""
    try:
        if which("apt-get"):
            print("🔧 Installing 'tree' on Linux (apt-get)...")
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            subprocess.run(["sudo", "apt-get", "install", "-y", "tree"], check=True)
            return True
        elif which("yum"):
            print("🔧 Installing 'tree' on Linux (yum)...")
            subprocess.run(["sudo", "yum", "install", "-y", "tree"], check=True)
            return True
        elif which("dnf"):
            print("🔧 Installing 'tree' on Linux (dnf)...")
            subprocess.run(["sudo", "dnf", "install", "-y", "tree"], check=True)
            return True
        else:
            print("⚠️ No known package manager found (apt-get, yum, or dnf). Using fallback method.")
            return False
    except Exception as e:
        print(f"⚠️ Failed to install 'tree' on Linux: {e}. Using fallback method.")
        return False

def install_tree_macos():
    """Attempts to install 'tree' on macOS using Homebrew."""
    try:
        if which("brew"):
            print("🍏 Installing 'tree' on macOS using Homebrew...")
            subprocess.run(["brew", "install", "tree"], check=True)
            return True
        else:
            print("⚠️ Homebrew is not installed. Using fallback method.")
            return False
    except Exception as e:
        print(f"⚠️ Failed to install 'tree' on macOS: {e}. Using fallback method.")
        return False

def install_tree_windows():
    """Attempts to install 'tree' on Windows using Chocolatey."""
    try:
        if which("choco"):
            print("🟦 Installing 'tree' on Windows using Chocolatey...")
            subprocess.run(["choco", "install", "-y", "tree"], check=True)
            return True
        else:
            print("⚠️ Chocolatey is not installed. Using fallback method.")
            return False
    except Exception as e:
        print(f"⚠️ Failed to install 'tree' on Windows: {e}. Using fallback method.")
        return False

def which(cmd):
    """Cross-platform equivalent of the 'which' command to check if a program is in the PATH."""
    from shutil import which
    return which(cmd)

def get_project_structure(root_dir):
    """
    Returns the directory structure using the 'tree' command if possible;
    otherwise, uses Python-based fallback.
    """
    # Attempt to install or confirm 'tree'
    installed = ensure_tree_installed()
    if installed and is_tree_available():
        # 'tree' is available: run it
        try:
            result = subprocess.run(["tree", "-L", "2", root_dir],
                                    capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            print(f"⚠️ Error running 'tree': {e}. Using fallback.")
            return generate_tree_fallback(root_dir)
    else:
        # Fallback if 'tree' is missing or installation failed
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
    except FileNotFoundError:
        tree_output += f"{prefix}🚫 [Directory Not Found]\n"

    return tree_output

def extract_text_from_file(file_path):
    """Reads the content of compatible text files."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        return f"Error reading {file_path}: {str(e)}"
