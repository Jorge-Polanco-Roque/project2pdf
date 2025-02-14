from setuptools import setup, find_packages

setup(
    name="project2pdf",  # Nombre del paquete en PyPI
    version="0.3.6",  # Versión inicial
    packages=find_packages(),  # Busca automáticamente todos los paquetes
    install_requires=[
        "fpdf>=1.7.2",  # Dependencias necesarias
    ],
    entry_points={
        "console_scripts": [
            "project2pdf=scripts.generate_pdf:main",  # Permite ejecutarlo desde CLI
        ],
    },
    author="Jorge Polanco",
    author_email="jorge.polanco@tec.mx",
    description="Generate a project structures and files in a single pdf file.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tuusuario/project2pdf",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
