class Database:
    def __init__(self):

        self.data={
            "user:1":"Anuska",
            "user:2":"Arun",
            "user:3":"Ritesh"
        }

    def get(self,key):
        return self.data.get(key, None)
    
    def set(self,key,value):
        self.data[key]=value

    def delete(self,key):
        if key in self.data:
            del self.data[key] 