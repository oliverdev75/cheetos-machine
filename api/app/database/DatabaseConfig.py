

class DatabaseConfig:

    def __init__(
        self,
        *,
        type,
        host,
        port,
        user,
        password,
        name
    ):
        self.type = type
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.name = name
    
    def get_string(self):
        return f"{self.type}://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"