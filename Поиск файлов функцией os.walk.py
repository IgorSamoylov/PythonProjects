

import os

all_files = os.walk('C:/')

for path, subdirectories, file_names in all_files:
    for file_name in file_names:
        if file_name.endswith('.java') and file_name.find('recorder') != -1:
            print(path + file_name)
