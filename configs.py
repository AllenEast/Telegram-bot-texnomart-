CATEGORIES = {
    'Iphone': 'katalog/smartfony-apple/',
    'Notebook': 'katalog/vse-noutbuki/',
    'Tv': 'katalog/televizory-toshiba/',
    'Kondisioner': 'katalog/vse-kondicionery-5/',
    'Pilesos': 'katalog/vse-pylesosy/',
    'Radar': 'katalog/radar-detektor-neoline/'
}


def get_value(category):
    for k, v in CATEGORIES.items():
        if k == category:
            return v
