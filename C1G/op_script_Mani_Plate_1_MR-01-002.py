from pprint import pprint
from opentrons import protocol_api
import json
from pathlib import Path
from collections import defaultdict
from opentrons.types import Point

# metadata
metadata = {
    "protocolName": "MR-01-002-01",
    "author": "Annabel Basford <a.basford20@imperial.ac.uk>",
    "description": "MR-01-002_01",
    "apiLevel": "2.9",
}

move_commands = [
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "A1",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "A2",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "A3",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "A4",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "A5",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "A6",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "A7",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "A8",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "B1",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "B2",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "B3",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "B4",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "B5",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "B6",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "B7",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "B8",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "C1",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "C2",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "C3",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "C4",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "C5",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "C6",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "C7",
        ]
    },
    {
        "substance": "TriB",
        "amount": 162,
        "plate": 4,
        "location": [
            "C8",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "D1",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "D2",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "D3",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "D4",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "D5",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "D6",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "D7",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "D8",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "E1",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "E2",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "E3",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "E4",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "E5",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "E6",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "E7",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "E8",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "F1",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "F2",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "F3",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "F4",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "F5",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "F6",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "F7",
        ]
    },
    {
        "substance": "TriC",
        "amount": 114,
        "plate": 4,
        "location": [
            "F8",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "A1",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "A2",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "A3",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "A4",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "A5",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "A6",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "A7",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "A8",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "B1",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "B2",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "B3",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "B4",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "D1",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "D2",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "D3",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "D4",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "D5",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "D6",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "D7",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "D8",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "E1",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "E2",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "E3",
        ]
    },
    {
        "substance": "TriG",
        "amount": 42,
        "plate": 4,
        "location": [
            "E4",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "B5",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "B6",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "B7",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "B8",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "C1",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "C2",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "C3",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "C4",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "C5",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "C6",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "C7",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "C8",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "E5",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "E6",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "E7",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "E8",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "F1",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "F2",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "F3",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "F4",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "F5",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "F6",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "F7",
        ]
    },
    {
        "substance": "TriJ",
        "amount": 86,
        "plate": 4,
        "location": [
            "F8",
        ]
    },
    {
        "substance": "Di1",
        "amount": 105,
        "plate": 4,
        "location": [
            "A1",
        ]
    },
    {
        "substance": "Di1",
        "amount": 105,
        "plate": 4,
        "location": [
            "B5",
        ]
    },
    {
        "substance": "Di1",
        "amount": 105,
        "plate": 4,
        "location": [
            "D1",
        ]
    },
    {
        "substance": "Di1",
        "amount": 105,
        "plate": 4,
        "location": [
            "E5",
        ]
    },
    {
        "substance": "Di2",
        "amount": 161,
        "plate": 4,
        "location": [
            "A2",
        ]
    },
    {
        "substance": "Di2",
        "amount": 161,
        "plate": 4,
        "location": [
            "B6",
        ]
    },
    {
        "substance": "Di2",
        "amount": 161,
        "plate": 4,
        "location": [
            "D2",
        ]
    },
    {
        "substance": "Di2",
        "amount": 161,
        "plate": 4,
        "location": [
            "E6",
        ]
    },
    {
        "substance": "Di3",
        "amount": 153,
        "plate": 4,
        "location": [
            "A3",
        ]
    },
    {
        "substance": "Di3",
        "amount": 153,
        "plate": 4,
        "location": [
            "B7",
        ]
    },
    {
        "substance": "Di3",
        "amount": 153,
        "plate": 4,
        "location": [
            "D3",
        ]
    },
    {
        "substance": "Di3",
        "amount": 153,
        "plate": 4,
        "location": [
            "E7",
        ]
    },
    {
        "substance": "Di4",
        "amount": 105,
        "plate": 4,
        "location": [
            "A4",
        ]
    },
    {
        "substance": "Di4",
        "amount": 105,
        "plate": 4,
        "location": [
            "B8",
        ]
    },
    {
        "substance": "Di4",
        "amount": 105,
        "plate": 4,
        "location": [
            "D4",
        ]
    },
    {
        "substance": "Di4",
        "amount": 105,
        "plate": 4,
        "location": [
            "E8",
        ]
    },
    {
        "substance": "Di5",
        "amount": 161,
        "plate": 4,
        "location": [
            "A5",
        ]
    },
    {
        "substance": "Di5",
        "amount": 161,
        "plate": 4,
        "location": [
            "C1",
        ]
    },
    {
        "substance": "Di5",
        "amount": 161,
        "plate": 4,
        "location": [
            "D5",
        ]
    },
    {
        "substance": "Di5",
        "amount": 161,
        "plate": 4,
        "location": [
            "F1",
        ]
    },
    {
        "substance": "Di6",
        "amount": 164,
        "plate": 4,
        "location": [
            "A6",
        ]
    },
    {
        "substance": "Di6",
        "amount": 164,
        "plate": 4,
        "location": [
            "C2",
        ]
    },
    {
        "substance": "Di6",
        "amount": 164,
        "plate": 4,
        "location": [
            "D6",
        ]
    },
    {
        "substance": "Di6",
        "amount": 164,
        "plate": 4,
        "location": [
            "F2",
        ]
    },
    {
        "substance": "Di7",
        "amount": 183,
        "plate": 4,
        "location": [
            "A7",
        ]
    },
    {
        "substance": "Di7",
        "amount": 183,
        "plate": 4,
        "location": [
            "C3",
        ]
    },
    {
        "substance": "Di7",
        "amount": 183,
        "plate": 4,
        "location": [
            "D7",
        ]
    },
    {
        "substance": "Di7",
        "amount": 183,
        "plate": 4,
        "location": [
            "F3",
        ]
    },
    {
        "substance": "Di8",
        "amount": 184,
        "plate": 4,
        "location": [
            "A8",
        ]
    },
    {
        "substance": "Di8",
        "amount": 184,
        "plate": 4,
        "location": [
            "C4",
        ]
    },
    {
        "substance": "Di8",
        "amount": 184,
        "plate": 4,
        "location": [
            "D8",
        ]
    },
    {
        "substance": "Di8",
        "amount": 184,
        "plate": 4,
        "location": [
            "F4",
        ]
    },
    {
        "substance": "Di9",
        "amount": 109,
        "plate": 4,
        "location": [
            "B1",
        ]
    },
    {
        "substance": "Di9",
        "amount": 109,
        "plate": 4,
        "location": [
            "C5",
        ]
    },
    {
        "substance": "Di9",
        "amount": 109,
        "plate": 4,
        "location": [
            "E1",
        ]
    },
    {
        "substance": "Di9",
        "amount": 109,
        "plate": 4,
        "location": [
            "F5",
        ]
    },
    {
        "substance": "Di10",
        "amount": 105,
        "plate": 4,
        "location": [
            "B2",
        ]
    },
    {
        "substance": "Di10",
        "amount": 105,
        "plate": 4,
        "location": [
            "C6",
        ]
    },
    {
        "substance": "Di10",
        "amount": 105,
        "plate": 4,
        "location": [
            "E2",
        ]
    },
    {
        "substance": "Di10",
        "amount": 105,
        "plate": 4,
        "location": [
            "F6",
        ]
    },
    {
        "substance": "Di14",
        "amount": 147,
        "plate": 4,
        "location": [
            "B3",
        ]
    },
    {
        "substance": "Di14",
        "amount": 147,
        "plate": 4,
        "location": [
            "C7",
        ]
    },
    {
        "substance": "Di14",
        "amount": 147,
        "plate": 4,
        "location": [
            "E3",
        ]
    },
    {
        "substance": "Di14",
        "amount": 147,
        "plate": 4,
        "location": [
            "F7",
        ]
    },
    {
        "substance": "Di15",
        "amount": 222,
        "plate": 4,
        "location": [
            "B4",
        ]
    },
    {
        "substance": "Di15",
        "amount": 222,
        "plate": 4,
        "location": [
            "C8",
        ]
    },
    {
        "substance": "Di15",
        "amount": 222,
        "plate": 4,
        "location": [
            "E4",
        ]
    },
    {
        "substance": "Di15",
        "amount": 222,
        "plate": 4,
        "location": [
            "F8",
        ]
    },
    {
        "substance": "Chloroform",
        "location": [
            "A1"
        ],
        "amount": 690,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A2"
        ],
        "amount": 640,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A3"
        ],
        "amount": 640,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A4"
        ],
        "amount": 690,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A5"
        ],
        "amount": 640,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A6"
        ],
        "amount": 630,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A7"
        ],
        "amount": 610,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "A8"
        ],
        "amount": 610,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B1"
        ],
        "amount": 690,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B2"
        ],
        "amount": 690,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B3"
        ],
        "amount": 650,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B4"
        ],
        "amount": 570,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B5"
        ],
        "amount": 650,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B6"
        ],
        "amount": 590,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B7"
        ],
        "amount": 600,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "B8"
        ],
        "amount": 650,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C1"
        ],
        "amount": 590,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C2"
        ],
        "amount": 590,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C3"
        ],
        "amount": 570,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C4"
        ],
        "amount": 570,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C5"
        ],
        "amount": 640,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C6"
        ],
        "amount": 650,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C7"
        ],
        "amount": 610,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "C8"
        ],
        "amount": 530,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D1"
        ],
        "amount": 740,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D2"
        ],
        "amount": 680,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D3"
        ],
        "amount": 690,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D4"
        ],
        "amount": 740,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D5"
        ],
        "amount": 680,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D6"
        ],
        "amount": 680,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D7"
        ],
        "amount": 660,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "D8"
        ],
        "amount": 660,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E1"
        ],
        "amount": 730,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E2"
        ],
        "amount": 740,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E3"
        ],
        "amount": 700,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E4"
        ],
        "amount": 620,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E5"
        ],
        "amount": 700,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E6"
        ],
        "amount": 640,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E7"
        ],
        "amount": 650,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "E8"
        ],
        "amount": 700,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F1"
        ],
        "amount": 640,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F2"
        ],
        "amount": 640,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F3"
        ],
        "amount": 620,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F4"
        ],
        "amount": 620,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F5"
        ],
        "amount": 690,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F6"
        ],
        "amount": 700,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F7"
        ],
        "amount": 650,
        "plate": "4"
    },
    {
        "substance": "Chloroform",
        "location": [
            "F8"
        ],
        "amount": 580,
        "plate": "4"
    }
]

