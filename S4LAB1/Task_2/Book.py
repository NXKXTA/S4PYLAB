class Book():
    def __init__(self, title, author, pages, cover_path):
        self.title = title  # Название
        self.author = author  # Автор
        self.pages = pages  # Страницы
        self.cover_path = cover_path  # Путь к обложке
        super().__init__()

    def get_info(self):
        return f"Название: {self.title}\nАвтор: {self.author}\nСтраниц: {self.pages}"
