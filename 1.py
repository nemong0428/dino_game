from js import document, window
from pyodide.ffi import create_proxy

canvas = document.getElementById("game")
ctx = canvas.getContext("2d")

x = 0
y = 100

def update(*args):
    global x, y
    
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    
    x += 1
    if x > canvas.width: x = -50
    
    ctx.fillStyle = "black"
    ctx.fillRect(x, y, 50, 50)
    
    window.requestAnimationFrame(update_proxy)

update_proxy = create_proxy(update)
window.requestAnimationFrame(update_proxy)