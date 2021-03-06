# Storedoc

A python module to upload files on cloud. Supported services - [AWS S3](https://aws.amazon.com/s3/), [DigitalOcean Spaces](https://www.digitalocean.com/docs/spaces/), LocalStorage.

# Installation
To install, simply use `pip` or `easy_install`:

```bash
$ pip install --upgrade storedoc
```
or
```bash
$ easy_install --upgrade storedoc
```
------------

# Get Started

#### Upload to AWS S3 Buckets

### Initialize the service

    from storedoc import Service
    client = Service('aws')


### Get information of the service

    client.describe()


### Instantiate AWS S3 Client

    client.connect(
        region_name='//s3.your-region.amazonaws.com',
        endpoint_url='https://s3.amazonaws.com',
        aws_access_key_id='your-access-key',
        aws_secret_access_key='your-secret'
    )


### Upload the file to S3 bucket (Note: File type supported <werkzeug.datastructures.FileStorage>)

    # Default ACL (Access Control List) is set to 'private'.
    # Default MIME Type results to 'binary/octet-stream' if no MIME type is provided.
    client.upload_file(file, bucket='your-bucket-name')

    # To add your custom ACL ('private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exe').
    client.upload_file(file, bucket='your-bucket-name', acl='public-read')

    # To add explicit MIME Type. Example for JPEG image upload, you can user
    client.upload_file(file, bucket='your-bucket-name', mime='image/jpeg')

    # You can let storedoc guess the MIME Type for you (Default is set to False)
    client.upload_file(file, bucket='your-bucket-name', guess_mime=True)

#### Upload to DigitalOcean Spaces Buckets

### Initialize the service

    from storedoc import Service
    client = Service('do')


### Get information of the service

    client.describe()


### Instantiate DO Spaces Client

    client.connect(
        region_name='//s3.your-region.amazonaws.com',
        endpoint_url='https://your-region.digitaloceanspaces.com',
        aws_access_key_id='your-access-key',
        aws_secret_access_key='your-secret'
    )


### Upload the file to S3 bucket (Note: File type supported <werkzeug.datastructures.FileStorage>)

    # Default ACL (Access Control List) is set to 'private'.
    # Default MIME Type results to 'binary/octet-stream' if no MIME type is provided.
    client.upload_file(file, bucket='your-bucket-name')

    # To add your custom ACL ('private'|'public-read'|'public-read-write'|'authenticated-read'|'aws-exe').
    client.upload_file(file, bucket='your-bucket-name', acl='public-read')

    # To add explicit MIME Type. Example for JPEG image upload, you can user
    client.upload_file(file, bucket='your-bucket-name', mime='image/jpeg')

    # You can let storedoc guess the MIME Type for you (Default is set to False)
    client.upload_file(file, bucket='your-bucket-name', guess_mime=True)


#### Save File to Local Storage

### Initialize the service

    from storedoc import Service
    client = LocalStorage()


### Save file to working directory (Note: File type supported <werkzeug.datastructures.FileStorage>)

    client.save_file(file)


### Save file to specific directory (Note: File type supported <werkzeug.datastructures.FileStorage>)

    client.save_file(file, folder='some-directory-name')


------

## Features
* Upload Any file to AWS s3, DigitalOcean Spaces
* Set ACL Support
* Content Type Support


## Third Party Libraries and Dependencies
The following libraries will be installed when you install the client library:
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (Amazon Web Services SDK for Python)


## To-Dos
- Test cases.


## Contribute
1. Look for an open [issue](https://github.com/rakeshgunduka/storedoc/issues) or create new issue to get a dialog going about the new feature or bug that you've discovered.
2. Fork the [repository](https://github.com/rakeshgunduka/storedoc) on Github to start making your changes to the master branch (or branch off of it).
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Make a pull request.

