from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/")
async def homepage(request):

    return web.Response(
        text="<h1>Bot hanya aktif di <a href='https://t.me/Drivecok'>@Telegram</a><br>By <a href='https://instagram.com/yourtulloh'>Yourtulloh</a></h1>",
        content_type="text/html",
    )

async def e404_middleware(app, handler):
    async def middleware_handler(request):

        try:
            response = await handler(request)
            if response.status == 404:
                return web.Response(
                    text="<h1>404: Torrent tidak ditemukan!</h2><br><h3>Drivecok</h3>",
                    content_type="text/html",
                )
            return response
        except web.HTTPException as ex:
            if ex.status == 404:
                return web.Response(
                    text="<h1>404: Torrent tidak ditemukan!</h2><br><h3>Drivecok</h3>",
                    content_type="text/html",
                )
            raise

    return middleware_handler

async def start_server():

    app = web.Application(middlewares=[e404_middleware])
    app.add_routes(routes)
    return app


async def start_server_async(port=80):

    app = web.Application(middlewares=[e404_middleware])
    app.add_routes(routes)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", port).start()
