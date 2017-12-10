from flask_jsonrpc.proxy import ServiceProxy
import json
class Client:

    def __init__(self, server_addr):
        try:
            if type(server_addr)==str :
                self.server=ServiceProxy("http://"+server_addr+"/")   
            else :
                raise Exception("invalid paramater")
        except Exception as e:
            Exception("server offline")

    def time(self):
        try:
            data = self.server.time()
            return data['time']
        except Exception as e:
            raise Exception("server offline")
        
    def ram(self):
        try:
            data = self.server.ram()
            return data['used'],data['total']
        except Exception as e:
            raise Exception("server offline")
        
    def hdd(self):
        try:
            data = self.server.hdd()
            return data['used'],data['total']
        except Exception as e:
            raise Exception("server offline")
        
        
    def add(self, a, b):
        if type(a)==int and type(b)==int :
            try:
                data = self.server.add(a,b)
                return data['result']
            except Exception as e:
                raise Exception("server offline")
    
        else :
            raise Exception("invalid paramater")

        
        
        
    def sub(self, a, b):
        if type(a)==int and type(b)==int :
            try:
                data = self.server.sub(a,b)
                return data['result']
            except Exception as e:
                raise Exception("server offline")
            
        else :
            raise Exception("invalid paramater")
      
        
    def json_to_xml(self, json_string):
        flag = 0
        try:
            flag=1
            json.loads(json_string)
            
        except Exception as e:
            flag=2
            raise Exception("invalid paramater")
        try:
            if flag==1:
                data =self.server.json_to_xml(json_string)
                return data['result']
            
        except :
            raise Exception("server offline")

       
