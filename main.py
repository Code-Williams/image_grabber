import requests, re
from bs4 import BeautifulSoup

image_name = input("Enter a name for searching in images: ")
if image_name == "": exit()
image_name = re.sub(r"\s+", "+", image_name)

image_page = requests.get(f"https://www.google.com/search?q={image_name}&sxsrf=AOaemvJfWVCU6pMPa99p--Xpxa01Q-3ZOQ:1643121860625&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjLpMz2kc31AhVKcBQKHeXhDr0Q_AUoAXoECAEQAw&cshid=1643121875891075&biw=1440&bih=796&dpr=2")

soup = BeautifulSoup(image_page.content, "html.parser")

find_all_images = soup.find_all("img", {"alt":""})

for images in find_all_images:
    print(images['src'])