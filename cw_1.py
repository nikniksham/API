def get_spn(toponym):
    poss = toponym['boundedBy']['Envelope']
    delta_x = str(list(map(float, poss['upperCorner'].split()))[0] - list(map(float, poss['lowerCorner'].split()))[0])
    delta_y = str(list(map(float, poss['upperCorner'].split()))[1] - list(map(float, poss['lowerCorner'].split()))[1])
    return delta_x, delta_y