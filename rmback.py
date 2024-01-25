import os
import sys
import argparse
from rembg import remove
import tkinter as tk
from tkinter import filedialog

def remove_background(input_path, output_path):
    with open(input_path, "rb") as input_file:
        input_data = input_file.read()
    output_data = remove(input_data)
    with open(output_path, "wb") as output_file:
        output_file.write(output_data)

def process_folder(input_folder):
    files = os.listdir(input_folder)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    for file in image_files:
        input_path = os.path.join(input_folder, file)
        output_path = input_path
        remove_background(input_path, output_path)
        print(f"Fondo eliminado y archivo reemplazado: {output_path}")

def open_folder_dialog():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Seleccione la carpeta de entrada")
    return folder_path

def main():
    parser = argparse.ArgumentParser(description='Eliminar fondo de imágenes en una carpeta.')
    parser.add_argument('--input_folder', type=str, help='Ruta de la carpeta de entrada')

    args = parser.parse_args()

    if args.input_folder:
        input_folder = args.input_folder
    else:
        input_folder = open_folder_dialog()

    if not os.path.exists(input_folder):
        print("Error: La carpeta de entrada especificada no existe.")
        sys.exit(1)

    process_folder(input_folder)
    print("Proceso completado.")

    another_folder = input("¿Desea procesar otra carpeta? (Sí/No): ").lower()
    if another_folder.startswith('s'):
        main()
    else:
        print("Programa cerrado.")

if __name__ == "__main__":
    main()
