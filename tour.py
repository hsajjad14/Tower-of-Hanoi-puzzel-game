
"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2018.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "__main__":'

import time
from toah_model import TOAHModel
import math

def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    @rtype: None
    """
    if model.get_number_of_stools()== 3:
        anne_hoy_three_stools(model,model.get_number_of_cheeses(),0,1,2,animate,delay_btw_moves)
    else:
        anne_hoy_four_stools(model,model.get_number_of_cheeses(),0,1,2,3,animate,delay_btw_moves)

def anne_hoy_four_stools(model, n, from_stool,spare_stool1, spare_stool2, to_stool,animate,delay_btw_moves):
    '''
    '''
    i = finding_i(n)
    k = n-i
    if n <= 2:
        anne_hoy_three_stools(model, n, from_stool, spare_stool1, to_stool, animate,delay_btw_moves)
    else:
        anne_hoy_four_stools(model, i, from_stool, to_stool, spare_stool2, spare_stool1,animate,delay_btw_moves)
        anne_hoy_three_stools(model, k, from_stool, spare_stool2, to_stool,animate,delay_btw_moves)
        anne_hoy_four_stools(model, i, spare_stool1, from_stool, spare_stool2, to_stool,animate,delay_btw_moves)

def anne_hoy_three_stools(model,n, from_stool, spare_stool , to_stool,animate, delay_btw_moves):
    '''
    '''
    # Credit to Larry Zhang
    # This is a modification of Larry Zhang's def hanoi_stack()
    if n == 1:
        model.move(from_stool, to_stool)
        if animate == True:
            print(model)
            time.sleep(delay_btw_moves)
    else:
        anne_hoy_three_stools(model,n-1, from_stool, to_stool, spare_stool,animate, delay_btw_moves)
        anne_hoy_three_stools(model,1, from_stool, spare_stool, to_stool, animate, delay_btw_moves)
        anne_hoy_three_stools(model,n-1, spare_stool, from_stool, to_stool, animate, delay_btw_moves)



        
    
def finding_i(n):
    l = []
    for j in range(1,n):
        l.append(j)
    middle = 0
    
          
    if len(l) % 2 == 0:
        middle = int((len(l)+1)/2)
    else:
        if len(l) > 3:
            middle = (len(l))//2
        
        else:
            middle = (len(l)-1)//2
                 
    if len(l) > 8:
        dec = int(n*0.2)
        middle = l[dec]
        
    if len(l) > 0:
        i = n - l[int(middle)]
    if len(l) <= 0:
        i = 0
    
        
    return i
        
        
if __name__ == '__main__':
    num_cheeses = 15
    delay_between_moves = 0.5
    console_animate = True

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())
