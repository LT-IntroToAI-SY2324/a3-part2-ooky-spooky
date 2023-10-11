from typing import List, Tuple

games_db: List[Tuple[str, str, int, List[str]]] = [
        (
            "Amnesia, the Dark Descent", # title 
            "Frictional Games", # developer
            2010, # year released
            "Alexander of Brennenburg", # villian 
            [
                "Alois", # characters 
                "Basile",
                "Daniel",
                "Justine Florbelle",
                "Malo",
                "Alexander of Brennenburg"
            ],
        ),

        (
            "Alien, Isolation", # title 
            "Craetive Assembly", # developer
            2014, # year released
            "Alien Xenomorph", # villian 
            [
                "Amanda Ripley", # characters 
                "Axel",
                "Ricardo",
                "Lingard",
                
            ],
        ),

        (
            "Slender: The Eight Pages", # title 
            "Parsec Productions", # developer
            2012, # year released
            "Slenderman", # villian 
            [
                "Slenderman", # characters 
                "Unnamed player",
            ],
        ),

        (
            "Resident Evil Village", # title 
            "Capcom", # developer
            2021, # year released
            "Albert Wesker", # villian 
            [
                "Ethan Winters", # characters 
                "Chris Redfield",
                "Mia Winters",
                "Rosemary Winters",
                "Alcina Dimitrescu",
                "The Duke",
                "Mother Miranda",
                "Salvaore Moeau",
                "Donna Bennevieno",
                "Karl Heisenberg",
                
            ],
        ),

        (
            "Prey", # title 
            "Arkane Austin", # developer
            2017, # year released
            "Mother", # villian 
            [
                "Morgan Yu",
                "Alex Yu",
                "January",
                "Cystoids",
                "Mimic",
                "Nightmare",
                "Phantom",
                "Poltergeist",
                "Telepath",
                "Technopath",
                "Weaver",
            ],
        ),
]

books_db: List[Tuple[str, str, int, List[str]]] = [   #### WE HAVE AN ERROR SOMEWHERE -- [ AND ( NOT CLOSED, remember to be on the lookout for it :3 - Cat
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
                "dick hallorann",
            ],  # characters
        ),
        (
            "dracula",
            "bram stoker",
            1897,
            "count dracula",
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
            "carrie white",
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
            "frankenstein",
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
            "alma katsu",
            2018,
            "james reed",
            [
                "elitha donner",
                "tamsen donner",
                "charles stanton",
                "mary graves",
                "jean-baptiste trudeau",
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
            "unnamed monster",
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
            "charles manx",
        
            [
                "charles manx",
                "vic mcqueen",
                "linda mcqueen",
                "chris mcqueen",
                "lou carmody",
            ],
        ),
]

movies_db: List[Tuple[str, str, int, List[str]]] = [
    (
        "Get Out",
        "Jordan Peele", # director
        "R", #rating
        2017, # year 
        [
            "Daniel Kaluuya", #actors
            "Allison Williams",
            "Bradley Whitford",
            "Catherine Keener",
            "Caleb Landry Jones",
            "Marcus Henderson",
        ],
    ),

    (
        "The Ring",
        "Gore Verbinski", # director
        "PG-13", #rating
        2016, # year 
        [
            "Naomi Watts", #actors
            "Martin Henderson",
            "David Dorfman",
            "Brian Cox",
            "Jane Alexander",
            "Lindsay Frost",
        ],
    ),
    
      (
        "Halloween",
        "John Carpenter", # director
        "R", #rating
        1978, # year 
        [
            "Jamie Lee Curtis", #actors
            "Donald Pleasance",
            "Tony Moran",
            "Nancy Kyes",
            "Brian Andrews",
            "Charles Cyphers",
        ],
    ),

    (
        "Hush",
        "Mike Flanagan", # director
        "R", #rating
        2016, # year 
        [
            "John Gallaghper Jr.", #actors
            "Kate Siegel",
            "Micheal Trucco",
            "Samantha Sloyan",
            "Emma Graves",
            
        ],
    ),

    (
        "The Conjuring",
        "James Wan", # director
        "R", #rating
        2013, # year 
        [
            "Patrick Wilson", #rating
            "Vera Farminga",
            "Ron Livingston",
            "Lili Taylor",
            "Shanley Caswell",
            "Heyley McFarland",
        ],
    ),

]