import asyncio
import requests 

async def req(name, number):
    for i in range(1,number+1):
        r = requests.get('https://webhook.site/9915eb94-ee00-4e62-b2b3-5665d7b7732d')
        await asyncio.sleep(1)
        print(name, r.headers['date'])

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    req("A",3),
    req("B",2),
    req("C",1)
))
loop.close()
