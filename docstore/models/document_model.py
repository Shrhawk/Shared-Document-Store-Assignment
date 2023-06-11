from django.db import models

from docstore.models.base_model import BaseModel


class Document(BaseModel):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/")
    folder = models.ForeignKey(
        "Folder", on_delete=models.CASCADE, related_name="documents"
    )
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
