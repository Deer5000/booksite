How would we filter for all books with titles containing the word ‘Django’?

    You would create a variable named 'fiter_by_titlename_django' then you would set it equal to "Book.objects.filter(title.icontains ='Django')



How would we filter for all books with tag ‘Fiction’?
    Book.objects.filter(tags.name = 'Fiction')



How would we filter for all authors who have written books containing the word ‘Django’? HINT: We can use the book field to refer to an author’s books, even though the Author model doesn’t explicitly contain it!


    Book.objects.filter(book.icontains = 'Django')