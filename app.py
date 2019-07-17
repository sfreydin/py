from aiohttp import web
import json
import os

async def handle(request):
    IMAGE_TAG = os.environ['IMAGE_TAG']
    response_obj = {'status': 'success', 'image_tag': IMAGE_TAG}
    return web.Response(text=json.dumps(response_obj))


app = web.Application()
app.router.add_get('/', handle)

web.run_app(app)
