SAMPLE_BOT = {
    'customer': {
        # Identifiers of customer
    },
    'current_node': 'a',
    'root': 'a',
    'nodes': {
        'a': {
            'type': 'text',
            'text': {
                'body': 'X'
            },
            'metadata': {
                'choices': {  # The user response
                    '1': 'a',
                    '2': 'b',
                    '3': 'FINISHED',
                }
            }
        },
        'b': {
            # https://developers.facebook.com/docs/whatsapp/cloud-api/get-started-for-bsps
            'type': 'template',
            'template': {
                'name': 'helloworld'
            },
            'metadata': {
                'choices': {  # The user response
                    '4': 'a',
                    '5': 'b',
                }
            }
        },
        'c': {
            # data
        }
    },
}
