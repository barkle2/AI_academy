from html2image import Html2Image
import os

# Initialize with a dedicated output directory
output_dir = 'images_hti'
hti = Html2Image(output_path=output_dir)

base_dir = r"d:\Workspace\AI_academy\AI_academy\Coaching"
prefix = "01_데이터_개념_"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f"Starting html2image conversion in {base_dir}")

for i in range(1, 24):
    num = f"{i:02d}"
    html_file = os.path.join(base_dir, f"{prefix}{num}.html")
    output_name = f"{prefix}{num}.png"
    
    if os.path.exists(html_file):
        print(f"Converting {prefix}{num}.html to image...")
        # html2image screenshot method: html_file can be a path to a local file
        # size=(1280, 720) ensures the correct aspect ratio and resolution
        try:
            hti.screenshot(html_file=html_file, save_as=output_name, size=(1280, 800))
            print(f"Successfully saved {output_name}")
        except Exception as e:
            print(f"Error converting {prefix}{num}.html: {e}")
    else:
        print(f"File not found: {html_file}")

print("html2image Conversion process finished.")
