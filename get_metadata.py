from openslide import open_slide

def save_metadata_to_txt(svs_path, output_txt):
    try:
        slide = open_slide(svs_path)
        
        # Get basic properties
        properties = {
            "File Format": slide.detect_format(svs_path),
            "Dimensions": slide.dimensions,
            "Level Count": slide.level_count,
            "Objective Power": slide.properties.get("openslide.objective-power", "N/A"),
            # Add more properties as needed
        }

        # Save metadata to text file
        with open(output_txt, "w") as f:
            for key, value in properties.items():
                f.write(f"{key}: {value}\n")

        print(f"Metadata saved to {output_txt}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_image_path = "/app/data/643-1-19.svs"  # Update with your SVS file path
    output_txt_path = "/app/data/metadata.txt"     # Update with your desired output path

    save_metadata_to_txt(input_image_path, output_txt_path)
