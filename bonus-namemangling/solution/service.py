import datetime
import solution

class Service(solution.IPRecord):
    def __init__(self,ip, host_name, svc_name, port):
        super().__init__(ip, host_name)
        self.name = svc_name
        self.port = port

    def info(self):
        data =  f"SERVICE: {self.name} was found on port {self.port} on {str(self)}"
        return data
        
