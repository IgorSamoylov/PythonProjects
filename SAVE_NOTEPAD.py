
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
import os

with open("RESOURCES/dropbox_token.txt", "r", encoding="UTF-8") as f:
    DROPBOX_TOKEN = f.read()

LOCAL_FILES_PATH = 'C:/Users/A12/Desktop/БЛОКНОТЫ ПРОГРАММИРОВАНИЕ/'
BACKUP_FILE_PATH = '/БЛОКНОТЫ ПРОГРАММИРОВАНИЕ/' # Путь, по которому будет идти сохранение внутри каталога dropbox
dbx_object = None

def backup(path: str, file_name: str):
    """Сохраняет файл по переданному пути в Dropbox по BACKUP_FILE_PATH"""
    file = path + file_name
    with open(file, 'rb') as f: # Чтение файла происходит в двоичном формате - флаг 'rb'
        print('Uploading', file)
        try:
            dbx_object.files_upload(f.read(), BACKUP_FILE_PATH + file_name, mode=WriteMode('overwrite'))
        except ApiError as err:
        # This checks for the specific error where a user doesn't have
        # enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()
        else:
            print("Success!")

def backup_files(path: str):
    print(f"Starting upload files in {path}...")
    for current_path, subdirectories, file_list in os.walk(path):
        for file_name in file_list:
            backup(current_path, file_name)

#def backup_rar_java_projects(path: str, file_name: str):
#    os.system(f'rar a {path} {path + file_name}')

#import asyncio
#async def backup_files_async(path: str):
#    for current_path, subdirectories, file_list in os.walk(path):
#        for file_name in file_list:
 #           backup(current_path, file_name)

def dropbox_dao(TOKEN: str):
    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox DAO object...")
    with dropbox.Dropbox(TOKEN) as dbx_object:

        # Check that the access token is valid
        try:
            dbx_object.users_get_current_account()
        except AuthError:
            sys.exit("ERROR: Invalid access token; try re-generating an "
                    "access token from the app console on the web.")
    print("DAO object created!")
    return dbx_object


dbx_object = dropbox_dao(DROPBOX_TOKEN)
backup_files(LOCAL_FILES_PATH)
print('The files was succesfuly loaded!')

#JAVA_PROJECTS_PATH = 'C:/Users/A12/IdeaProjects/'
#backup_rar_java_projects(JAVA_PROJECTS_PATH)


#backup('C:/Users/A12/Desktop/БЛОКНОТЫ ПРОГРАММИРОВАНИЕ/PYTHON.txt')
    
