from bs4 import BeautifulSoup
import requests, sys, time
import concurrent.futures


def get_info(base_url):
    intel = requests.get(base_url).text
    soup = BeautifulSoup(intel, features="lxml")
    try:
        valz = [i.attrs['href'] for i in soup.findAll('a', class_="preview")]
        with concurrent.futures.ThreadPoolExecutor() as execx:
            results = execx.map(redirects, valz)
    except Exception as e:
        print(e)


images = []


def redirects(url_r):
    new = requests.get(url_r).text
    soup = BeautifulSoup(new, features="lxml")
    try:
        for i in soup.findAll('img', id='wallpaper'):
            images.append(i.attrs['src'])

    except Exception as e:
        print(e)


def download(img):
    img_bytes = requests.get(img).content
    image = img.split("/")[::-1][0]
    with open(image, 'wb') as img:
        img.write(img_bytes)


def returntheurl(page=1):
    return f"https://wallhaven.cc/latest?page={page}"

if __name__ == "__main__":
    start = time.perf_counter()
    if len(sys.argv) == 2:
        if sys.argv[1].isnumeric():
            print("Please wait ... ")
            url = returntheurl(sys.argv[1])
        else:
            raise ValueError("Please Enter an Alphanumeric Value")
    else:
        url = returntheurl()

    get_info(url)
    with concurrent.futures.ThreadPoolExecutor() as execx:
        results = execx.map(download,images)

    end = time.perf_counter()
    print(f"Time taken to download {len(images)} images:- {round(end-start ,2)} second(s)")