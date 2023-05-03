from .IDTOModel import IDTOModel

class IMaterial(IDTOModel):
    name: str

    @staticmethod
    def validate(material):
        if (hasattr(material, "name") or not material.name):
            pass
