from peewee import *

from user_srv.settings import settings


class BaseModel(Model):
    class Meta:
        database = settings.DB


class User(BaseModel):
    GENDER_CHOICES = (
        ("female", "female"),
        ("male", "male")
    )

    ROLE_CHOICES = (
        (1, "user"),
        (2, "admin")
    )

    mobile = CharField(max_length=11, index=True, unique=True, verbose_name="phone mobile")
    password = CharField(max_length=200, verbose_name="password")
    nick_name = CharField(max_length=20, null=True, verbose_name="username | nick_name")
    profile_img_url = CharField(max_length=200, null=True, verbose_name="profile img")
    birthday = DateField(null=True, verbose_name="birthday")
    address = CharField(max_length=200, null=True, verbose_name="address")
    desc = TextField(null=True, verbose_name="personal description")
    gender = CharField(max_length=6, choices=GENDER_CHOICES, null=True, verbose_name="gender")
    role = IntegerField(default=1, choices=ROLE_CHOICES, verbose_name="role")


if __name__ == "__main__":
    settings.DB.create_tables([User])
