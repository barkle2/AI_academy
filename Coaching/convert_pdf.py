import subprocess
import os

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
base_dir = r"d:\Workspace\AI_academy\AI_academy\Coaching"
output_dir = os.path.join(base_dir, "pdf")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 01_데이터_개념_
prefix = "01_데이터_개념_"

print(f"Starting conversion in {base_dir}")

for i in range(1, 24):
    num = f"{i:02d}"
    html_file = os.path.join(base_dir, f"{prefix}{num}.html")
    pdf_file = os.path.join(output_dir, f"{prefix}{num}.pdf")
    
    if os.path.exists(html_file):
        print(f"Converting {prefix}{num}.html to pdf...")
        # Use absolute path and replace backslashes for file URL
        file_url = f"file:///{os.path.abspath(html_file).replace('\\', '/')}"
        
        try:
            subprocess.run([
                chrome_path,
                "--headless",
                f"--print-to-pdf={pdf_file}",
                "--no-margins",
                "--paper-width=13.33",
                "--paper-height=7.5",
                file_url
            ], check=True)
            print(f"Successfully converted to {prefix}{num}.pdf")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {prefix}{num}.html: {e}")
    else:
        print(f"File not found: {html_file}")

print("PDF Conversion process finished.")
