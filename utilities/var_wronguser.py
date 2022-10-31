class Verify:


    def __init__(self, driver):
        self.driver = driver

    def ver_wrong_user(self,data):
        print(data)
        if data == "Invalid credentials":
            print("pass")
        else:
            print("wrong")