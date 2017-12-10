import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:3000')
print(s.time(1))  # Returns 5
print(s.mul(5,2))  # Returns 5*2 = 10
