import sqlite3

# The program allows the user to:
# --Add new books to the database
# --update books to the database
# --delete books from the database
# --search the database to find a specific book
# I got help from realpython.com for writing docstrings.

               
def exit():        
    """Closes the database and shuts down the program."""            
        
    db = sqlite3.connect('ebookstore_db')        
    db.close()
    print('Database ebookstore_db is closed!')
    print('Good-bye')
    quit()

    
def create_table():        
    """Creates a table inside the database if the table does not exist.
        
    Raises
    ------
    Exception
        For all non exit exceptions.
    """
        
    try:
        db = sqlite3.connect('ebookstore_db')           
        cursor = db.cursor()
        with db:                                               
            cursor.execute('''CREATE TABLE IF NOT EXISTS
                        book(ID INTEGER PRIMARY KEY,
                        title TEXT NOT NULL COLLATE NOCASE,
                        author TEXT NOT NULL COLLATE NOCASE,
                        qty INTEGER NOT NULL)''')
            print('Table created successfully.')
    except Exception as e:
        raise e
    finally:
        db.close()
    
    
def in_put():        
    """Provides input options for ID, title, author, qty.       
        
    Raises
    ------
    ValueError
        If the data type entered for ID and qty is not an integer.
    """        
    while True:
        try:
            ID = int(input('Enter the book ID: '))
        except ValueError:
            print('Invalid entry...Try to enter an integer!')    
            in_put()
        title = input('Enter the book title: ')
        if title == '':
            print('You did not enter any value for title!')
            in_put()
        author = input('Enter the book author: ')
        if author == '':
            print('You did not enter any value for author!')
            in_put()
        try:
            qty = int(input('Enter the book quantity: '))
        except ValueError:
                print('Invalid entry...Try to enter an integer!')
                in_put()            
        insert_book(ID, title, author, qty)
        break
           

def insert_book(ID, title, author, qty):        
    """Inserts the book attributes into the table that's inside the database.

    Parameters
    ----------
    ID : int
        the book id to be inserted into the table.                     
    title : str
        the book title to be inserted into the table.
    author : str
        the book author to be inserted into the table.
    qty : int
        the book qty to be inserted into the table.
                
    Raises
    ------
    sqlite.3IntegrityError
        If the ID entered already exists in the table.
    """        
    try:
        db = sqlite3.connect('ebookstore_db')            
        cursor = db.cursor()
        # I used the context manager because it automatically commits or rollback.
        with db:                
            cursor.execute('''INSERT OR ABORT INTO book (ID, title, author,qty)
                            VALUES(?,?,?,?)''',(ID, title, author, qty))
            print(f"Book (ID:{ID}) titled '{title}' by author '{author}' inserted successfully.")
    except sqlite3.IntegrityError:
        print(f'ID {ID} already exists in the table!')
    finally:
        db.close()
        

def update_id(ID, New_ID):
    """Updates the current book ID with a new ID.

    Parameters
    ----------
    ID : int
        The current book ID to be replaced.
    New_ID : int
        The new book ID.
        
    Raises
    ------
    sqlite3.IntegrityError
    If the New_ID already exists in the table.
    """                
    try:
        db = sqlite3.connect('ebookstore_db')            
        cursor = db.cursor()
        with db:
            cursor.execute('''SELECT ID FROM book WHERE ID =?''', (ID,))
            result = cursor.fetchone()
            if result == None:
                print(f"Book (ID: {ID }) that you want to update doesn't exist...update was unsuccessful!")                
            else:        
                cursor.execute('''UPDATE book SET ID = ? WHERE ID = ?''',(New_ID,ID))                                              
                print(f'Book ID {ID} updated to {New_ID}')
    except sqlite3.IntegrityError:
        print(f'ID {ID} is already in use!')
    finally:
        db.close()
                                    

def update_title(ID, title):
    """Updates the book's title by using it's ID as an key.

    Parameters
    ----------
    ID : int
        The ID of the book title to be updated.
    title : str
        The new book title.
        
    Raises
    ------
    Exception
        For all non exit exceptions.
    """        
    try:
        db = sqlite3.connect('ebookstore_db')            
        cursor = db.cursor()
        
        with db:                        
            cursor.execute('''SELECT ID FROM book WHERE ID =?''', (ID,))
            result = cursor.fetchone()
            if result == None:
                print(f"Book (ID:{ID}) that you want to update doesn't exist...title update was unsuccessful!")
            else:
                cursor.execute('''UPDATE book SET title = ? WHERE ID = ?''',(title,ID))                                              
                print(f"Title for book (ID:{ID}) updated to new title '{title}'.")
    except Exception as e:
        raise e
    finally:
        db.close()


