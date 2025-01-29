import sys


def clearLines(x):
    temp = str.split(x, "\n")
    ans = ""
    for i in temp:
        ans = ans + i
    temp = ans.split("-")
    ans = ""
    for i in temp:
        ans = ans + i
    return ans


def translateHtml(x):
    import os
    temp = clearLines(x)
    os.system("/home/wznmickey/.pyenv/versions/3.10.13/bin/python -m googletranslate zh-CN " + '"' + x + '"')


def translate(x):
    import os
    temp = clearLines(x)
    os.system("/home/wznmickey/.pyenv/versions/3.10.13/bin/python -m googletranslate -r text zh-CN " + '"' + x + '"')

def deeplx(x):
    import httpx, json
    from urllib.parse import unquote
    deeplx_api = "http://127.0.0.1:1188/translate"

    data = {
        "text": x,
        "source_lang": "EN",
        "target_lang": "ZH"
    }

    post_data = json.dumps(data)
    r = httpx.post(url = deeplx_api, data = post_data)
    # print(r)
    # print(r.content)
    print(unquote(json.loads(r.text)["data"]))
    for i in json.loads(r.text)["alternatives"] or []:
        print(unquote(i))

from ollama import chat
from ollama import ChatResponse
def llm(x):
    response: ChatResponse = chat(model='qwen2.5:0.5b', messages=[
    {
        'role': 'user',
        'content': 'Translate this to Chinese: '+x,
    },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)

if __name__ == '__main__':
    argv = sys.argv
    if (argv[1] == "clearLines"):
        print(clearLines(argv[2]))

    if (argv[1] == "googleTranslateHtml"):
        translateHtml(argv[2])
    if (argv[1] == "googleTranslate"):
        translate(argv[2])
    if (argv[1] == "deeplx"):
        deeplx(argv[2])
    if (argv[1] == "llm"):
        llm(argv[2])
