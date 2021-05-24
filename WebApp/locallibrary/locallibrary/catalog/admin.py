from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    # pass
    # 这样将会在xx/catalog/author/ 网页的作者列表中展示作者list_display中所有的信息
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    # fields可以控制元组的展示；
    # 字段默认情况下垂直显示，但如果您进一步将它们分组在元组中（如上述“日期”字段中所示），则会水平显示
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# admin.site.register(Author) # 注册AuthorAdmin的话需要注释掉Author的注册
admin.site.register(Author, AuthorAdmin)  # 注册AuthorAdmin


# admin.site.register(Book)
# 使用decorator注册Book的管理类
@admin.register(Book)  # 使用注释的方式注册
class BookAdmin(admin.ModelAdmin):
    # pass
    # 不幸的是，我们不能直接指定 list_display 中的 genre 字段， 因为它是一个ManyToManyField
    # （Django可以防止这种情况，因为在这样做时会有大量的数据库访问“成本”）。
    # 于是，我们将定义一个 display_genre 函数来获取信息作为一个字符串（
    # 这是我们上面调用的函数;下面我们将定义它）。
    list_display = ('title', 'author', 'display_genre')
    fields = ['summary', ('title', 'author'), ('isbn', 'genre')]


admin.site.register(Genre)


# admin.site.register(BookInstance)
# 使用decorator注册BookInstance的管理类
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # book 不是many同many的所以可以直接展示，会展示其str(book)
    # 但是book的Author就需要单独写方法来展示
    list_display = ('__str__', 'book', 'book_author', 'status', 'due_back')
