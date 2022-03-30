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
    os.system("python -m googletranslate zh-CN " + '"' + x + '"')


def translate(x):
    import os
    temp = clearLines(x)
    os.system("python -m googletranslate -r text zh-CN " + '"' + x + '"')


if __name__ == '__main__':
    argv = sys.argv
    if (argv[1] == "clearLines"):
        print(clearLines(argv[2]))

    if (argv[1] == "googleTranslateHtml"):
        translateHtml(argv[2])
    if (argv[1] == "googleTranslate"):
        translate(argv[2])
