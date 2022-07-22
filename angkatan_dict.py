angkatan = {
    #Fill it with your faculty batch
    "Fasilkom": {
            "180" : "Quanta",
            "190" : "Maung",
            "200" : "Chronos",
            "210" : "Bakung",
    },
}


def get_angkatan(faculty, num):
    return angkatan[faculty][num]
