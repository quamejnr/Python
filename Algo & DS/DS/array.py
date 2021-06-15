
class Movie:
    def __init__(self, title, release_year, director):
        self.title = title
        self.release_year = release_year
        self.director = director

    def __str__(self):
        return f'"{self.title}" directed by {self.director} was released in {self.release_year}'


movie1 = Movie('Avengers', '1995', 'Joss Whedon')


array = [1, 2, 3, 4]

# print(True) if 1 in array else print(False)

print(array.index(4))