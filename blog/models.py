from stonehenge.db import fields, models


class BlogPost(models.Model):
    created_at = fields.DateTimeField()
    created_by = fields.ForeignKeyField("User")
    title = fields.CharField(max_length=15)
    is_awesome = fields.BooleanField(default=True)

    def __str__(self):
        return f"Blog Post: {self.title}"
