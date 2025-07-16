# object(객체) : 데이터와 데이터를 활용하는 함수를 묶어놓은 것
# 자료와 개념들을 묶어놓기 위해서 사용을 하기도 함
# 속성, 행동 등을 모여준 것들
# const user = {
#   // 속성
#   name: 'John',
#   age: 20,
  
#   // 행동
#   greet: function() {
#     return f"Hello, {self.name}!"
#   }
# }

# 클래스란 객체에 대한 틀
# 클래스를 활용해서 만든 객체 -> 인스턴스(같은 말은 아님)

class User:
  # 클래스 변수
  count = 0
  
  # 인스턴스 초기화 메서드 -> 파이썬 제공 메서드
  def __init__(self, name, age):
    # 인스턴스 변수
    self.name = name
    self.age = age
    User.count += 1
  
  # 특수 메소드 -> 파이썬 제공 메서드
  # 인스턴스가 문자열로 표현될 때 사용되는 메서드
  def __str__(self):
    return f"이름: {self.name}, 나이: {self.age}"
  
  def say_hello(self):
    print(f"안녕하세요 저는 {self.name} 입니다.")
    
  def log_in(self, name, age):
    if name == self.name and age == self.age:
      print('로그인 성공')
    else:
      print('로그인 실패')
  
  # 클래스 메서드를 사용하게 되면 클래스 변수에 접근을 할 수 있다.
  @classmethod
  def get_count(cls):
    return cls.count

# 인스턴스 생성 -> 자동으로 init 메서드를 호출
user1 = User('John', 20)

# 인스턴스 생성
user2 = User('Jane', 21)

# 인스턴스 메서드의 특별한 규칙, 따로 코드를 사용하지않아도 - 인스턴스가 첫번째 아귀먼트로 자동으로 들어감
# user1.name = 'John'
# user1.age = 20

# user2.name = 'Jane'
# user2.age = 21
user1.say_hello() # 자동적으로 self 스스로 들어가는 파이썬의 규칙

user1.log_in('John', 20)

print(user1.get_count())

# print 함수는 str을 자동으로 호출해준다.
print(user1)