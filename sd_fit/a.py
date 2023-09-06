import requests
from itertools import permutations
from concurrent.futures import ThreadPoolExecutor


count = 0


def sea(word):
    global count
    headers = {
        "authority": "crates.io",
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "referer": "https://crates.io/search?q=w",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }
    url = "https://crates.io/api/v1/crates"
    params = {"page": 1, "per_page": 3, "q": word}
    response = requests.get(url, headers=headers, params=params)
    names = [i["name"] for i in response.json()["crates"]]
    if not word in names:
        print(word)


def m2(ls):
    res = []
    for i in ls:
        for j in ls:
            res.append(i + j)
    return res


def m3(ls):
    res = []
    for i in ls:
        for j in ls:
            for k in ls:
                res.append(i + j + k)
    return res


words = "a、b、c、d、e、f、g、h、i、j、k、l、m、n、o、p、q、r、s、t、u、v、w、x、y、z".split("、")
w2 = ["".join(i) for i in m2(words)]
w3 = ["".join(i) for i in m3(words)]
words = w2 + w3


with ThreadPoolExecutor(32) as thread:
    for i, word in enumerate(words[442:646]):
        thread.submit(sea(word))
        # print(i, word)
