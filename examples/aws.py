from werkzeug.datastructures import FileStorage
from storedoc import Service


S3_ACCESS_KEY = 'your-access-key'
S3_SECRET = 'your-secret'
S3_REGION = 'your-region'
S3_BUCKET_MAIN = 'your-bucket-name'

S3_REGION_HOST = '//s3.{}.amazonaws.com'.format(S3_REGION)
S3_BASE_URL = 'https://s3.amazonaws.com'

# Get the service
awsClient = Service('aws')

# Describe Service
awsClient.describe()

# Connect to the service
awsClient.connect(
    region_name='//s3.your-region.amazonaws.com',
    endpoint_url='https://s3.amazonaws.com',
    aws_access_key_id='your-access-key',
    aws_secret_access_key='your-secret'
)

# Get the connection
awsClient.get_conn() 

# The FileStorage class is a thin wrapper over incoming files.
# It is used by the request object to represent uploaded files
file = FileStorage(open('path/to/local/file.ext', 'rb'))

# Upload to bucket on main directory
awsClient.upload_file(file, bucket=S3_BUCKET_MAIN)

# Upload to bucket on a specific directory
awsClient.upload_file(file, bucket=S3_BUCKET_MAIN, folder='some-directory-name')
