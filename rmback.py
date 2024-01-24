import os
import sys
import argparse
from rembg import remove

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

def main():
    parser = argparse.ArgumentParser(description='Eliminar fondo de imágenes en una carpeta.')
    parser.add_argument('input_folder', type=str, help='Ruta de la carpeta de entrada')
    args = parser.parse_args()

    input_folder = args.input_folder

    if not os.path.exists(input_folder):
        print("Error: La carpeta de entrada especificada no existe.")
        sys.exit(1)

    process_folder(input_folder)
    print("Proceso completado.")

if __name__ == "__main__":
    main()
