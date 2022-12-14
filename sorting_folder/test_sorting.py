import sorting_folder

import os
from pathlib import Path
import sys, shutil

EXTENSIONS = {
    "images": ('.jpeg', '.png', '.jpg', '.svg'),
    "video": ('.avi', '.mp4', '.mov', '.mkv'),
    "documents": ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
    "audio": ('.mp3', '.ogg', '.wav', '.amr'),
    "archives": ('.zip', '.gz', '.tar')
}


def clean(folder: Path):
    for file in folder.iterdir():
        if file.is_file():
            file = []
            if file.endswith(EXTENSIONS['images']):
                shutil.move(os.path.join(folder), file_destination)
                print(f'Image moved to "images": {file}')
            elif file.endswith(EXTENSIONS['video']):
                shutil.move(os.path.join(folder), file_destination)
                print(f'Video moved to "videos":[file})
            elif file.endswith(EXTENSIONS['documents']):
                shutil.move(os.path.join(folder), file_destination)
                print(f'Document moved to "documents":[file})
            elif file.endswith(EXTENSIONS['audio']):
                shutil.move(os.path.join(folder), file_destination)
                print(f'Audio moved to "audio":[file})
            elif file.endswith(EXTENSIONS['archives']):
                shutil.move(os.path.join(folder), file_destination)
                print(f'Archive moved to "archives":[file})
            sort_files(file, folder)

        # extracts the keys of the dictionary and compare to the existed
        elif file.name not in EXTENSIONS.keys():
            subfolder = file
# Get the list of all files and directories in current working directory, but the empty one. The rest remove.
            if not os.listdir(subfolder):
                # to remove or delete a empty directory
                shutil.rmtree(subfolder)
                return
            clean (subfolder)


def sort_files(file: Path, folder: Path):
    for folder_name, extensions in EXTENSIONS.items():
#to go through each file suffix and try to find extensions, which are
        if file.suffix in extensions:
            #concatenates the path with the given arguments
            new_folder = folder.joinpath(folder_name)
#create a new directory, to specify an existing directory without error by default it goes =False.
 #won't raise any exceptions if the directory exists.
            new_folder.mkdir(exist_ok=True)
# create a new file under a new name, normalize = removing first the suffix, the ending.
            new_file_name = normalize(file.name.removesuffix(file.suffix))
#then we add the above retrieved name and add it to the new folder with the separated suffix.
            new_file = file.rename(new_folder.joinpath(new_file_name + file.suffix))

            if folder_name == 'archives':
                archive_unpack(new_folder, new_file)

            break

    else:
        new_file_name = normalize(file.name.removesuffix(file.suffix))

        file.rename(folder.joinpath(new_file_name + file.suffix))


def normalize(file_name):
# everything should be in lower case.Removing the suffix, adding to a new file.name, and then
# we add the separated suffix.
    file.name = file.name.lower()
    new_file_name = normalize(file.name.removesuffix(file.suffix))
    file.rename(new_folder.joinpath(new_file_name + file.suffix))
    return file_name


def archive_unpack(folder: Path, file: Path):
#removing suffix
    archive_folder = folder.joinpath(file.name.removesuffix(file.suffix))
# creating a new directory without any raised exceptions
    archive_folder.mkdir(exist_ok=True)
# with shutil we unpack the archive and move it to a new location.
    shutil.unpack_archive(folder.joinpath(file), archive_folder)
    print("Archive file unpacked successfully.")

def main():
#'cause mainly all extensions are between 2-4 symbols, this is why we insert <2.
    if len(sys.argv) < 2:
        print('Enter path to folder which should be cleaned')
        exit()

    root_folder = Path(sys.argv[1])
#if either the root folder does not exist or there is no such directory,then
#we print a message "incorrect", and exit this if-condition.
    if (not root_folder.exists()) and (not root_folder.is_dir()):
        print('Path incorrect')



    clean(root_folder)

if __name__ == "__main__":
    main()

