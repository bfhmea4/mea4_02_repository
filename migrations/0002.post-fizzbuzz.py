
from yoyo import step

__depends__ = {'0000.initial-schema', '0001.create-fizzbuzz'}

steps = [
    step(
        "INSERT INTO fizzbuzz VALUES(1, '{response}','{request}')",

    ),
    step(
        "DELETE FROM fizzbuzz WHERE id = 1"
    )
]