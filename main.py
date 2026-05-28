def read_or_write_token():
    f = open("token.txt", "r")
    token = f.read()
    f.close()

    if(token == ""):
        with open("token.txt", "w") as f:
            token = input("Token not found. Please paste it now: ")
            f.write(token)
            f.close()
            return token
    else:
        return token


read_or_write_token()