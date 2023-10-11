from typing import List, Tuple

books_db: List[Tuple[str, str, int, List[str]]] = [
    (
        "it",  # title
        "stephen king",  # author
        1986,  # year released
        "pennywise", #main villian
        [
            "richie tozier",
            "eddie kasbrak",
            "ben hanscom",
            "mike hanlon",
            "dick hallorann"
        ],  # characters
    ),
    (
        "dracula",
        "bram stoker",
        1897,
        "count dracula"
        [
            "mina harker",
            "jonathan harker",
            "arthur holmwood",
            "renfield",
            "dr. john seward",
        ],
    ),
    (
        "carrie",
        "stephen king",
        1974,
        "carrie white"
        [
            "margaret white",
            "sue snell",
            "rita desjardin",
            "chris hargensen",
        ],
    ),
    (
        "frankenstein",
        "mary shelley",
        1818, # oldest book in this database
        "frankenstein"
        [
            "victor frankenstein",
            "cxaptin robert walton",
            "elizabeth lavenza",
            "dr. henry clerval",
        ],
    ),
    (
        "bird box",
        "josh malerman",
        2014, 
        "malevolent beings",
        [
            "tom",
            "jules",
            "victor (dog)",
            "felix",
            "malorie",
            "shannon",
        ],
    ),
    (
        "rosemary's baby",
        "ira levin",
        1967,
        "the castevets",
        [
            "rosemary woodhouse",
            "roman castevet",
            "guy woodhouse",
            "minnie castevet",
            "the devil",
            "mr. nicklas",
        ],
    ),
    (
        "the woman in black",
        "susan hill",
        1983,
        "woman in black",
        [
            "arthur kipps",
            "alice drablow",
            "mr. jerome",
            "mr. daily",
            "keckwick",
        ],
    ),
    (
        "the hunger",
        "alma katsu"
        2018,
        "james reed",
        [
            "elitha donner",
            "tamsen donner",
            "charles stanton",
            "mary graves",
            "jean-baptiste trudeau"
        ],
    ),
    (
        "ring",
        "koji suzuki",
        1991,
        "sadako yamamura",
        [
            "kazuyuki asakawa",
            "ryuji takayama",
            "shizuki asakawa",
            "yoko asakawa",
        ],
    ),
    (
        "house of leaves",
        "mark z. danielewski",
        2000,
        "",
        [
            "johnny truant",
            "zampano",
            "lude",
            "will navidson",
        ],
    ),
    (
        "a head full of ghosts",
        "paul g. tremblay",
        2015,
        "marjorie",
        [
            "meredith (merry) barrett",
            "marjorie berrett",
            "john barrett",
            "sarah barrett",
        ],
    ),
    (
        "come closer",
        "sara gran",
        2003,
        "naamah",
        [
            "amanda",
            "adam",
        ],
    ),
    (
        "no24r2",
        "joe hill, gabriel rodriguez",
        2013,
        "charles manx"
        
        [
            "charles manx",
            "vic mcqueen",
            "linda mcqueen",
            "chris mcqueen",
            "lou carmody",
        ],
    ),