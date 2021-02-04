import json
from channels import Channel
from channels.sessions import enforce_ordering

from .views import respond_to_websockets


@enforce_ordering
def ws_connect(message):
    # Initialise their session
    message.reply_channel.send({
        'accept': True
    })


@enforce_ordering
def ws_receive(message):
    payload = json.loads(message['text'])
    payload['reply_channel'] = message.content['reply_channel']
    Channel("chat.receive").send(payload)


@enforce_ordering
def ws_disconnect(message):
    pass


# Chat channel handling ###

def chat_start(message):
    pass


def chat_leave(message):
    pass


def chat_send(message):
    message_to_send_content = {
        'text': message['text'],
        'type': 'text',
        'source': 'CANDIDATE'
    }
    message.reply_channel.send({
        'text': json.dumps(message_to_send_content)
    })

    response = respond_to_websockets(
        message
    )

    response['source'] = 'BOT'
    message.reply_channel.send({
        'text': json.dumps(response)
    })
