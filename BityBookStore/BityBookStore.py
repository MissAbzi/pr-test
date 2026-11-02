# Guinevere Baptiste
# October 11th, 2026
# BITY BOOK GALLERY MANAGEMENT SYSTEM

# CONSTANTS
TITLE = "title"
AUTHOR = "author"
GENRE = "genre"
ISBN = "ISBN"
TAGS = "tags"


# FIND BOOK BY ISBN

def get_book(collection, isbn):
    for book in collection:
        if book[ISBN] == isbn:
            return (book[TITLE], book[AUTHOR])
    return ()


# ADD A BOOK

def add_book(collection, title, author, genre, isbn, tags):

    if get_book(collection, isbn):
        print("Error: A book with ISBN " + isbn +
              " already exists!")
        return collection.copy()

    new_book = {
        TITLE: title,
        AUTHOR: author,
        GENRE: genre,
        ISBN: isbn,
        TAGS: set(tags)
    }

    updated_collection = collection.copy()
    updated_collection.append(new_book)

    print("Book added successfully: " + title)
    return updated_collection


# SEARCH BOOKS BY TAGS

def books_with_tags(collection, tags):
    books = []

    for book in collection:
        if tags.issubset(book[TAGS]):
            books.append(book)

    return books

# SEARCH BY AUTHOR

def books_by_author(collection, author):
    results = []

    for book in collection:
        if author.lower() in book[AUTHOR].lower():
            results.append(book)

    return results


# SEARCH BY GENRE

def books_by_genre(collection, genre):
    results = []

    for book in collection:
        if genre.lower() in book[GENRE].lower():
            results.append(book)

    return results


# DISPLAY BOOKS

def display_books(books):

    if not books:
        print("\nNo books found.")
        return

    for number, book in enumerate(books, 1):
        print("\n" + str(number) + ". " + book[TITLE])
        print("   Author: " + book[AUTHOR])
        print("   Genre: " + book[GENRE])
        print("   ISBN: " + book[ISBN])
        print("   Tags: " + ", ".join(sorted(book[TAGS])))


# LIST UNIQUE AUTHORS

def list_authors(collection):
    authors = set()

    for book in collection:
        authors.add(book[AUTHOR])

    return sorted(authors)


# AUTOMATED TEST

def run_tests():

    print("\nRunning automated tests...")

    test_collection = []

    # Test adding a book
    test_collection = add_book(
        test_collection,
        "The Way of Kings",
        "Brandon Sanderson",
        "Fantasy",
        "9781000000001",
        ("epic", "long", "adventure")
    )

    assert len(test_collection) == 1, "Add book failed"

    # Test searching by ISBN
    assert get_book(
        test_collection, "9781000000001"
    ) == (
        "The Way of Kings", "Brandon Sanderson"
    ), "ISBN search failed"

    # Test missing ISBN
    assert get_book(
        test_collection, "0000000000000"
    ) == (), "Missing ISBN test failed"

    # Test tuple-to-set conversion
    assert test_collection[0][TAGS] == {
        "epic", "long", "adventure"
    }, "Tuple-to-set conversion failed"

    # Test searching by multiple tags
    assert len(
        books_with_tags(test_collection, {"epic", "long"})
    ) == 1, "Tag search failed"

    # Test tags that do not match
    assert len(
        books_with_tags(test_collection, {"epic", "romance"})
    ) == 0, "Tag filtering failed"

    # Test author search
    assert len(
        books_by_author(test_collection, "sanderson")
    ) == 1, "Author search failed"

    # Test genre search
    assert len(
        books_by_genre(test_collection, "fantasy")
    ) == 1, "Genre search failed"

    # Test unique author list
    assert list_authors(test_collection) == [
        "Brandon Sanderson"
    ], "Author list failed"

    # Test duplicate ISBN prevention
    original_count = len(test_collection)

    test_collection = add_book(
        test_collection,
        "Duplicate Book",
        "Another Author",
        "Fantasy",
        "9781000000001",
        ("duplicate",)
    )

    assert len(test_collection) == original_count, \
        "Duplicate ISBN prevention failed"

    print("\nAll automated tests passed!")


# MAIN INTERACTIVE APPLICATION

