from werkzeug.datastructures import FileStorage 
from storedoc import LocalStorage

# Initilialize local storage
localClient = LocalStorage()

# The FileStorage class is a thin wrapper over incoming files.
# It is used by the request object to represent uploaded files
file = FileStorage(open('path/to/local/file.ext', 'rb'))

# Save file on the working directory
localClient.save_file(file)

# Save file to the specific directory
localClient.save_file(file, folder='some-directory-name')
