class myclass(object):
    def show(self):
        print("i am method")

x=myclass()
x.show()




class mobile:
    def __init__(self):
        self.model= 'samgsung'
    def show_model(self):
        print("model:",self.model)
sam = mobile()
sam.show_model()
print(sam.model)
sam.model="i phone"
print(sam.model)
sam.show_model()





class mobile:
    def __init__(self):
        self.model= 'samgsung'
    def show_model(self):
        prise=20000
        print("model:",self.model,"prise:",prise)
sam = mobile()
sam.show_model()
