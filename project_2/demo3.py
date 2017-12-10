from xmlrpc.server import SimpleXMLRPCServer
import time   

def time(*args):   
	t = int(time.time())
	return t

def add(x,y):
	return x+y
    
def subtract(x, y):   
    return x-y   
    
def multiply(x, y):   
    return x*y   
    
def divide(x, y):   
    return x/y  
 
server = SimpleXMLRPCServer(("localhost", 3000))   
server.register_function(time, 'time')   
server.register_function(subtract, 'sub')   
server.register_function(multiply, 'mul')  
server.register_function(add,'add') 
server.register_function(divide, 'divide')   
server.serve_forever() 