import numpy as numpy
import pandas as pandas
from typing import *

TYPES = ['NORMAL', 'FIRE', 'WATER', 'ELECTRIC', 'GRASS', 'ICE', 'FIGHTING', 'POISON', 'GROUND', 'FLYING', 'PSYCHIC', 'BUG', 'ROCK', 'GHOST', 'DRAGON', 'DARK', 'STEEL', 'FAIRY']
TOTAL_TYPES = len(TYPES)
NORMAL, FIRE, WATER, ELECTRIC, GRASS, ICE, FIGHTING, POISON, GROUND, FLYING, PSYCHIC, BUG, ROCK, GHOST, DRAGON, DARK, STEEL, FAIRY = range(TOTAL_TYPES)

STRONG = 2
WEAK = 1/2
IMMUNE = 0

def set_chart_values (att:int, value:int, *args: List[int]):
    """
    set type chart table values
    att (int): attacking type
    value (int): effectiveness
    *args (list): list of types is effective/weak against
    """
    for opp in args:
      type_chart[att][opp] = value  

def print_chart():
    
    global type_chart, TYPES
    
    data_frame = pandas.DataFrame(type_chart, columns=TYPES, index=TYPES)
    # data_frame = data_frame.astype(int) # Remove ".0"

    print(data_frame)


#create type chart table
type_chart = numpy.ones(( TOTAL_TYPES, TOTAL_TYPES )) 

#NORMAL
set_chart_values(NORMAL, WEAK, [ROCK, STEEL])
set_chart_values(NORMAL, IMMUNE, [GHOST])

#FIRE
set_chart_values(FIRE, WEAK, [FIRE, WATER, ROCK, DRAGON])
set_chart_values(FIRE, STRONG, [GRASS, ICE, BUG, STEEL])

#WATER
set_chart_values(WATER, WEAK, [WATER, GRASS, DRAGON])
set_chart_values(WATER, STRONG, [FIRE, GROUND, ROCK])

#ELECTRIC
set_chart_values(ELECTRIC, WEAK, [ELECTRIC, GRASS, DRAGON])
set_chart_values(ELECTRIC, STRONG, [WATER, FLYING])
set_chart_values(ELECTRIC, IMMUNE, [GROUND])

#GRASS
set_chart_values(GRASS, WEAK, [FIRE, GRASS, POISON, FLYING, BUG, DRAGON, STEEL])
set_chart_values(GRASS, STRONG, [WATER, GROUND, ROCK])

#ICE
set_chart_values(ICE, WEAK, [FIRE, WATER, ICE, STEEL])
set_chart_values(ICE, STRONG, [GRASS, GROUND, FLYING, DRAGON])
#set_chart_values(ICE, STRONG, [GRASS, GROUND, FLYING, DRAGON, WATER]) # Freeze-Dry

#FIGHTING
set_chart_values(FIGHTING, WEAK, [POISON, FLYING, PSYCHIC, BUG, FAIRY])
set_chart_values(FIGHTING, STRONG, [NORMAL, ICE, ROCK, DARK, STEEL])
set_chart_values(FIGHTING, IMMUNE, [GHOST])

#POISON
set_chart_values(POISON, WEAK, [POISON, GROUND, ROCK, GHOST])
set_chart_values(POISON, STRONG, [GRASS, FAIRY])
set_chart_values(POISON, IMMUNE, [STEEL])

#GROUND
set_chart_values(GROUND, WEAK, [GRASS, BUG])
set_chart_values(GROUND, STRONG, [FIRE, ELECTRIC, POISON, ROCK, STEEL])
set_chart_values(GROUND, IMMUNE, [FLYING])

#FLYING
set_chart_values(FLYING, WEAK, [ELECTRIC, ROCK, STEEL])
set_chart_values(FLYING, STRONG, [GRASS, FIGHTING, BUG])

#PSYCHIC
set_chart_values(PSYCHIC, WEAK, [PSYCHIC, STEEL])
set_chart_values(PSYCHIC, STRONG, [FIGHTING, POISON])
set_chart_values(PSYCHIC, IMMUNE, [DARK])

#BUG
set_chart_values(BUG, WEAK, [FIRE, FIGHTING, POISON, FLYING, GHOST, STEEL, FAIRY])
set_chart_values(BUG, STRONG, [GRASS, PSYCHIC, DARK])

#ROCK
set_chart_values(ROCK, WEAK, [FIGHTING, GROUND, STEEL])
set_chart_values(ROCK, STRONG, [FIRE, ICE, FLYING, BUG])

#GHOST
set_chart_values(GHOST, WEAK, [DARK])
set_chart_values(GHOST, STRONG, [PSYCHIC, GHOST])
set_chart_values(GHOST, IMMUNE, [NORMAL])

#DRAGON
set_chart_values(DRAGON, WEAK, [STEEL])
set_chart_values(DRAGON, STRONG, [DRAGON])
set_chart_values(DRAGON, IMMUNE, [FAIRY])

#DARK
set_chart_values(DARK, WEAK, [FIGHTING, DARK, FAIRY])
set_chart_values(DARK, STRONG, [PSYCHIC, GHOST])

#STEEL
set_chart_values(STEEL, WEAK, [FIRE, WATER, ELECTRIC, STEEL])
set_chart_values(STEEL, STRONG, [ICE, ROCK, FAIRY])

#FAIRY
set_chart_values(FAIRY, WEAK, [FIRE, POISON, STEEL])
set_chart_values(FAIRY, STRONG, [FIGHTING, DRAGON, DARK])
