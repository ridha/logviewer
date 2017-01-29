# -*- coding: utf-8 -*-

import argparse
import os
import asyncio
import json

import aiohttp_jinja2

from aiohttp.web import run_app, Application, MsgType, Response, WebSocketResponse

from jinja2 import PackageLoader

from logviewer.tail import AsyncTail


async def index(request):
    return aiohttp_jinja2.render_template('index.html', request, {"host": request.host})

async def websocket_handler(request):
    resp = WebSocketResponse()
    await resp.prepare(request)

    async with AsyncTail(filepath=request.app['filepath']) as atail:
        async for line in atail:
            resp.send_str(json.dumps({
                'action': 'sent',
                'text': line
            }))

    resp.send_str(json.dumps({
        'action': 'close',
    }))
    await resp.close()
    print('Web socket connection closed')
    return resp


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/ws', websocket_handler)


async def init(loop, *, filepath):
    app = Application(loop=loop)
    app['filepath'] = filepath
    aiohttp_jinja2.setup(
        app,
        loader=PackageLoader('logviewer', 'templates')
    )
    setup_routes(app)
    return app


def main():
    parser = argparse.ArgumentParser(description="Logviewer is a realtime log monitoring in browser")
    parser.add_argument("-p", "--port", default=8080, type=int, help="Specify the webserver port (default to 8080)")
    parser.add_argument("-f", "--file", default=None, help="File path (default to stdin)")
    args = parser.parse_args()

    if args.file is not None and not os.path.isfile(args.file):
        print(f"Error: File {args.file} not found")
        return

    loop = asyncio.get_event_loop()
    try:
        app = loop.run_until_complete(init(loop, filepath=args.file))
        run_app(app, host='0.0.0.0', port=args.port)
    finally:
        if not loop.is_closed():
            loop.stop()
            loop.run_forever()
            loop.close()


if __name__ == '__main__':
    main()
