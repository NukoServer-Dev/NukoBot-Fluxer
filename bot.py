import asyncio
import os

import aiosqlite
import dotenv

dotenv.load_dotenv()

import fluxer

class NukoBot(fluxer.Bot):
    def __init__(self):
        super().__init__(command_prefix=["!.", "n!", "n?"], intents=fluxer.Intents.all())

        self.DB: aiosqlite.Connection = None
        self.CURSUR: aiosqlite.Cursor = None

    async def load_extensions(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")

    async def setup_hook(self):
        self.DB = await aiosqlite.connect("data.db")
        self.CURSUR = await self.DB.cursor()

        await self.load_extensions()

bot = NukoBot()

if __name__ == "__main__":
    bot.run(os.environ.get('TOKEN'))