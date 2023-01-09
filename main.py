from ActionController import ActionController

x = 0
while ActionController.run:
    ActionController.writeMessage(f"test {x}")
    x += 1
    ActionController.locatingKeyObjects()

