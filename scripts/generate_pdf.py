import os
from project2pdf.pdf_generator import ProjectPDFGenerator

def main():
    """Automatically detects projects in the root directory and generates PDFs without requiring parameters."""
    root_dir = os.getcwd()  # Use the current directory as the root
    generator = ProjectPDFGenerator(root_dir)
    generator.generate_pdf()

if __name__ == "__main__":
    main()
