variable "region" {
  description = "The AWS region to deploy resources in"
  default     = "us-west-2"
}

variable "table_name" {
  description = "Name of the DynamoDB table"
  default     = "the_table"
}
