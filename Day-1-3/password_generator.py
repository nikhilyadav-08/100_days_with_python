
class PasswordGenerator:
    def __init__(self, seed):
        self.seed = seed

    def generate_password(self, num_of_iter):
        if num_of_iter == 1:
            # print(self.seed)
            return str(self.seed)
        else:
            self.seed *= self.seed
            self.seed = self.output_middle(self.seed)
            self.generate_password(num_of_iter-1)

    def return_new_pwd(self):
        number = self.print_key()
        pwd_char = ""
        while number > 1:
            temp = number % 100
            if 30 < temp < 126:
                pwd_char += chr(temp)
                number = number //100
            else:
                number = number //100
                pwd_char += str(temp)
        return pwd_char

    def output_middle(self, var):
        len_of_var = len(str(var))
        return var * len_of_var

    def print_key(self):
        return self.seed

if __name__ == "__main__":
    pwd = PasswordGenerator(int(input("Enter your birth date: ")))
    pwd.generate_password(12)
    print(pwd.return_new_pwd())
