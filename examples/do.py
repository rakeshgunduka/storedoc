from werkzeug.datastructures import FileStorage 
from storedoc import Service

# DO Spaces Credentials
DO_ACCESS_KEY = 'your-access-key'
DO_SECRET = 'your-secret'
DO_REGION = 'your-region'
DO_AUDIO_BUCKET = 'your-bucket-name'

DO_HOST = 'digitaloceanspaces.com'
DO_BASE_URL = 'https://{}.{}'.format(DO_REGION, DO_HOST)

# Get the service
doClient = Service('do')

# Describe Service
doClient.describe()

# Connect to the service
doClient.connect(
	region_name=DO_REGION,
	endpoint_url=DO_BASE_URL,
	aws_access_key_id=DO_ACCESS_KEY,
	aws_secret_access_key=DO_SECRET
)

# Get the connection
doClient.get_conn() 

# The FileStorage class is a thin wrapper over incoming files.
# It is used by the request object to represent uploaded files
file = FileStorage(open('path/to/local/file.ext', 'rb'))

# Upload to bucket on main directory
doClient.upload_file(file, bucket=DO_AUDIO_BUCKET)

# Upload to bucket on a specific directory
doClient.upload_file(file, bucket=DO_AUDIO_BUCKET, folder='videos')
