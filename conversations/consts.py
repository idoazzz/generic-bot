from typing import List

EXAMPLE_COMPONENT: List[dict] = [
    {
        'type': 'body', 'parameters': [{'type': 'text', 'text': 'ido'}]
    }
]


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
                'body': 'a state! Enter: 1, 2, 3'
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
                'name': 'custom',
                'language': {"code": "en_US"},
                'components': [
                    {'type': 'body', 'parameters': [{'type': 'text', 'text': 'ido'}]}
                ]
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
