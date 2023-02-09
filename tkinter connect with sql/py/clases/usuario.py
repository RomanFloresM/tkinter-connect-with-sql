import hashlib

class usuario:
    id = None
    Nickname = None
    Correo = None
    RegsitroFecha = None
    pasw = None
    estatus = None

    def __ini__(self):
        self.id = None
        self.Nickname = None
        self.Correo = None
        self.RegsitroFecha = None
        self.pasw = None
        self.estatus = None

    def set_id(self, a):
        self.id = a

    def set_Nickname(self, a):
        self.Nickname = a

    def set_Correo(self, a):
        self.Correo = a

    def set_RegsitroFecha(self, a):
        self.RegsitroFecha = a

    def set_pasw(self, a):
        b = hashlib.sha256(a.encode('utf-8')).hexdigest() 
        self.pasw = b

    def get_id(self):
        return self.id

    def get_Nickname(self):
        return self.Nickname

    def get_Correo(self):
        return self.Correo

    def get_RegsitroFecha(self):
        return self.RegsitroFecha

    def get_pasw(self):
        return self.pasw

    def get_estatus(self):
        return self.estatus
    
