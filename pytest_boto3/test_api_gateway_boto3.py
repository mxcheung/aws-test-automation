import boto3

# Replace 'your_api_gateway_id', 'your_stage_name', 'your_http_method', and 'your_resource_path' with your API Gateway information
api_gateway_id = 'your_api_gateway_id'
stage_name = 'your_stage_name'
http_method = 'your_http_method'
resource_path = 'your_resource_path'

# Replace 'your_bearer_token' with your actual Bearer token
bearer_token = 'your_bearer_token'

# Create a client for API Gateway without specifying AWS credentials
client = boto3.client('apigateway', region_name='your_region')

# Create headers with Bearer token
headers = {
    'Authorization': f'Bearer {bearer_token}'
}

# Create a request to invoke the API with headers
request = {
    'restApiId': api_gateway_id,
    'resourceId': 'your_resource_id',  # Replace with your resource ID
    'httpMethod': http_method,
    'pathWithQueryString': resource_path,
    'stageVariables': {
        'your_stage_variable_key': 'your_stage_variable_value'  # Replace with your stage variable
    },
    'headers': headers
}

# Make the request to invoke the API
response = client.invoke_rest_api(**request)

# Print the response
print(response)