def update_author(ID, author):
    """Updates the book's author by using it's ID as a key.

    Parameters
    ----------
    ID : int
        The ID of the book author to be replaced.
    author : str
        The new book author.
        
    Raises
    ------
    Exception
        For all non exit exceptions.
    """        
    try:
        db = sqlite3.connect('ebookstore_db')            
        cursor = db.cursor()
        with db:                        
            cursor.execute('''SELECT ID FROM book WHERE ID =?''', (ID,))
            result = cursor.fetchone()
            if result == None:
                print(f"Book (ID:{ID}) that you want to update doesn't exist...author update was unsuccessful!")
            else:
                cursor.execute('''UPDATE book SET author = ? WHERE ID = ?''',(author,ID))                                              
                print(f"The author of book (ID:{ID}) updated to '{author}' successfully")
    except Exception as e:
        raise e
    finally:
        db.close()


def update_qty(ID, qty):
    """Updates the book's quantity by using it's ID as a key.

    Parameters
    ----------
    ID : int
        The ID of the book quantity to be updated.
    qty : int
        The new book qty.
        
    Raises
    ------
    Exception
        For all non exit exceptions.
    """                        
    try:
        db = sqlite3.connect('ebookstore_db')            
        cursor = db.cursor()
        with db:        
            cursor.execute('''SELECT ID FROM book WHERE ID =?''', (ID,))
            result = cursor.fetchone()
            if result == None:
                print(f"Book (ID:{ID}) that you want to update doesn't exist...qty update was unsuccessful!")
            else:
                cursor.execute('''UPDATE book SET qty = ? WHERE ID = ?''',(qty,ID))                                              
                print(f'Book (ID:{ID}) qty updated to {qty}')
    except Exception as e:
        raise e
    finally:
        db.close()


def remove_book(ID):
    """Removes the book from the table by using the ID as an argument.

    Parameters
    ----------
    ID : int
        The ID of the book to be removed.
                
    Raises
    ------
    Exception
        For all non exit exceptions.
    """        
    try:
        db = sqlite3.connect('ebookstore_db')            
        cursor = db.cursor()
        with db:        
            cursor.execute('''SELECT ID FROM book WHERE ID = ?''',(ID,))
            result = cursor.fetchone()                   
            if result == None:
                print(f'Book (ID:{ID}) does not exist.')                
            else:
                cursor.execute('''DELETE FROM book WHERE ID = ?''',(ID,))
                print(f'Book (ID:{ID}) has been removed.')
    except Exception as e:
        raise e
    finally:
        db.close()


def search_id(ID):
    """Searches for a book by using it's ID as a argument.

    Raises
    ------
    Exception
        For all non exit exceptions.                
    """        
    try:
        db = sqlite3.connect('ebookstore_db')
        db.row_factory = sqlite3.Row
        cursor = db.cursor()                
        with db:                         
            cursor.execute('''SELECT * FROM book 
                        WHERE ID = ? 
                        ''',(ID,))         
            result = cursor.fetchall()
            print(f'{len(result)} result/s found for ID: {ID}.')            
            for row in result:
                row_dict = dict(row)
                for k,v in row_dict.items():
                    print(f'{k}: {v}')
    except Exception as e:
        raise e
    finally:
        db.close()                    


def search_title(title):
    """Searches for a book by using one of it's title as an argument.

    Raises
    ------
    Exception
        For all non exit exceptions.                
    """        
    try:
        db = sqlite3.connect('ebookstore_db')
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        with db:                         
            cursor.execute('''SELECT * FROM book 
                        WHERE title = ? 
                        ''',(title,))         
            result = cursor.fetchall()
            print(f"{len(result)} result/s found for title '{title}' .")            
            for row in result:
                row_dict = dict(row)
                for k,v in row_dict.items():
                    print(f'{k}: {v}')
    except Exception as e:
        raise e
    finally:
        db.close()


