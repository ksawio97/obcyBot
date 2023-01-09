from ActionController import ActionController

x = 0
while ActionController.run:
    ActionController.writeMessage(f"test {x}")
    ActionController.locatingKeyObjects()
    x += 1