class Movie:
    def __init__ (self, name, yearLaunch, includedPlan, note):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note

movie = Movie("Top Gun Maverick", 2022, False, 5.0)
print("####Dados Filme####")
print(f"Nome do Filme: {movie.name} - Ano de Lançamento: {movie.yearLaunch}")

