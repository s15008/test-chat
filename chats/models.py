from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date publish')

    def __str__(self):
        return self.user_name

class Board(models.Model):
    board_name = models.CharField(max_length=100)
    admin_id = models.ForeignKey(User)
    pub_date = models.DateTimeField('date publish')

    def __str__(self):
        return self.board_name

class Message(models.Model):
    DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S:%f %z'

    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User)
    message = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publish')

    def get_formated_pub_date(self):
        return self.pub_date.strftime(self.DATETIME_FORMAT)

    def __str__(self):
        return self.message