def main():

    # BOOK GALLERY 12 BOOKS

    collection = [
        {
            TITLE: "The Way of Kings",
            AUTHOR: "Brandon Sanderson",
            GENRE: "Fantasy",
            ISBN: "9781000000001",
            TAGS: {"epic", "adventure", "magic"}
        },
        {
            TITLE: "Parable of the Sower",
            AUTHOR: "Octavia Butler",
            GENRE: "Science Fiction",
            ISBN: "9781000000002",
            TAGS: {"sci-fi", "dystopian", "futuristic"}
        },
        {
            TITLE: "1984",
            AUTHOR: "George Orwell",
            GENRE: "Dystopian Fiction",
            ISBN: "9781000000003",
            TAGS: {"classic", "politics", "dystopian"}
        },
        {
            TITLE: "The Power Broker",
            AUTHOR: "Robert A. Caro",
            GENRE: "Biography",
            ISBN: "9781000000004",
            TAGS: {"history", "politics", "leadership"}
        },
        {
            TITLE: "Crazy Rich Asians",
            AUTHOR: "Kevin Kwan",
            GENRE: "Contemporary Fiction",
            ISBN: "9781000000005",
            TAGS: {"family", "romance", "culture"}
        },
        {
            TITLE: "Things Fall Apart",
            AUTHOR: "Chinua Achebe",
            GENRE: "Literary Fiction",
            ISBN: "9781000000006",
            TAGS: {"africa", "classic", "colonialism"}
        },
        {
            TITLE: "She Would Be King",
            AUTHOR: "Wayetu Moore",
            GENRE: "Historical Fantasy",
            ISBN: "9781000000007",
            TAGS: {"africa", "mythology", "history"}
        },
        {
            TITLE: "The Coldest Winter Ever",
            AUTHOR: "Sistah Souljah",
            GENRE: "Urban Fiction",
            ISBN: "9781000000008",
            TAGS: {"urban", "drama", "coming_of_age"}
        },
        {
            TITLE: "Down These Mean Streets",
            AUTHOR: "Piri Thomas",
            GENRE: "Memoir",
            ISBN: "9781000000009",
            TAGS: {"memoir", "identity", "culture"}
        },
        {
            TITLE: "Ordinary Girls",
            AUTHOR: "Jaquira Díaz",
            GENRE: "Memoir",
            ISBN: "9781000000010",
            TAGS: {"memoir", "family", "identity"}
        },
        {
            TITLE: "Girls Burn Brighter",
            AUTHOR: "Shobha Rao",
            GENRE: "Literary Fiction",
            ISBN: "9781000000011",
            TAGS: {"friendship", "resilience", "international"}
        },
        {
            TITLE: "The Kite Runner",
            AUTHOR: "Khaled Hosseini",
            GENRE: "Historical Fiction",
            ISBN: "9781000000012",
            TAGS: {"family", "friendship", "redemption"}
        }
    ]

    print("\n" + "=" * 45)
    print("WELCOME TO THE BITY BOOK GALLERY EDITOE!")
    print("=" * 45)
    print("Your current collection contains", len(collection), "books.")

    # INTERACTIVE MENU

    while True:

        print("\n========== BOOK GALLERY ==========")
        print("1. View All Books")
        print("2. Add a New Book")
        print("3. Search by ISBN")
        print("4. Search by Tags")
        print("5. Search by Author")
        print("6. Search by Genre")
        print("7. List All Authors")
        print("8. Run Automated Tests")
        print("9. Exit")

        choice = input("\nChoose an option (1-9): ").strip()

        # OPTION 1: VIEW ALL BOOKS
        if choice == "1":

            print("\nYOUR BOOK COLLECTION")
            display_books(collection)

        # OPTION 2: ADD NEW BOOK
        elif choice == "2":

            print("\nADD A NEW BOOK")

            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            genre = input("Genre: ").strip()
            isbn = input("ISBN: ").strip()

            tag_input = input(
                "Enter tags separated by commas: "
            )

            tags = tuple(
                tag.strip().lower()
                for tag in tag_input.split(",")
                if tag.strip()
            )

            if title and author and genre and isbn:

                collection = add_book(
                    collection,
                    title,
                    author,
                    genre,
                    isbn,
                    tags
                )

            else:
                print("\nAll book fields are required.")

        # OPTION 3: SEARCH BY ISBN
        elif choice == "3":

            isbn = input("\nEnter ISBN to search: ").strip()

            result = get_book(collection, isbn)

            if result:
                print("\nBook found!")
                print("Title: " + result[0])
                print("Author: " + result[1])

            else:
                print("\nNo book found with that ISBN.")

        # OPTION 4: SEARCH BY TAGS
        elif choice == "4":

            tag_input = input(
                "\nEnter tags separated by commas: "
            )

            tags = {
                tag.strip().lower()
                for tag in tag_input.split(",")
                if tag.strip()
            }

            if tags:

                results = books_with_tags(collection, tags)

                print("\nTAG SEARCH RESULTS")
                display_books(results)

            else:
                print("\nPlease enter at least one tag.")

        # OPTION 5: SEARCH BY AUTHOR
        elif choice == "5":

            author = input(
                "\nEnter author name: "
            ).strip()

            if author:

                results = books_by_author(collection, author)

                print("\nAUTHOR SEARCH RESULTS")
                display_books(results)

            else:
                print("\nPlease enter an author name.")

        # OPTION 6: SEARCH BY GENRE
        elif choice == "6":

            genre = input(
                "\nEnter genre: "
            ).strip()

            if genre:

                results = books_by_genre(collection, genre)

                print("\nGENRE SEARCH RESULTS")
                display_books(results)

            else:
                print("\nPlease enter a genre.")

        # OPTION 7: LIST ALL AUTHORS
        elif choice == "7":

            print("\nAUTHORS IN YOUR COLLECTION")

            for author in list_authors(collection):
                print("- " + author)

        # OPTION 8: RUN AUTOMATED TESTS
        elif choice == "8":

            run_tests()

        # OPTION 9: EXIT
        elif choice == "9":

            print("\n" + "=" * 45)
            print("THANK YOU FOR VISITING BITY BOOK GALLERY!")
            print("=" * 45)
            print("Happy Reading!")
            break

        # INVALID MENU SELECTION
        else:

            print("\nInvalid selection. Choose 1-9.")


# START THE PROGRAM

if __name__ == "__main__":
    main()
