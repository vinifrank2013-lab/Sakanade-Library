all_books = {
     "books": []
}
global title
global author
global year
global pages
global completed_book
global book_found
book_found = False
completed_book = False

def add_books():
     print("Ok, let's add some books to your collection!")
     print("How many books would you like to add?")
     num_books = int(input())
     for i in num_books:
          print("What's the name of this book?")
          title = str(input())
          print("What is the author of this book?")
          author = str(input())
          print("What is the year of this book?")
          year = int(input())
          print("How many pages are in your book?")
          pages = int(input())
          while True:
           print("You've completed it? Type Y for yes and N for no.")
           completed_book_text = str(input())
           if completed_book_text.lower =='y':
               print("Ok.")
               completed_book = True
               break
           elif completed_book_text.lower == 'n':
               print("Ok.")
               completed_book = False
               break
           else:
               print("You typed wrong. Let's try again.")

          print("Thanks for your information.")
          book_inf = [title.lower, author, year, pages]
          title2 = title
          title2 = book_inf
          all_books['books'].append(title2)
     
          


def search_books():
     print("Ok, let's search for your books")
     print("Type what book do you wish to search:")
     search = str(input())
     for i in all_books["books"]:
          if search.lower == title.lower:
                    print(f"We found your book! It is {title}")
                    print(f"It was made by: {author}, was released in: {year}")
                    print(f"And it has {pages} pages.")
                    if completed_book == True:
                        print("And you've completed it already.")
                    else:
                        print("You didnt complete it.")
                    book_found == True
     if book_found == False:
          print("We didn't found your book. Try to add it in the add books tab")


                   
                    
               
        

     