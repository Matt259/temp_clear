import os
import shutil
import send2trash


def delete_files(files: str, root: str) -> None:
    for file in files:
        file_path = os.path.join(root, file)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Failed to delete file: {file_path} - {e}")


def delete_directory(dirs: str, root: str) -> None:
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        try:
            shutil.rmtree(dir_path)
        except Exception as e:
            print(f"Failed to delete directory: {dir_path} - {e}")
            
            
def main() -> None:
    DIRS_TO_CLEAR: tuple[str] = (os.environ.get('TEMP'), 'C:\Windows\Prefetch', 'C:\Windows\Temp', os.path.join(os.path.expanduser("~"), 'Downloads'))
    
    for dir_to_clear in DIRS_TO_CLEAR:
        
        if dir_to_clear and os.path.exists(dir_to_clear):
            for root, dirs, files in os.walk(dir_to_clear):
                delete_files(files, root)
                delete_directory(dirs, root)

    send2trash.send2trash('C:\\$Recycle.Bin')
    
    
if __name__ == "__main__":
    main()
    
    
