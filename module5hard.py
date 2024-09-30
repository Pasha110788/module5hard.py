from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Название-{self.title},длительность-{self.duration}'


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                break

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(user)
        self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for el in args:
            if el not in self.videos:
                self.videos.append(el)

    def get_videos(self, search):
        s_video = []
        for el in self.videos:
            if search.lower() in el.title.lower():
                s_video.append(el.title)
                return s_video

    def watch_video(self, film):
        if self.current_user:
            for video in self.videos:
                if self.current_user.age < 18 and self.current_user:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    break
                if film == video.title:
                    for i in range(video.time_now + 1, video.duration + 1):
                        print(i, end='')
                        sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print(' Конец видео')
                    break
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def __str__(self):
        return self.current_user.nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
