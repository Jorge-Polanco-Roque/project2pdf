import os
from fpdf import FPDF
from .utils import get_project_structure, extract_text_from_file

class PDFGenerator:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_section(self, title, content):
        """Agrega una sección con título y contenido al PDF."""
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(0, 10, title.encode('latin-1', 'replace').decode('latin-1'), ln=True, align='L')
        self.pdf.ln(5)
        self.pdf.set_font("Courier", '', 10)
        self.pdf.multi_cell(0, 5, content.encode('latin-1', 'replace').decode('latin-1'))

    def generate_pdf(self, input_dir, output_path):
        """Genera un PDF con la estructura del proyecto y el contenido de archivos compatibles."""
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 14)
        self.pdf.cell(0, 10, "Estructura del Proyecto", ln=True, align='C')
        self.pdf.ln(10)
        self.pdf.set_font("Courier", '', 10)
        self.pdf.multi_cell(0, 5, get_project_structure(input_dir).encode('latin-1', 'replace').decode('latin-1'))

        valid_extensions = {".py", ".ipynb", ".tsx", ".js", "dockerfile", ".env", ".ignore", ".md"}
        for root, _, files in os.walk(input_dir):
            for file in files:
                if any(file.lower().endswith(ext) for ext in valid_extensions) or file.lower() in {"dockerfile", ".env", ".gitignore"}:
                    file_path = os.path.join(root, file)
                    content = extract_text_from_file(file_path)
                    relative_path = os.path.relpath(file_path, input_dir)
                    self.add_section(f"📂 {relative_path}", content)

        self.pdf.output(output_path)
