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
    count += 1
    print(f"\r{count}")


words = "a、b、c、d、e、f、g、h、i、j、k、l、m、n、o、p、q、r、s、t、u、v、w、x、y、z".split("、")
w2 = ["".join(i) for i in permutations(words, 2)]
w3 = ["".join(i) for i in permutations(words, 3)]
words = w2 + w3

with ThreadPoolExecutor(32) as thread:
    for word in words:
        thread.submit(sea(word))
