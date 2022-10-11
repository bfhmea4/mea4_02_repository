# file: migration/0001.create-foo.py
from yoyo import step
steps = [
    step(
        "CREATE TABLE fizzbuzz (id INT, response VARCHAR(20), request INT, PRIMARY KEY (id))",
        "DROP TABLE fizzbuzz"
    )
]