def search_author(author):
    """Searches for a book by using it's author as an argument.

    Raises
    ------
    Exception
        For all non exit exceptions.                
    """        
    try:
        db = sqlite3.connect('ebookstore_db')
        db.row_factory = sqlite3.Row
        cursor = db.cursor()       
        with db:                         
            cursor.execute('''SELECT * FROM book 
                        WHERE author = ?
                        ''',(author,))         
            result = cursor.fetchall()
            print(f"{len(result)} result/s found for author '{author}'.")                    
            for row in result:
                row_dict = dict(row)
                for k,v in row_dict.items():
                    print(f'{k}: {v}')
    except Exception as e:
        raise e
    finally:
        db.close()    


def show_all():
    """Displays all the books in the table.

    Raises
    ------
    Exception
        For all non exit exceptions.                
    """                        
    try:
        db = sqlite3.connect('ebookstore_db')
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        with db:                                        
            cursor.execute('''SELECT * FROM book ''')
            result = cursor.fetchall()
            print(f'{len(result)} result/s found from your search.')
            for row in result:        
                row_dict = dict(row)                      
                for k,v in row_dict.items():
                    print(f'{k}: {v}')
                print()
    except Exception as e:
        raise e
    finally:
        db.close()


create_table()
while True:
    menu = ''              
    print('''
=== ebookstore main menu ===
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit              
''')
    try:
        menu = int(input('Enter your choice: '))            
    except ValueError:
        print('Invalid entry! Please enter an integer.')                                                                                                                  
    if menu == 1:               
        in_put()        
    elif menu == 2:
        while True:
            update_menu = ''                                
            print('''
=== Update menu ===
1. Update id
2. Update title
3. Update author
4. Update quantity
0. Back to main menu              
''')  
            try:
                update_menu = int(input('Enter your choice: '))            
            except ValueError:
                print('Invalid entry! Please enter an integer.')                     
            if update_menu == 1:
                try:
                    ID = int(input('Enter the current ID you want to update: '))
                    New_ID = int(input('Enter the New ID: '))                                                                
                    update_id(ID, New_ID)                        
                except ValueError:
                        print('Invalid entry! Please enter an integer.')                
            elif update_menu == 2:        
                try:
                    ID = int(input('Enter the ID of the book title you want to update: '))
                    title = input('Enter the new book title: ')
                    if title == '':
                        print('Title field cannot be empty!')                             
                    else:
                        update_title(ID, title)                                                
                except ValueError:
                    print('Invalid value entered.')                                                        
            elif update_menu == 3:        
                try:
                    ID = int(input('Enter the ID of the book author you want to update: '))
                    author = input('Enter the new book author: ')
                    if author == '':
                        print('Author field cannot be empty!')                
                    else:              
                        update_author(ID, author)                                                
                except ValueError:
                    print('Invalid value entered!')                                                    
            elif update_menu == 4:        
                try:
                    ID = int(input('Enter the ID of the book you want to update: '))
                    qty = int(input('Enter the new qty: '))                
                    update_qty(ID, qty)                                                
                except ValueError:
                    print('Invalid entry! Please enter an integer.')                                                
            elif update_menu == 0:
                break
            else:
                print('Choose between (1-4) or choose 0 for main menu.')
                                                                   
    elif menu == 3:    
        try:
            ID = int(input('Enter book ID to be removed: '))
            remove_book(ID)                
        except ValueError:
            print('Invalid value entered!')                        
    elif menu == 4:
        while True:
            search_menu = ''            
            print('''
=== Search menu ===
1. Search by id
2. Search by title
3. Search by author
4. Show all
0. Back to main menu
''')       
            try:
                search_menu = int(input('Enter your choice: '))                         
            except ValueError:
                print('Invalid entry! Please enter an integer: ')                                         
            if search_menu == 1:
                try:
                    ID = int(input('Enter ID of the book to search: '))                                                
                    search_id(ID)                    
                except ValueError:
                    print('Invalid entry! Please enter an integer.')
            elif search_menu == 2:                                            
                title = input('Enter the title of the book to search: ')
                search_title(title)                                    
            elif search_menu == 3:                                                            
                author = input('Enter the author of the book to search: ')
                search_author(author)                                    
            elif search_menu == 4:
                show_all()                
            elif search_menu == 0:                        
                break                
            else:
                print('Select between (1-4) or choose 0 for main menu.')
                                
    elif menu == 0:
        exit()
    else:
        print(f'Choice {menu} is not a valid option. Select between (1-4) or choose 0 to Exit.')
        

