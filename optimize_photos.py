import os
import json
from PIL import Image

# Use paths relative to the script location
base_dir = os.path.dirname(os.path.abspath(__file__))
raw_dir = os.path.join(base_dir, "photos_raw")
out_dir = os.path.join(base_dir, "photos")

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

processed_files = []

# Max dimension for optimized images (helps save bandwidth and memory)
MAX_SIZE = 1200

if not os.path.exists(raw_dir):
    print(f"Error: The source folder '{raw_dir}' does not exist.")
    print("Please create a 'photos_raw' folder and put your images there first.")
    exit(1)

raw_files = [f for f in sorted(os.listdir(raw_dir)) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]

if not raw_files:
    print(f"No image files found in '{raw_dir}'.")
    exit(0)

for filename in raw_files:
    input_path = os.path.join(raw_dir, filename)
    base_name = os.path.splitext(filename)[0]
    output_filename = f"{base_name}.webp"
    output_path = os.path.join(out_dir, output_filename)
    
    try:
        with Image.open(input_path) as img:
            # Correct orientation if EXIF tag exists
            try:
                from PIL import ImageOps
                img = ImageOps.exif_transpose(img)
            except Exception:
                pass
            
            # Resize if larger than MAX_SIZE
            w, h = img.size
            if w > MAX_SIZE or h > MAX_SIZE:
                if w > h:
                    new_w = MAX_SIZE
                    new_h = int(h * (MAX_SIZE / w))
                else:
                    new_h = MAX_SIZE
                    new_w = int(w * (MAX_SIZE / h))
                img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            
            # Save as WebP
            img.save(output_path, "WEBP", quality=82)
            
            # Check digits count for categorizing
            digit_count = len(base_name)
            category = "unknown"
            if digit_count == 2:
                category = "sweet"
            elif digit_count == 3:
                category = "silly"
            elif digit_count == 4:
                category = "chaotic"
            
            processed_files.append({
                "original": filename,
                "optimized": f"photos/{output_filename}",
                "category": category,
                "name": base_name
            })
            print(f"Processed {filename} -> photos/{output_filename} ({category})")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Save manifest to easily inspect
manifest_path = os.path.join(out_dir, "manifest.json")
with open(manifest_path, "w") as f:
    json.dump(processed_files, f, indent=2)

print("\nAll done! Manifest written to photos/manifest.json")
