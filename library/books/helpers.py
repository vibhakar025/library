from datetime import date, datetime
from books.models import Books, Circulation, CirculationHistory


ACTION_CHECKOUT = 1
ACTION_RETURN = 2

def is_book_available(bookId):
    book = Books.objects.filter(BookID = bookId).first()
    if book:
        if book.NumberOfCopies > 0:
            return True
    return False

def is_book_allocated(bookId, memberId):
    circulation = Circulation.objects.filter(MemberId = memberId, BookId = bookId).order_by('-Date').first()
    if circulation and circulation.EventType == ACTION_CHECKOUT:
        return True
    return False


def registerCirculationEvent(data, action):
    eventType = action
    date = data.get('date')
    bookId = data.get('book_id')
    memberId = data.get('member_id')
    event = CirculationHistory(EventType = eventType, BookId = bookId, MemberId = memberId, Date = date)
    event.save()

    if eventType == ACTION_CHECKOUT:
        circulation = Circulation(EventType = eventType, BookId = bookId, MemberId = memberId, Date = date)
        circulation.save()
    else:
        circulation = Circulation.objects.filter(EventType = ACTION_CHECKOUT, BookId = bookId, MemberId = memberId).first()
        if circulation:
            circulation.EventType = eventType
            circulation.Date = date
            circulation.save()

def updateBooks(bookId, action):
    book = Books.objects.filter(BookID = bookId).first()  
    #allocate
    if action == ACTION_CHECKOUT:
        book.NumberOfCopies -= 1       
    #deallocate
    elif action == ACTION_RETURN: 
        book.NumberOfCopies += 1   
    book.save()


def get_overdues_data(memberId):
    all_books = Circulation.objects.filter(EventType = ACTION_CHECKOUT, MemberId = memberId)

    date_str = '05-31-2023'

    date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
    today = date_object
    
    fines = list()

    for book in all_books:
        checkout_date = book.Date
        delta = today - checkout_date
        if delta.days > 7:
            fine = dict()
            fine['book'] = book.BookId
            fine['amount'] = (delta.days - 7) * 50
            fines.append(fine)

    return fines



    


