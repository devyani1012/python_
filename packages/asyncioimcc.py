import asyncio
async def main():
    print ("one")
    await asyncio.sleep(1)
    await fn2()
    await asyncio.sleep(1)
    print ("three")
    await asyncio.sleep(1)
    print("five")
async def fn2():
    print ("two")
    await asyncio.sleep(1)
    print ("four")
asyncio.run(main())        

