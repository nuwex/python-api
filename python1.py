
#f = urllib2.urlopen('http://api.wunderground.com/api/39ed7af6b5218b93/geolookup/conditions/q/UK/Cedar_Rapids.json')
#http://api.wunderground.com/api/39ed7af6b5218b93/astronomy/q/CA/San_Francisco.json

import urllib2
import json

#var = the country
#var1 = the city
#var2 = first date
#var3 = second date

print "*If the country is not recognized- try again with full name of country and city.*"
var = raw_input("Please enter a country (eg. United Kingdom = UK,  South Korea = South_Korea, USA = NY,MA,NV,CA): ")
print "you entered", var

var1 = raw_input("Please enter a city (eg. London = London, New York City = New_York_City): ")
print "you entered", var1

s = 'http://api.wunderground.com/api/39ed7af6b5218b93/geolookup/conditions/q/' + var + '/' + var1 + '.json'
f = urllib2.urlopen(s)
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_c = parsed_json['current_observation']['temp_c']
temp_f = parsed_json['current_observation']['temp_f']
observation_time_rfc822 = parsed_json['current_observation']['observation_time_rfc822']
weather = parsed_json['current_observation']['weather']

relative_humidity = parsed_json['current_observation']['relative_humidity']
wind_string = parsed_json['current_observation']['wind_string']
wind_dir = parsed_json['current_observation']['wind_dir']
wind_degrees = parsed_json['current_observation']['wind_degrees']
wind_mph = parsed_json['current_observation']['wind_mph']
wind_gust_mph = parsed_json['current_observation']['wind_gust_mph']
wind_kph = parsed_json['current_observation']['wind_kph']
wind_gust_kph = parsed_json['current_observation']['wind_gust_kph']
pressure_mb = parsed_json['current_observation']['pressure_mb']
pressure_in = parsed_json['current_observation']['pressure_in']
pressure_trend = parsed_json['current_observation']['pressure_trend']
dewpoint_string = parsed_json['current_observation']['dewpoint_string']
dewpoint_f = parsed_json['current_observation']['dewpoint_f']
dewpoint_c = parsed_json['current_observation']['dewpoint_c']

icon = parsed_json['current_observation']['icon']
icon_url = parsed_json['current_observation']['icon_url']

print "\nCurrent temperature in %s is: %sC or %sF at %s" % (location, temp_c, temp_f, observation_time_rfc822)
print "The weather is %s" % (weather)

print "\n\nExtra Weather Information\n"
print "The relative humidity: %s" % (relative_humidity)
print "Wind: %s" % wind_string
print "Wind Direction: %s" % (wind_dir)
print "Wind Degrees: %s" % (wind_degrees)
print "Wind mph: %s" % (wind_mph)
print "Wind Gust mph: %s" % (wind_gust_mph)
print "Wind kph: %s" % (wind_kph)
print "Wind gust kph: %s" % (wind_gust_kph)
print "Pressure mb: %s" % (pressure_mb)
print "Pressure in: %s" % (pressure_in)
print "Pressure trend: %s" % (pressure_trend)
print "Dewpoint: %s" % (dewpoint_string)
print "Dewpoint (F): %s" % (dewpoint_f)
print "Dewpoint (C): %s" % (dewpoint_c)

print "Icon: %s" % (icon)
print "Icon URL: %s" % (icon_url)

f.close()





#second section

print "\n\nMore Moon and Sun information here\n"

t = 'http://api.wunderground.com/api/39ed7af6b5218b93/geolookup/astronomy/q/' + var + '/' + var1 + '.json'
g = urllib2.urlopen(t)
json_string = g.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']

print "\n\nMoon"
ageOfMoon = parsed_json['moon_phase']['ageOfMoon']
percentIlluminated = parsed_json['moon_phase']['percentIlluminated']
print "Age of Moon: %s" % (ageOfMoon)
print "Percentage of Illumination: %s" % (percentIlluminated) + "%"


print "\n\nSun"
sunriseH = parsed_json['moon_phase']['sunrise']['hour']
sunriseM = parsed_json['moon_phase']['sunrise']['minute']
sunsetH = parsed_json['moon_phase']['sunset']['hour']
sunsetM = parsed_json['moon_phase']['sunset']['minute']

print "Sunrise Time: %s:%s" % (sunriseH, sunriseM)
print "Sunset Time: %s:%s\n" % (sunsetH, sunsetM)
g.close()





#third section
#example URL - http://api.wunderground.com/api/Your_Key/planner_MMDDMMDD/q/CA/San_Francisco.json

