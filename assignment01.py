profile = {} #create empty dict profile
profile['NAME'] = {'first':'Mildred','middle':'D.','last':'Robertson'}
profile['ADDRESS'] = {'street':'438 Redbud Drive', 'city':'New York', 'state':'NY', 'zipcode':'10011'} # append key,value
profile['Mother\'s maiden name']='McBride'
profile['SSN'] = '113-38-XXXX'
profile['Geo coordinates'] = (40.679748, -74.076426) # tuple
profile['PHONE'] = {'home':('+1','347-683-3961'),'work':('+1','347-683-3961')}
profile['BIRTHDAY'] = {'birthday':('09','13','1963'),'age':'54','zodiac':'Virgo'}
profile['ONLINE'] = {
        'email':'MildredDRobertson@armyspy.com',\
        'username':'Obtainted','password':'Tha3uiy5aegh',\
        'website':'sanrioworld.com'}
profile['FINANCE'] = {'visa':'4539967677526065','exp':'062021','cvv2':'735'}
profile['EMPLOYMENT'] = {'company':'Total Yard Management', 'occupation':'Electrical power line installer'}
profile['PHYSICAL CHARACTERISTICS'] = {'height':('5\' 6"','167 cm'), 'weight':('213.6 pounds','97.1 kg'), 'blood type':'0+'}
profile['TRACKING NUMBERS'] = {\
        'UPS tracking number':'1Z 85W 247 00 1102 229 8', \
        'Western Union MTCN':'1387471482', \
        'MoneyGram MTCN':'56949852'}
profile['OTHER'] = {'Favorite color':'Purple','Vehicle':'2000 Holden HRT','GUID':'78d4c7c6-5d4d-497e-8cb1-1448534f79a9'}

from pprint import pprint

pprint(profile)