substance_locations = {
    "3": {
        "name": "Stock",
        "type": "analyticalsales_24_wellplate_80000ul",
        "A1": {
            "substance": "TriG",
            "amount": 3000
        },
        "A2": {
            "substance": "TriJ",
            "amount": 3000
        },
        "A3": {
            "substance": "TriB",
            "amount": 5000
        },
        "A4": {
            "substance": "TriC",
            "amount": 5000
        },
        "A5": {
            "substance": "Di1",
            "amount": 3000
        },
        "A6": {
            "substance": "Di2",
            "amount": 3000
        },
        "B1": {
            "substance": "Di3",
            "amount": 3000
        },
        "B2": {
            "substance": "Di4",
            "amount": 3000
        },
        "B3": {
            "substance": "Di5",
            "amount": 3000
        },
        "B4": {
            "substance": "Di6",
            "amount": 3000
        },
        "B5": {
            "substance": "Di7",
            "amount": 3000
        },
        "B6": {
            "substance": "Di8",
            "amount": 3000
        },
        "C1": {
            "substance": "Di9",
            "amount": 3000
        },
        "C2": {
            "substance": "Di10",
            "amount": 3000
        },
        "C3": {
            "substance": "Di14",
            "amount": 3000
        },
        "C4": {
            "substance": "Di15",
            "amount": 3000
        }
    },
    "5": {
        "name": "Solvent",
        "type": "fisher_6_wellplate_25000ul",
        "A1": {
            "substance": "Chloroform",
            "amount": 25000
        },
        "A2": {
            "substance":"Chloroform",
            "amount": 25000
        }
        }
}

