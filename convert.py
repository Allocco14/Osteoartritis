from openslide import open_slide
from PIL import Image
import os

def convert_svs_to_png(input_path, output_path, tile_size, level):
    # Abre la imagen SVS
    slide = open_slide(input_path)
    
    # Crea el directorio de salida si no existe
    os.makedirs(output_path, exist_ok=True)
    
    # Obtiene dimensiones de la imagen en el nivel especificado
    width, height = slide.level_dimensions[level]
    
    tiles_x = width // tile_size + 1
    tiles_y = height // tile_size + 1

    # Itera sobre las tiles y las guarda como PNG
    for i in range(0, width, tile_size):
        for j in range(0, height, tile_size):
            print(f"{i//width} de {tiles_x} y {j//height} de {tiles_y}")
            region = slide.read_region((i * (2 ** level), j * (2 ** level)), level, (tile_size, tile_size))
            region = region.convert("RGB")
            output_file = os.path.join(output_path, f"tile_{i}_{j}_level_{level}.png")
            region.save(output_file, "PNG")
            

if __name__ == "__main__":
    input_image_path = r"/app/data/643-1-19.svs"  # Usa la 'r' para indicar una cadena cruda en Windows
    output_directory = r"/app/data/output/"
    tile_size = 1024  # Puedes ajustar este valor según tus necesidades
    target_level = 1  # Nivel al que deseas acceder, ajusta según tus necesidades

    convert_svs_to_png(input_image_path, output_directory, tile_size, target_level)
