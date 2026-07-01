import urllib.request
import time

urls = [
    "https://www.swisscom.ch",
    "https://www.google.com",
    "https://www.github.com",
]

print("=" * 40)
print("URL Monitor")
print("=" * 40)

for url in urls:
    try:
        start = time.time()
        urllib.request.urlopen(url, timeout=5)
        duration = round((time.time() - start) * 1000)
        print(f"OK      {duration}ms   {url}")
    except Exception as e:
        print(f"FEHLER  -        {url}")

print("=" * 40)