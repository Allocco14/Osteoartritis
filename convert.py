from openslide import open_slide
from PIL import Image
import os
from tqdm import tqdm
import time
from multiprocessing import Pool, cpu_count

def convert_tile(tile_info):
    input_path, output_path, level, tile_size, i, j = tile_info
    slide = open_slide(input_path)
    region = slide.read_region(
        (i * (2 ** level), j * (2 ** level)), level, (tile_size, tile_size))
    region = region.convert("RGB")
    output_file = os.path.join(output_path, f"tile_{i}_{j}_level_{level}.png")
    region.save(output_file, "PNG")

def convert_svs_to_png(input_path, output_path, tile_size, level):
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    # Get dimensions of the image at the specified level
    slide = open_slide(input_path)
    width, height = slide.level_dimensions[level]
    tiles_x = width // tile_size + 1
    tiles_y = height // tile_size + 1
    total = tiles_x * tiles_y
    start_time = time.time()
    tile_info_list = []
    for i in range(0, width, tile_size):
        for j in range(0, height, tile_size):
            tile_info_list.append((input_path, output_path, level, tile_size, i, j))
    # Multiprocessing
    with Pool(cpu_count()) as p:
        print(p, cpu_count())
        with tqdm(total=total) as pbar:
            for _ in p.imap_unordered(convert_tile, tile_info_list):
                pbar.update(1)
    end_time = time.time()
    print(f"Total time: {end_time - start_time} seconds")

if __name__ == "__main__":
    tile_size = 1024  # You can adjust this value according to your needs
    target_level = 0  # Level you want to access, adjust as needed
    # Use 'r' to indicate a raw string in Windows
    filename = "202-19"
    input_image_path = r"/app/data/" + filename + ".svs"
    output_directory = f"/app/data/output/{target_level}_{tile_size}/"
    convert_svs_to_png(input_image_path, output_directory,
                       tile_size, target_level)
