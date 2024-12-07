from passlib.hash import bcrypt
from tortoise import Model, fields


class UserModel(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=50)
    password = fields.CharField(max_length=255)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    def set_password(self, raw_password: str):
        self.password = bcrypt.hash(raw_password)

    def check_password(self, raw_password: str) -> bool:
        return bcrypt.verify(raw_password, self.password)

    def __str__(self):
        return self.username or self.email

    class Meta:
        table = "user"
