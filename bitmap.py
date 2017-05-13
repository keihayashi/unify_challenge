import urllib.request
from PIL import Image

width = 128
height = 128
pixels = width * height
nums = ""

while pixels > 0:
    with urllib.request.urlopen("https://www.random.org/integers/?num=10000&min=0&max=16777215&col=1&base=10&format=plain&rnd=new") as res:
       html = res.read().decode("utf-8")
       nums += html + ' '
    pixels -= 10000

nums = nums.split()
image = Image.new("RGB", (width, height))
pixels = image.load()
count = 0

for i in range(image.size[0]):
    for j in range(image.size[1]):
        rgb = int(nums[count])
        r = rgb >> 16
        g = rgb >> 8 & 0xFF
        b = rgb & 0xFF
        pixels[i,j] = (r, g, b)
        count += 1

image.save('bitmap.bmp')
