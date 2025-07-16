# 클래스
class User:
  # 클래스 변수 - 모든 인스턴스에 공유하는 값
  count = 0
  
  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password
    User.count += 1
    
  def __str__(self):
    return f"사용자 {self.name} 이메일 {self.email}"
  
  # 데코레이터: 클래스 메서드화
  # 인스턴스일 때는 첫번째 인자: 본인 self
  # 클래스메서드 일 때는 첫번째 인자: class 변수
  @classmethod
  def print_numer_of_user(cls):
    print(f"총 유저 수는: {cls.count}")
    

user1 = User("신진섭", "yeo1120@aa", "12345")
user2 = User("신진섭2", "yeo1120@aa", "12345")

print(user1.count)
print(User.count)

User.print_numer_of_user()


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        # 여기에 코드를 작성하세요
        parameter_list = string_params.split(",") # split 메소드를 사용해서 쉼표(,)를 기준으로 문자열을 리스트로 분리한다
        return cls(parameter_list[0], parameter_list[1], parameter_list[2])
    @classmethod
    def from_list(cls, list_params):
        # 여기에 코드를 작성하세요
        return cls(list_params[0], list_params[1], list_params[2])
      
    # 정적인 메서드: 인스턴스나 클래스가 필요하지않을 때 사용하는데 클래스 안에 넣으면 좋을 때 사용한다.
    @staticmethod
    def valid_email(email):
      return "@" in email

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)

print(yoonsoo.valid_email(yoonsoo.email))

class SimpleCalculator:
    def __init__(self, x, y):
     self.x = x
     self.y = y
     
    # 계산기 클래스
    @staticmethod
    def add(first_number, second_number):
        # 파라미터로 받는 두 숫자의 합을 리턴한다
        return first_number + second_number
    
    @staticmethod
    def subtract(first_number, second_number):
        # 첫 번째 파라미터에서 두 번째 파라미터를 뺀 값을 리턴한다
        return first_number - second_number
    
    @staticmethod
    def multiply(first_number, second_number):
        # 파라미터로 받는 두 숫자의 곱을 리턴한다
        return first_number * second_number
    
    @staticmethod
    def divide(first_number, second_number):
        # 첫 번째 파라미터를 두 번째 파라미터로 나눈 값을 리턴한다
        return first_number / second_number
      
    # __add__, __sub__, __mul__, __truediv__, __bool__, __len__, __getitem__, __setitem__
    def __add__(self, other):
      return self.x + other.x + self.y + other.y
# 계산기 인스턴스 생성
calculator = SimpleCalculator(3, 5)
calculator2 = SimpleCalculator(444, 555)
    
# 계산기 연산 호출
print(calculator.add(4, 5))
print(calculator.subtract(4, 5))
print(calculator.multiply(4, 5))
print(calculator.divide(4, 5))

print(calculator + calculator2)

class Song:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.year})"


class PlayList:
    def __init__(self, songs):
        self.songs = songs

    def __str__(self):
        result = f"플레이리스트 안 노래들:\n\n"
        for song in self.songs:
            result += f"{song}\n"
        return result

    # 여기 코드를 쓰세요
    def __add__(self, other):
      return PlayList(self.songs + other.songs)

# 실행 코드
rolling_in_the_deep = Song("Rolling in the Deep", "Adele", 2011)
call_me_maybe = Song("Call Me Maybe", "Carly Rae Jepsen", 2012)
get_lucky = Song("Get Lucky", "Daft Punk", 2013)
uptown_funk = Song("Uptown Funk", "Mark Ronson", 2015)

palette = Song("Pallete(팔레트)", "아이유", 2017)
blood_sweat_and_tears = Song("피 땀 눈물", "방탄소년단", 2016)
tt = Song("TT", "트와이스", 2016)

us_pop_2010s = PlayList([rolling_in_the_deep, call_me_maybe, get_lucky, uptown_funk])
k_pop_2010s = PlayList([palette, blood_sweat_and_tears, tt])

pop_2010s = us_pop_2010s + k_pop_2010s
print(pop_2010s)
