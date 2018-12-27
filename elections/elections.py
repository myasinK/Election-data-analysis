
from open_fec_data import *
import pandas as pd
import numpy as np
import json


presidential_election_2016 = pd.read_excel('C:\\Users\\Yasin\\elections\\elections\\federalelections2016.xlsx', None ) # 'None' to get all sheets

all_sheets = list( presidential_election_2016 )

pres_general = presidential_election_2016[ all_sheets[8] ]

column_names = pres_general.columns

nd_array_pres_data = pres_general.values

number_of_rows = len( nd_array_pres_data )

total_rows = number_of_rows + 1 # plus header row

#fec_id = list( nd_array_pres_data[ :, 1 ] ) 
#state = list( nd_array_pres_data[ :, 2 ] )
#state_abbr = list( nd_array_pres_data[ :, 3 ] )
#candidate_name = list( nd_array_pres_data[ :, 6 ] )
#affiliation = list( nd_array_pres_data[ :, 9 ] ) 
#votes_for_candidate = list( nd_array_pres_data[ :, 10 ] ) 
#general_pc = list( nd_array_pres_data[ :, 12 ] * 100 ) 
#winner = list( nd_array_pres_data[ :, 13 ] )

# Drop columns so that 
# 1st col is FEC ID
# 2nd col is state name
# 3rd col is state abbreviation
# 4th col is candidate last-name
# 5th col is party affiliation
# 6th col is votes for candidate
# 7th col is vote percentage in that state
# 8th col is winner indicator
pres_general_2016 = np.delete( nd_array_pres_data, [ 0, 4, 5, 7, 8, 11  ], 1 )    

#pres_2016_json = {}
pres_2016_json = pres_general_2016.tolist()

json_path = 'C:\\Users\\Yasin\\elections\\elections\\pres-general-2016.txt'

with open(json_path, 'w') as json_file:
    json.dump( pres_2016_json, json_file )