import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web


# 注意headers指定content-type为html,否则会出现无法显示的问题
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    #server利用asyncio创建TCP服务
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()