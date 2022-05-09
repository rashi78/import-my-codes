#output values you can check with running terraform console command 

output "s3-bucket-info" {
    value = aws_s3_bucket_versioning.bucket-versioning
}

output "s3-bucket-info" {
    value = aws_s3_bucket_versioning.bucket-versioning2
}
