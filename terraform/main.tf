provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "mlops_data" {
  bucket = "mlops-project-data"
}

resource "aws_lambda_function" "ml_model" {
  function_name = "MLPredictor"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.8"
  handler       = "lambda_handler.lambda_handler"

  source_code_hash = filebase64sha256("lambda_function.zip")

  environment {
    variables = {
      BUCKET_NAME = aws_s3_bucket.mlops_data.bucket
    }
  }
}
