import zmq

class Publisher:
    '''Data publisher to be used within Blender scripts.'''

    def __init__(self, bind_address, btid):
        self.ctx = zmq.Context()
        self.sock = self.ctx.socket(zmq.PUB)
        self.sock.setsockopt(zmq.LINGER, 0)
        self.sock.bind(bind_address)
        self.btid = btid
        
    def publish(self, kwargs):
        data = dict(btid=self.btid)
        data.update(kwargs)
        self.sock.send_pyobj(data)