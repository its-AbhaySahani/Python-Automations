# extract zip files
import zipfile
import os

def extract_zip_file(zip_file, extract_dir):
    """Extracts a .zip file to the specified directory."""
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extractall(extract_dir)
    print(f"{zip_file} extracted successfully to {extract_dir}")

def main():
    # Specify the .zip file to extract and the directory to extract to
    zip_file = 'Abhay.zip'  # Replace with your .zip file
    extract_dir = 'extracted_files'  # Replace with the directory to extract to

    # Create the directory if it doesn't exist
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

    # Extract the .zip file
    extract_zip_file(zip_file, extract_dir)

if __name__ == '__main__':
    main()
