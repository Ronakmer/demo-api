class ORMManager():
    def __init__(self,model):
        self.model = model

    def addData(self,data):
        obj = self.model()
        for key, value in data.items():
            obj.__dict__[key] = value
        obj.save()

    def getData(self):
        data = []
        for obj in self.model.object.all():
            pass


        


        
        
    


        