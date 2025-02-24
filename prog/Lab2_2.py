from datetime import datetime, timedelta

class Book:
    def __init__(self, author, title, year, publisher, price):
        self.author = author
        self.title = title
        self.year = year
        self.publisher = publisher
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}, {self.publisher}, {self.price} руб.)"


class Subscriber:
    MAX_BOOKS = 10  # Максимальное количество книг в списке

    def __init__(self, surname, library_number):
        self.surname = surname
        self.library_number = library_number
        self.books = []  # Список книг
        self.count = 0  # Текущий счетчик книг

    def size(self):
        """Возвращает максимальное количество книг."""
        return self.MAX_BOOKS

    def add_book(self, book, issue_date, return_date, returned=False):
        """Добавляет книгу в список, если не превышен лимит."""
        if self.count >= self.MAX_BOOKS:
            print("Достигнуто максимальное количество книг.")
            return
        self.books.append({
            'book': book,
            'issue_date': issue_date,
            'return_date': return_date,
            'returned': returned
        })
        self.count += 1

    def remove_book(self, index):
        """Удаляет книгу по индексу."""
        if 0 <= index < self.count:
            del self.books[index]
            self.count -= 1
        else:
            print("Некорректный индекс.")

    def find_due_books(self):
        """Находит книги, которые подлежат возврату."""
        due_books = []
        today = datetime.now().date()
        for entry in self.books:
            if not entry['returned'] and entry['return_date'] < today:
                due_books.append(entry)
        return due_books

    def find_by_author(self, author):
        """Находит книги по автору."""
        return [entry for entry in self.books if entry['book'].author == author]

    def find_by_publisher(self, publisher):
        """Находит книги по издательству."""
        return [entry for entry in self.books if entry['book'].publisher == publisher]

    def find_by_year(self, year):
        """Находит книги по году издания."""
        return [entry for entry in self.books if entry['book'].year == year]

    def total_due_cost(self):
        """Вычисляет стоимость всех подлежащих возврату книг."""
        total_cost = sum(entry['book'].price for entry in self.find_due_books())
        return total_cost

    def merge(self, other):
        """Сливает две учетные карточки."""
        for entry in other.books:
            if self.count < self.MAX_BOOKS:
                self.books.append(entry)
                self.count += 1

    def intersection(self, other):
        """Возвращает пересечение двух учетных карточек."""
        common_books = []
        for entry in self.books:
            if entry in other.books:
                common_books.append(entry)
        return common_books

    def difference(self, other):
        """Возвращает разность двух учетных карточек."""
        unique_books = [entry for entry in self.books if entry not in other.books]
        return unique_books

    def __getitem__(self, index):
        """Перегрузка индексирования для доступа к книгам."""
        if 0 <= index < self.count:
            return self.books[index]
        raise IndexError("Индекс вне диапазона.")

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"Абонент: {self.surname}, Номер: {self.library_number}, Книги: {self.count}"


class Debt:
    def __init__(self, subscriber):
        self.subscriber = subscriber
        self.due_books = subscriber.find_due_books()

    def __str__(self):
        return f"Долг абонента {self.subscriber.surname}: {len(self.due_books)} книг."


def input_book():
    """Функция для ввода данных о книге."""
    author = input("Введите автора книги: ")
    title = input("Введите название книги: ")
    year = int(input("Введите год издания: "))
    publisher = input("Введите издательство: ")
    price = float(input("Введите цену книги: "))
    return Book(author, title, year, publisher, price)


def main():
    surname = input("Введите фамилию абонента: ")
    library_number = input("Введите библиотечный номер абонента: ")
    subscriber = Subscriber(surname, library_number)

    while True:
        print("\nВыберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книги по автору")
        print("4. Найти книги по издательству")
        print("5. Найти книги по году издания")
        print("6. Показать книги, подлежащие возврату")
        print("7. Показать общую стоимость долгов")
        print("8. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            book = input_book()
            issue_date = datetime.now().date()
            return_date = issue_date + timedelta(days=30)  # Предположим, что срок займа 30 дней
            subscriber.add_book(book, issue_date, return_date)
            print("Книга добавлена.")

        elif choice == '2':
            index = int(input("Введите индекс книги для удаления (0 - {}): ".format(subscriber.count - 1)))
            subscriber.remove_book(index)
            print("Книга удалена.")

        elif choice == '3':
            author = input("Введите автора для поиска: ")
            found_books = subscriber.find_by_author(author)
            for entry in found_books:
                print(entry['book'])

        elif choice == '4':
            publisher = input("Введите издательство для поиска: ")
            found_books = subscriber.find_by_publisher(publisher)
            for entry in found_books:
                print(entry['book'])

        elif choice == '5':
            year = int(input("Введите год издания для поиска: "))
            found_books = subscriber.find_by_year(year)
            for entry in found_books:
                print(entry['book'])

        elif choice == '6':
            due_books = subscriber.find_due_books()
            if due_books:
                for entry in due_books:
                    print(f"Книга подлежит возврату: {entry['book']}")
            else:
                print("Нет книг, подлежащих возврату.")

        elif choice == '7':
            total_cost = subscriber.total_due_cost()
            print(f"Общая стоимость долгов: {total_cost} руб.")

        elif choice == '8':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == '__main__':
    main()