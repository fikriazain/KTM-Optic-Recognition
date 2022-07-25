angkatan = {
    #Fill it with your faculty batch
    "S1":{
        "Fasilkom": {
                "180" : "Quanta",
                "190" : "Maung",
                "200" : "Chronos",
                "210" : "Bakung",
        },
    }
}

prodi = {
    "00.12.01":{
        "01": ['Reguler', 'S1 Ilmu Komputer', 'Fasilkom', 'S1'],
        "02": ['Kls Internasional', 'S1 Ilmu Komputer', 'Fasilkom', 'S1'],
        "06": ['Reguler', 'S1 Sistem Informasi', 'Fasilkom', 'S1'],
        "07": ['Ekstensi', 'S1 Sistem Informasi', 'Fasilkom', 'S1'],
        "08": ['Paralel', 'S1 Sistem Informasi', 'Fasilkom', 'S1'],
        "09": ['Paralel', 'S1 Ilmu Komputer', 'Fasilkom', 'S1'],
    }
}


def get_angkatan(faculty, num, jenjang):
    return angkatan[jenjang][faculty][num]

def get_faculty_detail(num):
    first = num[0:2]
    second = num[3:]
    studi = prodi[second]
    detail = studi[first]
    return detail

