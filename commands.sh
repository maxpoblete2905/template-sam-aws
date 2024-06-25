# crear un bucket S3
aws s3 mb s3://my-bucket-sam-maxpo

# Package Cloudformation
aws cloudformation package --template-file template.yaml --s3-bucket my-bucket-sam-maxpo --output-template-file gen/template-generate.yaml

#Deploy
aws cloudformation deploy --template-file gen/template-generate.yaml --stack-name sam-app --capabilities CAPABILITY_IAM

