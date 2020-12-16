    USERS = set()
    def register(websocket):
        USERS.add(websocket)

    async def ph(websocket, path):
        while True:
            register(websocket) #not sure if you need to place it here
            need_update = await websocket.recv()
            #check unique token to verify that it's the database
            message = 'update'#here we receive message that the data
                              #has been added and need to message the
                              #browser to update
            print('socket executed')
            if USERS:       # asyncio.wait doesn't accept an empty list
                await asyncio.wait([user.send(message) for user in USERS])


    start_server = websockets.serve(ph, '0.0.0.0', 5678)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()