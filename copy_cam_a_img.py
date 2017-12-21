# copies images(CAM A) from source to destination
import os
import shutil
import re
# source and destination paths
source = os.path.join(os.path.expanduser('~'), 'datasets', 'all')
#source = r'U:\datasets\all'

destination_flech_loch = os.path.join(os.path.expanduser('~'), 'datasets', 'flech_loch')
#destination_loch = 'U:\datasets\loch'
#destination_ok = 'U:\datasets\ok'
# list files in a source directory
source_files = os.listdir(source)
# loop through the source
for file_name in source_files:
    # if re.match(r'l.+camA_.+',file_name):
    #     # join the src and file name
    #     full_file_name = os.path.join(source, file_name)
    #     # check if it is file and then copy to the destination path
    #     if os.path.isfile(full_file_name):
    #         shutil.copy(full_file_name, destination_loch)

    if re.match(r'fl.+camA_.+', file_name):
        full_file_name = os.path.join(source, file_name)
        # check if it is file and then copy to the destination path
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, destination_flech_loch)

