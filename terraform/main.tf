
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}
 
# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
  # VERSION IS NOT NEEDED HERE
}


resource "aws_s3_bucket" "Terraform_Bucket" {
    bucket = "tf-bucket-rashi-testing-01"
    
}

resource "aws_s3_bucket" "Terraform_Bucket2" {
    bucket = "tf-bucket-rashi-testing-02"
    
}

resource "aws_s3_bucket_versioning" "bucket-versioning" {
    bucket = "tf-bucket-rashi-testing-01"
    versioning_configuration {
        status = "Enabled"
    }
}

resource "aws_s3_bucket_versioning" "bucket-versioning2" {
    bucket = "tf-bucket-rashi-testing-02"
    versioning_configuration {
        status = "Enabled"
    }
}




output "s3-bucket-info" {
    value = aws_s3_bucket_versioning.bucket-versioning
}

output "s3-bucket-info" {
    value = aws_s3_bucket_versioning.bucket-versioning2
}

