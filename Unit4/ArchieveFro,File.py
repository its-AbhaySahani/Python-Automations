import zipfile
import tarfile
import os

def create_zip_archive(archive_name, files):
    """Creates a .zip archive from the list of files."""
    with zipfile.ZipFile(archive_name, 'w') as zipf:
        for file in files:
            if os.path.isfile(file):
                zipf.write(file)
                print(f"Added {file} to {archive_name}")
            else:
                print(f"File {file} does not exist and will be skipped.")
    print(f"{archive_name} created successfully.")

def create_tar_gz_archive(archive_name, files):
    """Creates a .tar.gz archive from the list of files."""
    with tarfile.open(archive_name, 'w:gz') as tar:
        for file in files:
            if os.path.isfile(file):
                tar.add(file)
                print(f"Added {file} to {archive_name}")
            else:
                print(f"File {file} does not exist and will be skipped.")
    print(f"{archive_name} created successfully.")

def main():
    # List of files to include in the archive
    files_to_archive = ['file1.txt', 'file2.txt', 'file3.txt']  # Replace with your file names

    # Choose the archive type
    archive_format = input("Choose the archive format ('zip' or 'tar.gz'): ").strip().lower()
    archive_name = input("Enter the name for the archive (e.g., 'archive_name'): ").strip()

    # Append appropriate file extension
    if archive_format == 'zip':
        archive_name += '.zip'
        create_zip_archive(archive_name, files_to_archive)
    elif archive_format == 'tar.gz':
        archive_name += '.tar.gz'
        create_tar_gz_archive(archive_name, files_to_archive)
    else:
        print("Invalid archive format. Please choose either 'zip' or 'tar.gz'.")

if __name__ == '__main__':
    main()
