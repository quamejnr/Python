import zipfile

# writing into the zipfile
# To compress a zipfile we pass compression=zipfile.ZIP_DEFLATED as an argument
with zipfile.ZipFile('zipfile.zip', 'w') as my_zip:  # creating a zipfile

    # placing files in a zip folder
    my_zip.write('list.txt')
    my_zip.write('new_file.csv')

# Extracting zip files
with zipfile.ZipFile('zipfile.zip', 'r') as my_zip:
    my_zip.extractall('new_file')
