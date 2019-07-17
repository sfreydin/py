from aiohttp import web
import json
import os

async def handle(request):
    tag = os.environ['TAG']
    response_obj = {'status': 'success', 'tag': tag}
    return web.Response(text=json.dumps(response_obj))


app = web.Application()
app.router.add_get('/', handle)

web.run_app(app)