class Opentrons:
    def __init__(
        self,
        protocol: protocol_api.ProtocolContext,
        deck_info: dict,
    ):
        """
        Initialise the Opentrons object.

        Parameters
        ----------
        protocol : protocol_api.ProtocolContext
            The protocol context for the current protocol.
        deck_info : dict
            Dictionary of deck information.
            Contains information of substances and their quantities on the deck.

        Returns
        -------
        None
        """
        # Set gantry speeds
        self.protocol = protocol
        self.protocol.max_speeds["X"] = 220
        self.protocol.max_speeds["Y"] = 220
        self.protocol.max_speeds["Z"] = 220

        # TODO: Add dynamic loading of labware
        # self.tiprack1000 = self.protocol.load_labware(
        #     "opentrons_96_tiprack_1000ul", 1
        # )
        self.tiprack300 = self.protocol.load_labware(
            "opentrons_96_tiprack_300ul", 2
        )
        self.plate = self.protocol.load_labware(
            "analyticalsales_48_wellplate_2000ul", 4
        )
        self.labware = {}
        self.labware[4] = self.plate
        # self.labware[1] = self.tiprack1000
        self.labware[2] = self.tiprack300
        # Add substances to the deck
        for deck_number in deck_info:
            self.labware[int(deck_number)] = self.protocol.load_labware(
                deck_info[deck_number]["type"], int(deck_number)
            )
        # Delete name and type from deck_info
        for deck_number in deck_info:
            del deck_info[deck_number]["type"]
            del deck_info[deck_number]["name"]
        # Loading pipettes
        # self.right_pipette = self.protocol.load_instrument(
            # "p1000_single_gen2", "right", tip_racks=[self.tiprack1000]
        # )
        self.left_pipette = protocol.load_instrument(
            "p300_single_gen2", "left", tip_racks=[self.tiprack300]
        )
        # self.right_pipette.flow_rate.aspirate = 40
        # self.right_pipette.flow_rate.dispense = 40
        self.left_pipette.flow_rate.aspirate = 60
        self.left_pipette.flow_rate.dispense = 60
        self.left_pipette.swelled = False
        # self.right_pipette.swelled = False
        # For tracking substance amounts
        self.substances = defaultdict(list)
        for position in deck_info:
            position_int = int(position)
            for well_plate in deck_info[position]:
                substance_position = self.labware[position_int][well_plate]
                substance = deck_info[position][well_plate]
                substance_name = substance["substance"]
                amount = substance["amount"]
                self.substances[substance_name].append(
                    {
                        "position": substance_position,
                        "amount": amount,
                    }
                )

    def swell_tip(self, pipette, position):
        """
        Swells the tip in the `stock` labware location at a specified location.

        Notes
        -----
        Perform before a pipette is used for transfer.

        Parameters
        ----------
        pipette : pipette
            The pipette to be used.

        position:
            Position to swell the tip in.

        Returns
        -------
        None

        """
        for i in range(1):
            pipette.aspirate(100, position)
            self.protocol.delay(10)
            pipette.move_to(position.top())
            pipette.dispense(100, location=position)
        pipette.swelled = True

    def move_without_drip(self, position_to, position_from, pipette, amount):
        """
        Transfers substance from one location to another without dripping (hopefully).

        Notes
        -----
        Ideally, the swell function will be used before this function is called to reduce the
        probability of drips.

        Parameters
        ----------
        position_to: position
            Location of the target well plates to move substance to.
        position_from: position
            Location of the source well plates to move substance from.
        amount: float or int
            Amount of substance to be moved. (in uL)


        Returns
        -------
        None

        """
        # Check if pipette swelled before movement
        pipette.aspirate(amount, position_from)
        pipette.air_gap(15)
        pipette.dispense(location=position_to.top(z=2))

    def move_substance(self, amount, substance_name, position_to, pipette):
        """
        Moves a specified amount of substance from one location to another.

        Parameters
        ----------
        amount : float or int
            Amount of substance to be moved. (in mL)
        substance_name : str
            Name of the substance to be moved.
        position_to: position
            Location of the target well plates to move substance to.
        pipette: pipette
            The pipette to be used.
        value:

        Returns
        -------
        None

        """
        # Find the deck location of the substance
        try:
            substance_position = self.substances[substance_name][0]["position"]
        except:
            pprint(self.substances)
            print(f"Substance {substance_name} not found.")
            raise RuntimeError(
                f"Substance not found in deck. This could be due to the deck being empty, or the amount of {substance_name} needed exceeding the amount placed on the deck."
            )

        # Perform swelling
        if pipette.swelled != substance_name:
            self.swell_tip(
                pipette=pipette,
                position=substance_position,
            )
            pipette.swelled = substance_name
            # Check to see if amount of substance is greater than the amount on the deck
        minimum_volume = 400
        if amount > (
            self.substances[substance_name][0]["amount"] - minimum_volume
        ):
            print(
                f"Amount of {substance_name} needed is greater than the amount on the deck.\n"
                f"Trying again to move after changing the well plate to movw from of {substance_name}."
            )
            # Change the well plate to move from
            self.substances[substance_name].pop(0)
            if len(self.substances[substance_name]) == 0:
                raise RuntimeError(
                    f"No more {substance_name} left on the deck. Please check the deck and try again."
                )
            self.move_substance(
                amount=amount,
                substance_name=substance_name,
                position_to=position_to,
                pipette=pipette,
            )

        assert pipette.swelled == substance_name
        # Get amount left on deck
        # amount_left = self.substances[substance_name][0]["amount"]
        # Change well bottom clearance to prevent pipette touching the solvent
        # aspirate_loc = substance_position.bottom()
        # aspirate_loc = aspirate_loc.move(
        #     Point(0, 0, -aspirate_loc.point.z + 1)
        # )
        self.move_without_drip(
            pipette=pipette,
            position_to=position_to,
            position_from=substance_position,
            amount=amount,
        )
        self.substances[substance_name][0]["amount"] -= amount


