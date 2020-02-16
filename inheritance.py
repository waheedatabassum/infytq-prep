class Apple:
    def security(self):
        print("security goes well in it")
    def pixels(self):
        print("well defined pixels")
        #representing the child or subclass
class Vivo(Apple):
     def volume(self):
         print("superb for enjoying the music")
     def model(self):
         print("too classy to look")
apple1 = Apple()
apple1.security()
apple1.pixels()
vivo1 = Vivo()
vivo1.security()
