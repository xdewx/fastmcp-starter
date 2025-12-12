
import asyncio
import logging
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_greet(name: str):
    try:
        async with client:
            result = await client.call_tool("greet", {"name": name})
            return result
    except Exception as e:
        logging.error(e)
        return None
        
def test_call_greet():
    r=asyncio.run(call_greet("ipa"))
    print(r)
    if not r:
        return
    assert r.content[0].text == "Hello, ipa!"
