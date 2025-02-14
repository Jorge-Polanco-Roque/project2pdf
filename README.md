# 📄 project2pdf

**Convert project structures into a single PDF.**
Perfect for providing context to an LLM (Large Language Model) about a specific project.

## 🚀 Features
✅ **Automatically detects projects** in the root directory  
✅ **Generates a structured PDF** with directory trees and code snippets  
✅ **Supports multiple file types** (`.py`, `.ipynb`, `.tsx`, `.js`, `Dockerfile`, `.env`, `.md`, `.gitignore`)  
✅ **No manual input needed** – just run and get your documentation  

## 📦 Installation

Install `project2pdf` from [PyPI](https://pypi.org/project/project2pdf/):

```sh
pip install project2pdf
```

## 🛠 Usage
Simply run the command inside your project directory:

```sh
project2pdf
```

This will:
- Detect all project folders in the root directory
- Generate a structured PDF for each project
- Save the output in the root as `project_name_documentation.pdf`

## 📝 Example Output
After running `project2pdf`, you will find a PDF file like:

```
📂 my_project_documentation.pdf
```

## 🔧 Configuration
No additional configuration is needed. The script will:
- Include the first two levels of the directory structure
- Extract relevant code from supported files
- Format everything in a clean, readable PDF

## 👨‍💻 Supported File Types
The tool processes and includes the following file types:
- `.py`, `.ipynb` → Python scripts & Jupyter Notebooks
- `.tsx`, `.js` → TypeScript/JavaScript files
- `Dockerfile`, `.env`, `.gitignore` → Project metadata
- `.md` → Markdown documentation

## 📌 Use Cases
🔹 **Quickly onboard new developers** to a project  
🔹 **Document your project** before sharing it with an LLM  
🔹 **Organize and archive** project structures  

## 💡 Example
If your project structure is:

```
my_project/
│── src/
│   ├── main.py
│   ├── utils.py
│── README.md
│── requirements.txt
│── .gitignore
```

`project2pdf` will generate `my_project_documentation.pdf` with:
1. **Project structure** (`tree -L 2` output)
2. **Code snippets** from `main.py`, `utils.py`, etc.
3. **Metadata** from `.gitignore`, `requirements.txt`, etc.

## 🔥 Why Use This?
- **Automates project documentation** 📑
- **Saves time onboarding new team members** ⏳
- **Enhances LLMs' understanding of project context** 🤖

## 🌍 License
MIT License. Free to use and modify!

## 📬 Feedback & Contributions
Have ideas or found a bug? Open an issue or contribute on [GitHub](https://github.com/your-repo/project2pdf)!