# from channels import include
from channels.routing import ProtocolTypeRouter

# channel_routing = [
#     include("CHATBOT.sub_routing.websocket_routing", path=r"^/chat/stream"),

#     include("CHATBOT.sub_routing.custom_routing"),

# ]
# application = ProtocolTypeRouter({
#     # Empty for now (http->django views is added by default)
# })

application = ProtocolTypeRouter({
    # (your routes here)
    # channel_routing
})
