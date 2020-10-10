import inspect
from .BaseDoc import BaseDoc


def validate_docs(documents):
    """Recebe uma lista de tuplas (ClasseDoc, NumeroDoc) e a valida"""
    validations = []

    for doc in documents:
        if not inspect.isclass(doc[0]) or not issubclass(doc[0], BaseDoc):
            raise TypeError(
                "O primeiro índice da tupla deve ser uma classe de documento!"
            )

        validations.append(doc[0]().validate(doc[1]))

    return validations
