import boto3
import io
import zipfile
import mimetypes

def lambda_handler(event, context):
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:249461076984:deployPortfolioTopic')
    
    location = {
        "bucketName" : 'portfoliobuild.alandiaz.com',
        "objectKey" : 'portfoliobuild.zip'

    }

    try:
        job = event.get("CodePipeline.job")

        if job:
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "MyAppBuild":
                    location = artifact["location"]["s3Location"]

        print("Building portfolio from " + str(location))

        s3 = boto3.resource('s3')
        
        portfolio_bucket = s3.Bucket('portfolio.alandiaz.com')
        build_bucket = s3.Bucket(location["bucketName"])
        
        portfolio_zip = io.BytesIO()
        build_bucket.download_fileobj(location["objectKey"], portfolio_zip)
        
        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm,
                    ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
                portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
        print('Job Done')
        topic.publish(Subject='Porfolio Deployment Success', Message='You portfolio has been deployed successfully.')
        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job["id"])
    except:
        topic.publish(Subject='Porfolio Deployment Failed', Message='You portfolio deployment has failed.')
        raise
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