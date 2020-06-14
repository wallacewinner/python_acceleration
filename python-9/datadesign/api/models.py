from django.db import models
from django.core import validators


class User(models.Model):
    name = models.CharField('Name', max_length =  50)
    last_login = models.DateField('Last_login', auto_now = True)
    email = models.CharField('Email', max_length = 254,
            validators = [validators.EmailValidator()])
    password = models.CharField('Password', max_length = 50,
            validators = [validators.MinLengthValidator(8)])


class Agent(models.Model):
    name = models.CharField('Name', max_length = 50)
    status = models.BooleanField()
    env = models.CharField('Env')
    version = models.CharField('Version', max_length = 5)
    address = models.GenericIPAddressField('Address', 
                                    max_length = 39,
                                    protocol = 'IPv4') 

class Group(models.Model):
    name = models.CharField('Name', max_length = 50)

class Event(models.Model):
    def level(self, level):
        if (level not in ['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO']):
            raise TypeError(f'Wrong input {level}')

    level = models.CharField('level', max_length = 20, validators=[level])
    data = models.TextField('data')
    arquivado = models.BooleanField('arquivado')
    date = models.DateField('date', auto_now = True)
    agent = models.ForeignKey(Agent, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
