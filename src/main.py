from braw import signed_get


def main():
    account = signed_get("/api/v3/account")
    print("CONNECTED")
    print(account)


if __name__ == "__main__":
    main()
