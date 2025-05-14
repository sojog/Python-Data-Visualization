


# //dontpad.com/suprafete

suprafete = {
    'Bangladesh': 147570,
    'Brazilia': 8515770,
    'China': 9562910,
    'India': 3287263,
    'Indonezia': 1904569,
    'Mexic': 1972550,
    'Nigeria': 923768,
    'Pakistan': 881913,
    'Rusia': 17098242,
    'Statele Unite': 9831510
}



from pprint import pprint

countries = ['Bangladesh', 'Brazil', 'China', 'India', 'Indonesia', 'Mexico', 'Nigeria', 'Pakistan', 'Russia', 'United States']
population =  [170, 213, 1411, 1378, 271, 126, 211, 225, 146, 331]


populatii = { tara:population[index] for index, tara in enumerate(countries) }
pprint(populatii)


{
 'Bangladesh': 170,
 'Brazil': 213,
 'China': 1411,
 'India': 1378,
 'Indonesia': 271,
 'Mexico': 126,
 'Nigeria': 211,
 'Pakistan': 225,
 'Russia': 146,
 'United States': 331
}