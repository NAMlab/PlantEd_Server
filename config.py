import math

summer = {"Min_T" : 15,
          "Max_T" : 30,
          "shift" : 10,
          "skew" : 3.2}

winter = {"Min_T" : -5,
          "Max_T" : 10,
          "shift" : 10,
          "skew" : 3.2}

# HUMIDITY
humidity = {"Min_T" : 0.4,
          "Max_T" : 1,
          "shift" : -20.8,
          "skew" : 3.2}

water_concentration_at_temp = [0.269,0.288,0.309,0.33,0.353,0.378,0.403,0.431,0.459,0.49,0.522,0.556,0.592,
                               0.63,0.67,0.713,0.757,0.804,0.854,0.906,0.961,1.018,1.079,1.143,
                               1.21,1.28,1.354,1.432,1.513,1.598,1.687,1.781,1.879,1.981,2.089,2.201,2.318,2.441,2.569,2.703]

# provide season and x in hours to get temp or humidity
def get_y(x,dict):
    M = (dict["Min_T"] + dict["Max_T"]) / 2  # mean
    A = (dict["Max_T"] - dict["Min_T"]) / 2  # amplitude
    F = (2 * math.pi) / 24  # based on a 25 hour cycle
    P = dict["shift"]# shift
    d = dict["skew"]# skewness
    temp = M + A * math.sin(F*((x-P)+d*(math.sin(F*(x-P))/2)))
    #print(temp)
    return temp