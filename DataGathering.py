#!/usr/bin/env python



print('Importieren der verwendeten Libraries ... ', end='', flush=True)
import sys
import urllib.request
import io
import pandas
print('OK')



# Quelle der Rohdaten
print('Initialisierung ... ', end='', flush=True)
link_to_database = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?&table=compositepars'

# Auswahl an Attributen aus dem Rohdatensatz
column_selection_benjamin = ['fpl_hostname', 'fst_optmag', 'fst_nirmag', 'fst_spt', 'fst_teff', 'fst_logg', 'fst_lum', 'fst_mass', 'fst_rad', 'fst_met', 'fst_age']
column_selection_philip = ['fpl_name', 'fpl_controvflag', 'fpl_letter', 'fpl_bmasse', 'fpl_rade', 'fpl_orbper', 'fpl_smax', 'fpl_eccen', 'fpl_hostname', 'fpl_cbflag', 'fst_mass', 'fst_rad', 'fst_teff', 'fst_age']
column_selection = set(column_selection_benjamin + column_selection_philip)

# Umbenennung der Attribute im Rohdatensatz
column_renaming = {
  'fpl_name': 'planet_name',
  'fpl_controvflag': 'controversial_flag',
  'fpl_letter': 'planet_letter',
  'fpl_bmasse': 'planet_mass',
  'fpl_rade': 'planet_radius',
  'fpl_orbper': 'orbital_period',
  'fpl_smax': 'orbital_radius',
  'fpl_eccen': 'eccentricity',
  'fpl_hostname': 'host_name',
  'fpl_cbflag': 'binary_flag',
  'fst_mass': 'stellar_mass',
  'fst_rad': 'stellar_radius',
  'fst_teff': 'stellar_temperature',
  'fst_age': 'stellar_age',
  'fst_optmag': 'optical_magnitude',
  'fst_nirmag': 'near_ir_magnitude',
  'fst_spt': 'spectral_type',
  'fst_logg': 'stellar_surface_gravity',
  'fst_lum': 'stellar_luminosity',
  'fst_met': 'stellar_metallicity'
}
print('OK')



# Download der Rohdaten
print('Download der Daten ... ', end='', flush=True)
try:
    raw_data = urllib.request.urlopen(link_to_database).read()
except:
    print()
    print('Error: Die Daten konnten nicht heruntergeladen werden')
    print()
    sys.exit(1)
print('OK')

# Beschränken der Rohdaten auf die ausgewählten Attribute
print('Bearbeiten der Daten ... ', end='', flush=True)
try:
    data = pandas.read_csv(io.StringIO(str(raw_data,'utf-8')))
except:
    print()
    print('Error: Die heruntergeladenen Daten konnten nicht korrekt gelesen werden')
    print()
    sys.exit(1)
data = data.drop(set(data.columns) - column_selection, axis=1)

# Umbenennung der Attribute
data = data.rename(columns=column_renaming)
print('OK')

#Speichern der Daten als CSV
print('Speichern der Daten ... ', end='', flush=True)
try:
    data.to_csv('data/Data.csv', index=False, mode='w+')
except FileNotFoundError:
    print()
    print('Error: Schreiben der Daten als CSV fehlgeschlagen (möglicherweise existiert das Verzeichnis "data" nicht)')
    print()
    sys.exit(1)
print('OK')

sys.exit(0)
