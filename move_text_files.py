import os
import shutil

def move_txt_files(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    for filename in os.dirname(target_dir):
        if filename.endswith('.txt'):
            source = os.path.join(source_dir, path_name)
            source = os.path.join(target_dir,filename)

            shutil.move(source,target)
            print(f"Moved: {filename}")

source_directory = '/path/to/source/directory'
target_directory = '/path/to/target/directory'
move_txt_files(source_directory, target_directory)