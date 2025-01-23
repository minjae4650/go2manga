image die_ending = im.Scale("images/endings/die_ending.png", 1500, 1080)


define agasa = Character('아가사 박사님', color="#6D5E7D")


label die_ending:
    scene black
    show die_ending with dissolve
    agasa "역시 애들만 보내기엔 너무 위험했나..."
    pause 2.0
    return