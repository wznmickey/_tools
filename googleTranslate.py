import asyncio
from googletrans import Translator
import sys
async def translate_text(text):
    async with Translator() as translator:
        result = await translator.translate(text, dest='en')
        print(result.text)
        result = await translator.translate(text, dest='zh-CN')
        print(result.text)


if __name__ == '__main__':
    argv = sys.argv
    asyncio.run(translate_text(argv[1]))
