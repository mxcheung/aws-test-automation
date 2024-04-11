def is_valid_client(client_name, client_reference):
    # Define whitelist dictionaries for client-name and client-reference
    client_name_whitelist = {'client1', 'client2', 'client3'}
    client_reference_whitelist = {'reference1', 'reference2', 'reference3'}

    # Check if the provided values are in the whitelist
    if client_name not in client_name_whitelist or client_reference not in client_reference_whitelist:
        return False
    return True

def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        query_params = event.get('queryStringParameters', {})
        logger.info(f'query_params: {query_params}')
        
        # Check if client-name and client-reference are present in the query parameters
        client_name = query_params.get('client-name')
        client_reference = query_params.get('client-reference')
        if not client_name or not client_reference:
            return response(400, {'error': 'client-name and client-reference are required'})

        # Check if the client-name and client-reference are valid
        if not is_valid_client(client_name, client_reference):
            return response(400, {'error': 'Invalid client-name or client-reference'})

        # Proceed with the original functionality if the client is valid
        instruction_status_items = get_instruction_status(client_name, client_reference)
        logger.info(f'instruction_status_items: {instruction_status_items}')
        return response(200, {'items': instruction_status_items})

def response(status_code, body):
    return {
        'statusCode': status_code,
        'body': json.dumps(body),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
