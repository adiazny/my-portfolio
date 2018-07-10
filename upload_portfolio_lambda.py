import boto3
import io
import zipfile
import mimetypes

def lambda_handler(event, context):
    
    s3 = boto3.resource('s3')
    
    portfolio_bucket = s3.Bucket('portfolio.alandiaz.com')
    
    build_bucket = s3.Bucket('portfoliobuild.alandiaz.com')
    
    portfolio_zip = io.BytesIO()
    
    build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)
    
    with zipfile.ZipFile(portfolio_zip) as myzip:
        for nm in myzip.namelist():
            obj = myzip.open(nm)
            portfolio_bucket.upload_fileobj(obj, nm,
                ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
            portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
    return 'Hello from Lambda'



#Iterate through the bucket to list the objects.
#for obj in portfolio_bucket.objects.all():
#    print(obj.key)

#Download object from S3 to local path
#portfolio_bucket.download_file('index.html','/tmp/index.html')
#build_bucket.download_file('portfoliobuild.zip', '/tmp/portfoliobuild.zip')

#with zipfile.ZipFile(portfolio_zip) as myzip:
#    for nm in myzip.namelist():
#        print(nm)