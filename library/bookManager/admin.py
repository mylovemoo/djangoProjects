from django.contrib import admin

from .models import Book,Author,Publish

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['admin_name']}),
        ('BookInfo', {'fields': ['book_author'], 'classes':['collapse']}),
    ]
    list_display = ('book_name', 'book_pubdate', 'book_author')

admin.site.register(Book,BookAdmin}
#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Publish)
