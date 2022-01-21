import aiohttp
import asyncio
import ujson

class Engine(object):
    def __init__(self, vk_group_token, vk_group_id):
        self.vk_group_token = vk_group_token
        self.vk_group_id = vk_group_id
        self.url = "https://api.vk.com/method/"
        self.api_version = '5.101'

    async def method(self, method, args):
        async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
            args["access_token"] = self.vk_group_token
            args["v"] = self.api_version
            async with session.post(self.url+method, json=args) as response:
                return await response.json()

token = "96680abd57ab6db207e5a8f7710f0fbe4fe70371fa1b6f331a605f85d9acbabc4858f973e4f34c6589544"
id_ = "club205346390"
api = Engine(token, id_)

async def main():
    args = {
        "offset": 0,
        "count": 20,
        "filter": 'all',
    }
    var = await api.method('messages.getConversations', args)
    print(var)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
