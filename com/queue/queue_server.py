# _*_ coding:utf-8 _*_
'''
Created on 2013-3-29

@author: huanghu
'''
import SimpleHTTPServer
import BaseHTTPServer
import SocketServer
from com.customer.customer import Customer

class WebRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        customer = Customer();
        value1 = str(customer.take());
        value2 = str(customer.take());
        value3 = str(customer.take());
        value4 = str(customer.take());
        value5 = str(customer.take());
        value6 = str(customer.take());
        value7 = str(customer.take());
        value8 = str(customer.take());
        value9 = str(customer.take());
        value10 = str(customer.take());
        value11 = str(customer.take());
        value12 = str(customer.take());
        value13 = str(customer.take());
        value14 = str(customer.take());
        value15 = str(customer.take());
        value16 = str(customer.take());
  
        msg = "{\"d2\":[[%s ,%s] ,[%s ,%s] ,[%s ,%s] ,[%s ,%s]] ,\"d3\":[[%s ,%s] ,[%s ,%s] ,null ,[%s ,%s] ,[%s ,%s]]}" ;
        msg = msg % (value1 ,value2 ,value3 ,value4 ,value5 ,value6 ,value7 ,value8 ,value9 ,value10 ,value11 ,value12 ,value13 ,value14 ,value15 ,value16);

        #响应状态 
        code = 200;
        self.send_response(code);
        
        #响应头
        self.send_header('Allow', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'X-Request, X-Requested-With')
        self.send_header("Content-Type", "application/json;charset=UTF-8");
        self.send_header("Content-Length", len(msg));
        self.end_headers();
        
        #响应实体
        self.wfile.write(msg);   

class QueueServer(object):
    def examSimpleHTTP(self):
        PORT = 8000
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("", PORT), Handler)
        print "serving at port", PORT
        httpd.serve_forever()
        
    def examBaseHTTP(self ,server_class=BaseHTTPServer.HTTPServer,
            handler_class=WebRequestHandler):
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()
    