from django.db import models
from django.urls import reverse  # 用于通过反转URL模式来生成URL
import uuid  # 请求具体某一本书实例所需要用到


# Create your models here.
class Genre(models.Model):
    """
    表示图书类型的Model（如 科幻类，武侠类）
    """
    name = models.CharField(max_length=200, help_text="输入一本书的类型（如：科幻，武侠）")

    def __str__(self):
        """
        模型对象转换会字符串的方法定义
        :return:
        """
        return self.name


class Book(models.Model):
    """
    表示一本书的模型
    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',  # 如果关联的类在引用之前尚未在此文件中定义，则必须使用模型的名称作为字符串
                               on_delete=models.SET_NULL,
                               # on_delete=models.SET_NULL 将作者的值设置为 Null 如果相关的作者记录被删除:删除了书的作者，对应的此作者的这本书也被从Author Model中删除
                               null=True,  # 如果没有作者被选择，这允许数据库存储一个 Null 值
                               )
    # 使用ForeignKey(外键)是因为书只能有一个作者，但是作者可以有多个书
    # Author作为字符串而不是对象，因为它还没有在文件中声明。
    summary = models.TextField(max_length=1000, help_text="输入这本书的简要描述")
    isbn = models.CharField('ISBN',
                            max_length=13,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre,  # Genre已经被定义，可以直接使用
                                   help_text="为这边书选择一个类型")

    # ManyToManyField：多对多，因为一本书可以属于多个类型，一个类型可以包含多本数
    # Genre的model已经定义，我们可以指定上面的对象

    def display_genre(self):
        """
        为类型创建一个字符串。这是在Admin中显示类型所必需的。
        :return:
        """
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'  # 这个定义了在网页展示时的简短列名

    def __str__(self):
        """
        Book model转换成字符串的方法定义
        :return:
        """
        return self.title

    def get_absolute_url(self):
        """
        返回访问特定图书实例的url。
        :return:
        """
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """
    表示具体的某一本书的示例模型
    """

    # UUIDField 用于设置 id 字段作为该模型的primary_key 。
    # 这个类型字段为每个实例分配一个全局唯一的值（用于在library库中可以找到的每本书）
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          help_text="在整个图书馆中这本图书的唯一ID标识")
    book = models.ForeignKey('Book',
                             on_delete=models.SET_NULL,
                             null=True)

    # 定义方法取得书的作者，在admin中使用
    def book_author(self):
        return self.book.author

    imprint = models.CharField(max_length=200)
    # DateField 用于due_back日期（书籍预期在借用或维护后可用）。
    # 该值可以是（blank或者null当该书可用时需要）
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    # status是CharField定义选择／选择列表。
    # 你可以看到我们定义一个包含键值对元组的元组，并将其传递给choices参数，而键是当选择该选项时实际保存的值。
    # 我们还设置了一个默认的值 “m” （维护），因为书籍最初将在库存之前创建不可用。
    status = models.CharField(max_length=1,
                              choices=LOAN_STATUS,
                              blank=True,
                              default='m',
                              help_text='本书的可用性状态')

    # 元数据（Class Meta）使用此字段在查询中返回时记录
    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """
        BookInstance model转换成字符串的方法定义
        :return:
        """
        return '%s(%s)' % (self.id, self.book.title)


class Author(models.Model):
    """
    表示Author的Model
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        返回访问特定作者实例的url。
        :return:
        """
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """
        Author Model转换成字符串的方法定义
        :return:
        """
        return '%s，%s' % (self.last_name, self.first_name)
