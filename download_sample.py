import urllib.request
import ssl

url = "https://github.com/nvkelso/natural-earth-vector/blob/master/110m_cultural/ne_110m_admin_0_countries.zip?raw=true"
context = ssl._create_unverified_context()

try:
    with urllib.request.urlopen(url, context=context) as response, open("sample.zip", "wb") as out_file:
        out_file.write(response.read())
    print("Download successful")
except Exception as e:
    print(f"Download failed: {e}")
