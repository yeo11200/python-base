class User:
    # 인스턴스 변수 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트

    # 팔로우
    def follow(self, another_user):
        # 여기에 코드를 작성하세요
        if another_user not in self.following_list:
          self.following_list.append(another_user)
          another_user.followers_list.append(self)
    # 내가 몇 명을 팔로우하는지 리턴
    def num_following(self):
        # 여기에 코드를 작성하세요
        return len(self.following_list)
    # 나를 몇 명이 팔로우하는지 리턴
    def num_followers(self):
        # 여기에 코드를 작성하세요
        return len(self.followers_list)

# 유저들 생성
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 유저마다 서로 관심 있는 유저를 팔로우
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

# 유저 이름, 자신의 팔로워 수, 자신이 팔로우하는 사람 수를 출력합니다
print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())

class MenuItem:
    # 음식 메뉴를 나타내는 클래스
    def __init__(self, name, price):
        # 여기에 코드를 작성하세요
        self.name = name
        self.price = price
    def __str__(self):
        # 여기에 코드를 작성하세요
        return f"{self.name} 가격: {self.price}"

# 메뉴 인스턴스 생성
burger = MenuItem("햄버거", 4000)
coke = MenuItem("콜라", 1500)
fries = MenuItem("후렌치 후라이", 1500)

# 메뉴 인스턴스 출력
print(burger)
print(coke)
print(fries)

class GameCharacter:
    # 게임 캐릭터 클래스
    def __init__(self, name, hp, power):
        # 게임 캐릭터는 속성으로 이름, hp, 공격력을 갖는다
        self.name = name
        self.hp = hp
        self.power = power
    def is_alive(self):
        # 게임 캐릭터가 살아있는지(체력이 0이 넘는지) 확인하는 메소드
        return self.hp > 0
    def get_attacked(self, damage):
        """
        게임 캐릭터가 살아있으면 공격한 캐릭터의 공격력만큼 체력을 깎는 메소드
        조건:    
            1. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다
            2. 남은 체력보다 공격력이 더 크면 체력은 0이 된다
        """
        # 게임 캐릭터가 살아있으면
        # 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다
        if self.is_alive():
            self.hp = self.hp - damage if self.hp >= damage else 0
        else:
            print("{}님은 이미 죽었습니다.".format(self.name))
    def attack(self, other_character):
        # 게임 캐릭터가 살아있으면 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다
         if self.is_alive():
            other_character.get_attacked(self.power)
    def __str__(self):
        # 게임 캐릭터의 의미있는 정보를 포함한 문자열을 리턴한다
        return f"{self.name}님의 hp는 {self.hp}만큼 남았습니다."

# 게임 캐릭터 인스턴스 생성                        
character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

# 게임 캐릭터 인스턴스들 서로 공격
character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)

# 게임 캐릭터 인스턴스 출력
print(character_1)
print(character_2)

class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 작성 날짜와 내용을 갖는다
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소드
        return "작성 날짜: {}\n내용: {}".format(self.date, self.content)
    
    
class BlogUser:
    # 블로그 유저 클래스
    def __init__(self, name):
        """
        블로그 유저는 속성으로 이름, 게시글들을 갖는다
        posts는 빈 배열로 초기화한다
        """
        self.name = name
        self.post = []

    def add_post(self, date, content):
        # 새로운 게시글 추가
        post = Post(date, content)
        self.post.append(post)
    def show_all_posts(self):
        # 블로그 유저의 모든 게시글 출력
        for post in self.post:
            print(post)

    def __str__(self):
        # 간단한 인사와 이름을 문자열로 리턴
        # return "안녕하세요 {}입니다.\n".format(self.name)
        return f"안녕하세요 {self.name}입니다. \n"
    
    

# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호")

# 블로그 유저 인스턴스 출력(인사, 이름)
print(blog_user_1)

# 블로그 유저 게시글 2개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이었다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()