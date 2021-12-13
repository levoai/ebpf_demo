from aiohttp import web
import json

# from openapi_server.models.inline_response200 import InlineResponse200
# from openapi_server import util


async def hello_world_get(request: web.Request, body=None) -> web.Response:
    ohai = {
        "Hello": "World",
        "Description": "A simple GET handler to demonstrate levo-ebpf-demo's ability "
                       "to capture buffers from sendto() and recvfrom() system calls."
    }
    return web.Response(status=200, content_type="application/json", body=json.dumps(ohai, indent=2))