print "If you want more information, about the Historical information between 2 dates in the year (max 30 days)"
print "Please enter the following information"
var2 = raw_input("Starting month and day (MMDD) ")
print "you entered", var2

var3 = raw_input("Ending month and day (MMDD) ")
print "you entered", var3

u = 'http://api.wunderground.com/api/39ed7af6b5218b93/planner_' + var2 + var3 + '/q/' + var + '/' + var1 + '.json'
h = urllib2.urlopen(u)
json_string = h.read()
parsed_json = json.loads(json_string)

#caused errors
#location = parsed_json['location']['city']

title = parsed_json['trip']['title']
#temp_highM is the temp_high Minimum in Celcius

temp_high_min = parsed_json['trip']['temp_high']['min']['C']
temp_high_avg = parsed_json['trip']['temp_high']['avg']['C']
temp_high_max = parsed_json['trip']['temp_high']['max']['C']

temp_low_min = parsed_json['trip']['temp_low']['min']['C']
temp_low_avg = parsed_json['trip']['temp_low']['avg']['C']
temp_low_max = parsed_json['trip']['temp_low']['max']['C']

chanceofpartlycloudyday = parsed_json['trip']['chance_of']['chanceofpartlycloudyday']['percentage']
chanceofsunnycloudyday = parsed_json['trip']['chance_of']['chanceofsunnycloudyday']['percentage']
chanceofcloudyday = parsed_json['trip']['chance_of']['chanceofcloudyday']['percentage']
chanceofwindyday = parsed_json['trip']['chance_of']['chanceofwindyday']['percentage']
chanceoffogday = parsed_json['trip']['chance_of']['chanceoffogday']['percentage']
chanceofhumidday = parsed_json['trip']['chance_of']['chanceofhumidday']['percentage']
chanceofprecip = parsed_json['trip']['chance_of']['chanceofhumidday']['percentage']
chanceofrainday = parsed_json['trip']['chance_of']['chanceofrainday']['percentage']
chanceofthunderday = parsed_json['trip']['chance_of']['chanceofthunderday']['percentage']
chanceofsnowonground = parsed_json['trip']['chance_of']['chanceofsnowonground']['percentage']
chanceoftornadoday = parsed_json['trip']['chance_of']['chanceoftornadoday']['percentage']
chanceofsultryday = parsed_json['trip']['chance_of']['chanceofsultryday']['percentage']
chanceofhailday = parsed_json['trip']['chance_of']['chanceofhailday']['percentage']
chanceofsnowday = parsed_json['trip']['chance_of']['chanceofsnowday']['percentage']
tempbelowfreezing = parsed_json['trip']['chance_of']['tempbelowfreezing']['percentage']
tempoverfreezing = parsed_json['trip']['chance_of']['tempoverfreezing']['percentage']

print "\nTitle: %s\n" % (title)
print "Highest Temperature (Min): %s" % (temp_high_min)
print "Highest Temperature (Avg): %s" % (temp_high_avg)
print "Highest Temperature (Max): %s" % (temp_high_min)
print "Lowest Temperature (Min) : %s" % (temp_low_min)
print "Lowest Temperature (Avg) : %s" % (temp_low_avg)
print "Lowest Temperature (Max) : %s" % (temp_low_max)

print "\nChance of Partly Cloudy : %s" % (chanceofpartlycloudyday) + "%"
print "Chance of Sunny Cloudy: %s" % (chanceofsunnycloudyday) + "%"
print "Chance of Cloudy: %s" % (chanceofcloudyday) + "%"
print "Chance of Sunny Windy: %s" % (chanceofwindyday) + "%"
print "Chance of Partly Fog: %s" % (chanceoffogday) + "%"
print "Chance of Humid: %s" % (chanceofhumidday) + "%"
print "Chance of Precipitation: %s" % (chanceofprecip) + "%"
print "Chance of Rain: %s" % (chanceofrainday) + "%"
print "Chance of Thunder: %s" % (chanceofthunderday) + "%"
print "Chance of Snow on Ground: %s" % (chanceofsnowonground) + "%"
print "Chance of Tornado: %s" % (chanceoftornadoday) + "%"
print "Chance of Sultry: %s" % (chanceofsultryday) + "%"
print "Chance of Hail: %s" % (chanceofhailday) + "%"
print "Chance of Snow: %s" % (chanceofsnowday) + "%"
print "Chance of Temperature below Freezing: %s" % (tempbelowfreezing) + "%"
print "Chance of Temperature above Freezing: %s" % (tempoverfreezing) + "%"


print "\n\nThank you for using my Weather API\n"
h.close()
