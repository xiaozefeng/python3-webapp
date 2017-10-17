# -*- coding: utf-8 -*-

__author__ = 'jack'

'''
async web application

'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/', index)
    server = await loop.create_server(app.make_handler(), '127.0.0.1', 8080)
    logging.info('server started at http://127.0.0.1:8080')
    return server

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
