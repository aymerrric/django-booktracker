from django.contrib import admin
from booktracker.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    fieldsets = [("Book properties", {"fields": ["name", "pages"]}),
                 ("Appreciation", {"fields": ["note", "status"]})]

admin.site.register(Book, BookAdmin)
