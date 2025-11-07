def update_checkout_count(books, counts, book_title, new_count):
    if book_title in books:
        index = books.index(book_title)
        counts[index] = new_count
        return True
    else:
        return False

def remove_unpopular_books(books, counts, min_checkouts):
    i = 0
    while i < len(books):
        if counts[i] < min_checkouts:
            del books[i]
            del counts[i]
        else:
            i += 1

def categorize_by_popularity(books, counts, popular_threshold):
    popular_books = []
    regular_books = []

    for i in range(len(books)):
        if counts[i] >= popular_threshold:
            popular_books.append(books[i])
        else:
            regular_books.append(books[i])

    return popular_books, regular_books

def analyze_library_stock(initial_books, initial_counts, book_to_update, unpopular_threshold, popular_threshold):
    books_copy = initial_books[:]
    counts_copy = initial_counts[:]
    title, new_count = book_to_update

    update_checkout_count(books_copy, counts_copy, title, new_count)
    remove_unpopular_books(books_copy, counts_copy, unpopular_threshold)
    popular_books, regular_books = categorize_by_popularity(books_copy, counts_copy, popular_threshold)
    
    return popular_books, regular_books



books = ["Moby Dick", "1984", "Dune", "War and Peace"]
counts = [15, 130, 95, 25]
update_info = ["Moby Dick", 20]
unpopular_min = 22
popular_min = 100
popular, regular = analyze_library_stock(books, counts, update_info, unpopular_min, popular_min)

print("Popular:", popular)
print("Regular:", regular)