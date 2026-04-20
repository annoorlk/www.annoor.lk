import os
from PIL import Image

# Settings
INPUT_FOLDER = "images_uncompressed"
OUTPUT_FOLDER = "images"
QUALITY = 70        # 0-100 (lower = more compression)
MAX_WIDTH = 1200    # Resize width (None to skip)

# Create output folder
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def compress_image(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            # Convert PNG with transparency properly
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Resize if needed
            if MAX_WIDTH and img.width > MAX_WIDTH:
                ratio = MAX_WIDTH / float(img.width)
                new_height = int(img.height * ratio)
                img = img.resize((MAX_WIDTH, new_height), Image.LANCZOS)

            # Save compressed image
            img.save(output_path, "JPEG", quality=QUALITY, optimize=True)

            print(f"Compressed: {input_path} -> {output_path}")

    except Exception as e:
        print(f"Error processing {input_path}: {e}")

# Process all images in folder
for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_file = os.path.splitext(filename)[0] + ".jpg"
        output_path = os.path.join(OUTPUT_FOLDER, output_file)

        compress_image(input_path, output_path)

print("✅ Done compressing images.")