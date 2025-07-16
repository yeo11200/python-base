class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다!")

    def login(self, email, password):
        # 로그인 메소드
        if self.email == email and self.password == password:
            print("로그인 성공, 환영합니다")
            self.say_hello()
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}"

    @classmethod
    def print_number_of_users(cls):
        print(f"총 유저 수는: {cls.count}입니다")
