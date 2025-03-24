import cherrypy
import os

# Update the CherryPy configuration
cherrypy.config.update({
    'server.socket_host': '127.0.0.1',
    'server.socket_port': 8082  
})


class MyApp:
    
   
    @cherrypy.expose
    def index(self):
        return "This is a plain text response!"
    
    
    @cherrypy.expose
    def res_html(self):
        return open('res.html').read()  
    
    
    @cherrypy.expose
    def html(self):
        return """
        <html>
        <head>
            <title>CherryPy HTML Page.</title>
        </head>
        <body>
            <h1>Hello World! Welcome to CherryPy!</h1>
            <p>This is an HTML page served by CherryPy.</p>
        </body>
        </html>
        """


if __name__ == '__main__':
    cherrypy.quickstart(MyApp())
