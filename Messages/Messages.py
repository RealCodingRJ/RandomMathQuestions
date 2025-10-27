async def createFileSync(name: str, message: str):
    with open(name, "w") as f:
        f.write(message)