def run(protocol: protocol_api.ProtocolContext):
    """
    Run the protocol.
    """

    amount_added = defaultdict(lambda: 0)
    substance_path = substance_locations
    move_path = move_commands
    # Check if root in the directory
    #if not substance_path.is_file():
    #    substance_path = Path("/root/Opentrons_Code/AB-02-007/Plate2/substance_locations.json")
    #    move_path = Path("/root/Opentrons_Code/AB-02-007/Plate2/move_commands.json")

    #with open(str(substance_path)) as f:
    #    deck_info = json.load(f)
    ot = Opentrons(protocol=protocol, deck_info=substance_locations)

    #with open(str(move_path)) as f:
    #    move_info = json.load(f)

    # Extract list of moves from the move information
    moves = []
    for substance in move_commands:
        for location in substance["location"]:
            moves.append(
                {
                    "substance": substance["substance"],
                    "location": location,
                    "amount": substance["amount"],
                    "plate": substance["plate"],
                }
            )
    added_substances = []
    positions_added = defaultdict(str)
    pipette_max_volume = 220
    for move in moves:
        location = move["location"]
        amount = int(move["amount"])
        plate = int(move["plate"])
        substance = move["substance"]
        # Get target well location
        target_well = ot.labware[plate].wells(location)[0]
        # Add the first substance to the list
        num_moves = amount // pipette_max_volume
        added = 0
        if len(added_substances) == 0:
            ot.left_pipette.pick_up_tip()
            added_substances.append(substance)
        # Check if substance matches the last substance added
        elif substance != added_substances[-1]:
            # Get a new tip
            ot.left_pipette.drop_tip()
            ot.left_pipette.pick_up_tip()
            added_substances.append(substance)
        for i in range(num_moves + 1):
            # Check if move is the last move
            if i == num_moves:
                amount_to_add = amount - added
            else:
                amount_to_add = pipette_max_volume
            if amount_to_add == 0:
                continue
            ot.move_substance(
                amount=amount_to_add,
                substance_name=substance,
                position_to=target_well,
                pipette=ot.left_pipette,
            )
            added += amount_to_add
            amount_added[location] += amount_to_add
        positions_added[location] += substance + " "
    for line in protocol.commands():
        continue
    pprint(amount_added)
    pprint(positions_added)
