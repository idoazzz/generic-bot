import logging
from logging.config import dictConfig
from typing import Optional

from fastapi import FastAPI, Request, HTTPException

from app.conversations.consts import SAMPLE_BOT
from app.conversations.controller import apply_action
from app.conversations.graph import ConversationGraph
from app.settings.logs import log_config
from app.whatsapp.utils import send_text_message, dispatch_message

dictConfig(log_config)
logger = logging.getLogger('botserver')

app = FastAPI(debug=True)
graph: ConversationGraph = ConversationGraph(**SAMPLE_BOT)

WEBHOOK_VERIFY_TOKEN = 'blue_panda'


@app.get('/')
async def root():
    payload: dict = graph.get_node_payload(graph.current_node_name)
    dispatch_message(payload=payload)
    return {'message': payload}


@app.post('/webhooks/whatsapp/webhook')
async def notification(request: Request):
    request_raw: dict = await request.json()
    logger.debug(request_raw)
    entry = request_raw.get('entry', [])[0]
    logger.debug(entry)
    change = entry.get('changes', [])[0]
    logger.debug(change)
    value = change.get('value', {})
    logger.debug(value)
    message = value.get('messages', [])[0]
    logger.debug(message)
    text = message.get('text', {})
    logger.debug(text)
    action: str = text.get('body')
    payload: Optional[dict] = apply_action(graph, action)
    if not payload or not isinstance(payload, dict):
        illegal_choice_message: str = f'Illegal action: {action}'
        send_text_message(text=illegal_choice_message)
        logger.warning(illegal_choice_message)
        return

    else:
        dispatch_message(payload=payload)
    # send_text_message('response!')
    logger.info(request_raw)
    return {'message': request_raw}


@app.get('/webhooks/whatsapp/webhook')
async def webhook_authenticate(request: Request):
    """Authenticate our webhook endpoint using the secret key.

    https://developers.facebook.com/docs/graph-api/webhooks/getting-started#verification-requests
    """
    mode: str = request.query_params.get('hub.mode')
    challenge: int = int(request.query_params.get('hub.challenge'))
    verify_token: str = request.query_params.get('hub.verify_token')

    if mode == 'subscribe' and challenge and verify_token == WEBHOOK_VERIFY_TOKEN:
        logger.debug(f'Authorized verification: {challenge}')
        return challenge

    raise HTTPException(status_code=403, detail='Wrong credentials')
