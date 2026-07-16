def ask_duplicate():
    while True:
        ans = input("重複を許可しますか？ (y/n): ").strip().lower()

        if ans == "y":
            return True
        elif ans == "n":
            return False

        print("y または n を入力してください。")