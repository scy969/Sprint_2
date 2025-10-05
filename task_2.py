class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: {self.movies}"


class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: {self.movies}"


# Создаем объекты и вызываем методы
comedy_obj = Comedy()
result_comedy = comedy_obj.add_movie('Большой куш')
print(result_comedy)

drama_obj = Drama()
result_drama = drama_obj.add_movie('Оружейный барон')
print(result_drama)