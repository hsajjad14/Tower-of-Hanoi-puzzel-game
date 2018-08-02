Use console controller to play the game in the console (shell), Or use gui_controller to play on the gui.
Here is the game in the gui_controller:

The start
![gui_start](https://user-images.githubusercontent.com/40809349/43599987-5766b992-9657-11e8-8291-9ea037287ab1.PNG)
The ending
![gui_end](https://user-images.githubusercontent.com/40809349/43599906-0860e944-9657-11e8-98e9-3d757c2e31d6.PNG)


Here it is in the Console controller:
![console_game](https://user-images.githubusercontent.com/40809349/43600007-6eae7284-9657-11e8-968f-1f9876d1305d.PNG)

To change the cheese's or number of stools for the gui_controller under "if __name__ == "__main__":"
change gui = GUIController(6, 4, 1024, 320, 20) to whatever you prefer, the first number is num of cheese and second is number of stools.

the tour class uses a recursive algorithm to solve the puzzel with any number of cheese on 4 stools in the fewest number of steps.

Here is the tour class solving the puzzel:
![tour_start](https://user-images.githubusercontent.com/40809349/43600070-98012a8c-9657-11e8-98a3-facda5f32236.PNG)

![tour_end](https://user-images.githubusercontent.com/40809349/43600035-7cfaa39e-9657-11e8-8849-615e1fdeadac.PNG)

