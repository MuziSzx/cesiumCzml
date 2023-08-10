import tle2czml

tles = '''空天碳卫星1号     
1 57403U 23101E   23205.44931032  .11573785  33140-5  35289-3 0  9997
2 57403  97.4277 267.4631 0110398  26.4714 344.0415 16.25783297   687'''
czml = tle2czml.tles_to_czml(tles)
print(czml)
fo = open("test.czml", "w")
fo.write(czml)
fo.close()
