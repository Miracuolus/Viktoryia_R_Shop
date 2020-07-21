from decimal import Decimal
from bookapp.models import Book

def rating_from_comment(value, book):
    count = 0
    r = []
    for c in value.all():
        if c.rating:
            count += 1
            r.append(c.rating)
            sum_rating = 0
            for i in r:
                sum_rating += int(i)
            rating  = sum_rating/count
            Book.objects.filter(pk=book).update(rating=Decimal(rating))
