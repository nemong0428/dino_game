from js import document, window, Image
from pyodide.ffi import create_proxy
import random


canvas = document.getElementById("game")
ctx = canvas.getContext("2d")

def clearCanvas(): ctx.clearRect(0, 0, canvas.width, canvas.height)



def drawRect(sprite):
    #ctx.fillStyle = sprite["color"]
    #ctx.fillRect(sprite["x"], sprite["y"], sprite["width"], sprite["height"])
    
    img = Image.new()
    img.src = sprite["image"]
    ctx.drawImage(img, sprite["x"], sprite["y"])
    
def checkCollision(dino, cactus):
    if (dino["x"] < cactus["x"] + cactus["width"] and
        dino["x"] + dino["width"] > cactus["x"] and
        dino["y"] < cactus["y"] + cactus["height"] and
        dino["y"] + dino["height"] > cactus["y"]):
        return True
    return False


dino = {
    "width": 50,
    "height": 50,
    "x": 0,
    "y": 250,
    "color": "red",
    "image": "public/dino.png",
    "jump": False,
}
cactus = {
    "width": 50,
    "height": 50,
    "x": 750,
    "y": 250,
    "color": "green",
    "image": "public/cactus.png"
}

cactuses = [cactus.copy()]
timer = 0


def update(*args):
    global timer
    
    clearCanvas()
    
    timer += 1
    if timer % 120 == 0 and random.randrange(0,4) == 0:
        cactuses.append(cactus.copy())
    
    for cac in cactuses:
        cac["x"] -= 2;
        if (cac["x"] + cac["width"] == 0): 
            cactuses.remove(cac)
            continue
        drawRect(cac)
        
        if checkCollision(dino, cac):
            clearCanvas()
            window.alert(f'Game Over!\n점수 : {timer}')
            return
        
    if dino["jump"] == True:
        if dino["y"] == 100: dino["jump"] = False
        else: dino["y"] -= 2
    else: 
        if dino['y'] != canvas.height - dino['height']: dino["y"] += 2
    drawRect(dino)
    
    window.requestAnimationFrame(update_proxy)

update_proxy = create_proxy(update)
window.requestAnimationFrame(update_proxy)


def onkeydown(KeyboardEvent):
    keyCode = KeyboardEvent.code
    if keyCode == 'Space' and dino["jump"] == False and dino["y"] == canvas.height - dino['height']:
        dino["jump"] = True
window.onkeydown = onkeydown
