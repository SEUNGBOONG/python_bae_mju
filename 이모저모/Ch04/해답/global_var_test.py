var = 10

def func():
    # print(var)
    global var
    var2 = var
    var = 20
    print(var2)

func()

print("another test")

apple = 10
banana = apple
print(f"banana = {banana}, apple = {apple}")
apple = 20
print(f"banana = {banana}, apple = {apple}")

apple = [1,2,3]
banana = apple
print(f"banana = {banana}, apple = {apple}")
apple = [4,5,6]
print(f"banana = {banana}, apple = {apple}")

apple = [1,2,3]
banana = apple
print(f"banana = {banana}, apple = {apple}")
apple[2] = 4
print(f"banana = {banana}, apple = {apple}")