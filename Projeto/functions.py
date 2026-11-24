import json




all_books = {
     "books": []
}
global title
global author
global year
global pages
global genre
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
      try:
       with open("library.json", "r") as file:
            global all_books
            all_books = json.load(file)
            print("Files loaded!")
      except FileNotFoundError:
            print("You don't have a json file to load")
      except json.JSONDecodeError:
            print("The content of your json is invalid. Try changing it!")

            
      















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
           if completed_book_text.lower() =='y':
               print("Ok.")
               completed_book = True
               break
           elif completed_book_text.lower() == 'n':
               print("Ok.")
               completed_book = False
               break
           else:
               print("You typed wrong. Let's try again.")
          print("What Genre is it?")
          genre = str(input())

          print("Thanks for your information.")
          book_inf = {
               "title": title,
               "author": author,
               "year": year,
               "pages": pages,
               "completed": completed_book,
               "genre": genre
                     }
          all_books["books"].append(book_inf)
          


def search_books():
     found = False
     print("Ok, let's search for your books")
     print("Type what book do you wish to search:")
     search = str(input())
     for i in all_books["books"]:
          if search.lower() == i["title"].lower():
                    print(f"We found your book! It is {i["title"]}")
                    print(f"It was made by: {i["author"]}, was released in: {i["year"]}")
                    print(f"And it has {i["pages"]} pages.")
                    print(f"It's Genre is {i["genre"]}.")
                    if i["completed"] == True:
                        print("And you've completed it already.")
                    else:
                        print("You didnt complete it.")
                    found  = True
     if found == False:
          print("We didn't found your book. Try to add it in the add books tab")


def remove_books():
          print("Okay, let's remove the book you need")
          print("Type what book do you wish to remove:")
          search = str(input())
          for i in all_books["books"]:
               if search.lower() == i["title"].lower():
                         print(f"We found your book! It is {i["title"]}")
                         print(f"Okay, let's delete {i["title"]}")
                         
                         all_books["books"].remove(i)
                         print(f"Okay, we've removed {i} from your list")
                         foundToremove = True
                         break
          if foundToremove == False:
               print("We didn't found your book. Try to add it in the add books tab")


def mark_as_read():
          print("Okay, first, we need to search your book")
          print("Type what book do you wish to search:")
          search = str(input())
          for i in all_books["books"]:
               if search.lower() == i["title"].lower():
                         print(f"We found your book! It is {i["title"]}")
                         if i["completed"] == True:
                               print("You have already read it")
                         else:
                               print(f"Okay, let's mark {i["title"]} as read")
                               i["completed"] = True
                               print(f"We marked {i["title"]} as read.")
                         foundMark = True
          if foundMark == False:
               print("We didn't found your book. Try to add it in the add books tab")                    
               
        
def list_books():
      print("Okay, let's list your books!")
      for i in all_books["books"]:
            show_book(i)



def edit_books():
                print("Ok, firstly, we need to search your book")
                print("Type what book do you wish to search:")
                search = str(input())
                for i in all_books["books"]:
                     if search.lower() == i["title"].lower():
                               print(f"We found your book! It is {i["title"]}.")
                               foundToEdit = True
                               while True:
                                print("EDIT MENU")
                                print("1. Edit Title")
                                print("2. Edit Author")
                                print("3. Edit Year of Publication")
                                print("4. Edit Number of pages")
                                print("5. Edit Genre")
                                print("6. Exit edit menu")
                                print("Type What you want to do")
                                opmenu = int(input())
                                if opmenu == 1:
                                     print("Ok, let's edit the title")
                                     print("Type it below")
                                     i["title"] = str(input())
                                     print("Ok, name changed!")
                                     print("Do you want to edit something else?")
                                     print("Type below Y for yes and N for no")
                                     optitle = str(input())
                                     if optitle.lower() == "y":
                                           continue
                                     else:
                                           break
                                elif opmenu == 2:
                                      print("Ok, let's edit the author")
                                      print("Type it below")
                                      i["author"] = str(input())
                                      print("Ok, Author changed!")
                                      print("Do you want to edit something else?")
                                      print("Type below Y for yes and N for no")
                                      optitle = str(input())
                                      if optitle.lower() == "y":
                                          continue
                                      else:
                                          break
                                elif opmenu == 3:
                                      print("Ok, let's edit the Year of release")
                                      print("Type it below")
                                      i["year"] = int(input())
                                      print("Ok, Year changed!")
                                      print("Do you want to edit something else?")
                                      print("Type below Y for yes and N for no")
                                      optitle = str(input())
                                      if optitle.lower() == "y":
                                          continue
                                      else:
                                         break
                                elif opmenu == 4:
                                      print("Ok, let's edit the Number of pages")
                                      print("Type it below")
                                      i["pages"] = int(input())
                                      print("Ok, Number of pages changed!")
                                      print("Do you want to edit something else?")
                                      print("Type below Y for yes and N for no")
                                      optitle = str(input())
                                      if optitle.lower() == "y":
                                              continue
                                      else:
                                           break
                                elif opmenu == 5:
                                       print("Ok, let's edit the Genre")
                                       print("Type it below")
                                       i["genre"] = str(input())
                                       print("Ok, Genre changed!")
                                       print("Do you want to edit something else?")
                                       print("Type below Y for yes and N for no")
                                       optitle = str(input())
                                       if optitle.lower() == "y":
                                               continue
                                       else:
                                            break
                                      



                                
                                elif opmenu == 6:
                                      print("Ok, exiting the edit menu.")
                                      break
                if foundToEdit == False:
                      print("We didn't found your book :( try again!")
                  
                    
                                      
                                    
      



def show_book(i):
      print(f"Title: {i["title"]}")
      print(f"Author: {i["author"]}")
      print(f"Year of Release: {i["year"]}")
      print(f"Number of pages: {i["pages"]}")
      print(f"Genre: {i["genre"]}")
      if i["completed"] == True:
            print("Completed: Yes")
      else:
            print("Completed: No")

