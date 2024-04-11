    if http_method == 'GET':
        query_params = event.get('queryStringParameters')
        logger.info(f'query_params: {query_params}')
        client_name = query_params['client-name']
        client_reference = query_params['client-reference']
        instruction_status_items = get_instruction_status(client_name, client_reference)
        logger.info(f'instruction_status_items: {instruction_status_items}')
        return response(200, {
            'items': instruction_status_items
        })
