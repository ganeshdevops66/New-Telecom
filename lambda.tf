resource "aws_lambda_function" "telecom_lambda" {
  function_name = "telecomProcessor"
  role          = aws_iam_role.lambda_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"

  filename      = "../lambda.zip"

  environment {
    variables = {
      BUCKET = aws_s3_bucket.telecom_bucket.bucket
    }
  }
}
