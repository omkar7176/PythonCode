class client_info:
    cli_id = 1
    cli_name = "Raju"
    cli_add = "Delhi"
    cli_need = "Java"

    def info(self):
        print(f"The {self.cli_name} have ID no {self.cli_id}, he stay in {self.cli_add} & skills {self.cli_need}")

a = client_info()
b = client_info()
c = client_info()

b.cli_id = 2
b.cli_name = "Jayesh"
b.cli_add = "Mumbai"
b.cli_need = "Python"

a.info()
b.info()
c.info()