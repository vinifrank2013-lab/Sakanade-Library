import json




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

def save_json():
      print("Okay, let's save your library in JSON")

      with open("library.json", "w") as file:
            json.dump(all_books, file, indent=4)
      print("Your library is now save on json format!")

def load_json():
      print("Okay, let's load your library from json")

      with open("library.json", "r") as file:
            all_books = json.load(file)
      print("We loaded your files!")
      
















def add_books():
     print("Ok, let's add some books to your collection!")
     print("How many books would you like to add?")
     num_books = int(input())
     for i in range(num_books):
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
          book_inf = {
               "title": title.lower(),
               "author": author,
               "year": year,
               "pages": pages,
               "completed": completed_book
                     }
          all_books["books"].append(book_inf)
          


def search_books():
     print("Ok, let's search for your books")
     print("Type what book do you wish to search:")
     search = str(input())
     for i in all_books["books"]:
          if search.lower == i[0].lower:
                    print(f"We found your book! It is {i[0]}")
                    print(f"It was made by: {i[1]}, was released in: {i[2]}")
                    print(f"And it has {i[3]} pages.")
                    if completed_book == True:
                        print("And you've completed it already.")
                    else:
                        print("You didnt complete it.")
                    book_found = True
     if book_found == False:
          print("We didn't found your book. Try to add it in the add books tab")


def remove_books():
          print("Okay, let's remove the book you need")
          print("Type what book do you wish to remove:")
          search = str(input())
          for i in all_books["books"]:
               if search.lower == i[0].lower:
                         print(f"We found your book! It is {i[0]}")
                         print(f"Okay, let's delete {i[0]}")
                         all_books["books"].remove(i)
                         print(f"Okay, we've removed {i} from your list")
                         book_found = True
          if book_found == False:
               print("We didn't found your book. Try to add it in the add books tab")


def mark_as_read():
          print("Okay, first, we need to search your book")
          print("Type what book do you wish to search:")
          search = str(input())
          for i in all_books["books"]:
               if search.lower == i[0].lower:
                         print(f"We found your book! It is {title}")
                         if i[4] == True:
                               print("You have already read it")
                         else:
                               print(f"Okay, let's mark {i[0]} as read")
                               i[4] = True
                               print(f"We marked {i[0]} as read.")
                         book_found = True
          if book_found == False:
               print("We didn't found your book. Try to add it in the add books tab")                    
               
        
def list_books():
      print("Okay, let's list your books!")
      for i in all_books["books"]:
            show_book(i)



def edit_books():
      print
      



def show_book(i):
      print(f"Title: {i[0]}")
      print(f"Author: {i[1]}")
      print(f"Year of Release: {i[2]}")
      print(f"Number of pages: {i[3]}")
      if i[4] == True:
            print("Completed: Yes")
      else:
            print("Completed: No")
     