from PIL import Image, ImageDraw
fin = open('input.txt', 'r').readlines()
line = fin[0].split()
w, h = int(line[2]), int(line[5])  # params of pic
size = (w, h)
img = Image.new('RGBA', size, (0, 0, 0, 0))
draw = ImageDraw.Draw(img)
pattern = 'O'  # pattern of background
for y in range(h):
    line = str(fin[y + 1])
    for x in range(w):
        if line[x] != pattern:
            draw.point((x, y))
img.save('result.jpeg', 'JPEG')
