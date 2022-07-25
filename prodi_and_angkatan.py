angkatan = {
    #Fill it with your faculty batch
    "S1":{
        "FASILKOM": {
                "180" : "Quanta",
                "190" : "Maung",
                "200" : "Chronos",
                "210" : "Bakung",
        },
    }
}

prodi = {
    "00.12.01":{
        #FASILKOM
        "01": ['Reguler', 'S1 Ilmu Komputer', 'FASILKOM', 'S1'],
        "02": ['Kls Internasional', 'S1 Ilmu Komputer', 'FASILKOM', 'S1'],
        "06": ['Reguler', 'S1 Sistem Informasi', 'FASILKOM', 'S1'],
        "07": ['Ekstensi', 'S1 Sistem Informasi', 'FASILKOM', 'S1'],
        "08": ['Paralel', 'S1 Sistem Informasi', 'FASILKOM', 'S1'],
        "09": ['Paralel', 'S1 Ilmu Komputer', 'FASILKOM', 'S1'],
    },
    "00.05.01":{
        #FH Ilmu Hukum
        "01": ['Reguler', 'S1 Ilmu Hukum', 'FH', 'S1'],
        "02": ['Ekstensi', 'S1 Ilmu Hukum', 'FH', 'S1'],
        "06": ['Paralel', 'S1 Ilmu Hukum', 'FH', 'S1'],
        "07": ['Kls Internasional', 'S1 Ilmu Hukum', 'FH', 'S1'],
    },
    "02.04.01":{
        #FT Teknik Mesin
        "01": ['Reguler', 'S1 Teknik Mesin', 'FT', 'S1'],
        "03": ['Ekstensi', 'S1 Teknik Mesin', 'FT', 'S1'],
        "04": ['Kls Internasional', 'S1 Teknik Mesin', 'FT', 'S1'],
        "07": ['Paralel', 'S1 Teknik Mesin', 'FT', 'S1'],
    }, 
    "02.03.01":{
        #FMIPA Fisika/Geofisika
        "02": ['Reguler', 'S1 Fisika', 'FMIPA', 'S1'],
        "03": ['Ekstensi', 'S1 Fisika', 'FMIPA', 'S1'],
        "05": ['Paralel', 'S1 Fisika', 'FMIPA', 'S1'],
        "06": ['Reguler', 'S1 Geofisika', 'FMIPA', 'S1'],
        "09": ['Paralel', 'S1 Geofisika', 'FMIPA', 'S1'],
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

