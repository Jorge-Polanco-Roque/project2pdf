import os
import argparse
from project2pdf.pdf_generator import PDFGenerator

def main():
    parser = argparse.ArgumentParser(description="Convierte archivos de un proyecto a PDF.")
    parser.add_argument("input_dir", help="Directorio raíz del proyecto a documentar")
    parser.add_argument("output_pdf", help="Ruta del archivo PDF de salida")

    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output_pdf), exist_ok=True)
    
    pdf_generator = PDFGenerator()
    pdf_generator.generate_pdf(args.input_dir, args.output_pdf)

    print(f"✅ PDF generado en: {args.output_pdf}")

if __name__ == "__main__":
    main()
