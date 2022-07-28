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
        "01": ['Reguler', 'Ilmu Komputer', 'FASILKOM', 'S1'],
        "02": ['Kls Internasional', 'Ilmu Komputer', 'FASILKOM', 'S1'],
        "06": ['Reguler', 'Sistem Informasi', 'FASILKOM', 'S1'],
        "07": ['Ekstensi', 'Sistem Informasi', 'FASILKOM', 'S1'],
        "08": ['Paralel', 'Sistem Informasi', 'FASILKOM', 'S1'],
        "09": ['Paralel', 'Ilmu Komputer', 'FASILKOM', 'S1'],
    },
    "00.05.01":{
        #FH Ilmu Hukum
        "01": ['Reguler', 'Ilmu Hukum', 'FH', 'S1'],
        "02": ['Ekstensi', 'Ilmu Hukum', 'FH', 'S1'],
        "06": ['Paralel', 'Ilmu Hukum', 'FH', 'S1'],
        "07": ['Kls Internasional', 'Ilmu Hukum', 'FH', 'S1'],
    },
    "02.04.01":{
        #FT Teknik Mesin
        "01": ['Reguler', 'Teknik Mesin', 'FT', 'S1'],
        "03": ['Ekstensi', 'Teknik Mesin', 'FT', 'S1'],
        "04": ['Kls Internasional', 'Teknik Mesin', 'FT', 'S1'],
        "07": ['Paralel', 'Teknik Mesin', 'FT', 'S1'],
    }, 
    "02.03.01":{
        #FMIPA Fisika/Geofisika
        "02": ['Reguler', 'Fisika', 'FMIPA', 'S1'],
        "03": ['Ekstensi', 'Fisika', 'FMIPA', 'S1'],
        "05": ['Paralel', 'Fisika', 'FMIPA', 'S1'],
        "06": ['Reguler', 'Geofisika', 'FMIPA', 'S1'],
        "09": ['Paralel', 'Geofisika', 'FMIPA', 'S1'],
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

