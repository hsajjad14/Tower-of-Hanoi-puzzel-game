"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""


# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
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


from toah_model import TOAHModel, IllegalMoveError


def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    try:
        model.move(origin, dest)
    except IllegalMoveError:
        print("\nyou cannot make this move!!\n")


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        
        if isinstance(number_of_cheeses, int) and isinstance(number_of_stools, int):
            self.number_of_cheeses = number_of_cheeses
            self.number_of_stools = number_of_stools
            self.model = TOAHModel(self.number_of_stools)
            self.model.fill_first_stool(self.number_of_cheeses)
            self.complete =  self.model._stools[0][:]
            
        else:
            print("Please enter a NUMBER of cheeses and a NUMBER of stools")
        
        
        
    

    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """
        
        flag = True
        player_input = ''
        orginial_stool = 0
        destination_stool = 0
        print("\nThis is how you play.\n\nEnter from which stool you want to move to and its destination\nas an ordered pair, i.e. (cheese stool location, stool I want to move to), (0,1) means \nI want to move the top cheese on stool 1 to top of stool 2.\nAnd you can only stack smaller cheese on larger cheese: enter quit anytime to exit the game \nother wise we will keep playing\n")     
        print()
        print("here is the model of the game")
        print(self.model)

        
        while flag:
            if self.complete == self.model._stools[self.number_of_stools-1]:
                print("\ncongratulations you won!!!\n")
                print("You completed the puzzel in "+ str(self.model.number_of_moves())+" moves")
                flag = False
            else:
                player_input = input("please enter the ordered pair of your movement: ")
                if player_input.lower() == 'quit':
                    print('goodbye')
                    flag = False
    
                else:
                    r = player_input.split(',')
                    if player_input[0] != '(' or player_input[-1] != ')':
                        print('\nPlease enter the NUMBER of your source and destination stool as an ordered pair!\n')
                    else:
                        try:
                            orginial_stool = int(r[0][1:])
                            destination_stool = int(r[1][:-1])
                        except ValueError:
                            print('\nPlease enter the NUMBER of your source and destination stool\n')
                        else:
                            if orginial_stool < self.model.get_number_of_stools() and destination_stool < self.model.get_number_of_stools():
                                move(self.model,orginial_stool, destination_stool)
                                print(self.model)
                            else:
                                print('\nPlease enter an appropriate stool and/or cheese\n')
                                
                
                        
                    
                    
                    
                    
            
            
                
            
            
        

if __name__ == '__main__':
 
    play = True
    
    print('''\nWelcome to Tower of Anne Hoy game! \nPlease Enter Number of stools and Number of Cheeses You Want to Play with\n''')          
    
    while play:
        try:
            cheese = input('Number of Cheese: ')
            number_of_cheese = int(cheese)
            if number_of_cheese < 0:
                raise ValueError
        except ValueError:
            if cheese.lower() == 'quit':
                print("goodbye")                
                play = False
            else:
                print("\nif you don't want to play enter quit\n")
        else:
            try:
                stools = input('Number of Stools: ')
                number_of_stools =  int(stools)
                if number_of_stools < 0:
                    raise ValueError                
            except ValueError:
                if stools.lower() == 'quit':
                    print("goodbye")
                    play = False
                else:
                    print("\nif you don't want to play enter quit\n")                
            else:  
                m = ConsoleController(number_of_cheese, number_of_stools)
                m.play_loop()
                play = False

