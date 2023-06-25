# NCurses

## What is NCurses?
### NCurses is a clone of the original System V Release 4.0 (SVr4) Curses. <br> The name Curses is supposd to be a pun on "Cursor Optimization" and NCurses stands for "New Curses".

### <p>&nbsp;</p>

## History/Background
### Back in the good ole days if you wanted a terminal (computer) to perform a specific task, such as print a line of text, you would need to use escape sequences. <br>
### These sequences are special charcter codes that allow a terminal to perform certain actions. Of course as time went on, different terminals would require different characters codes to interact with it. <br>
### With this, the designers of UNIX invented the 'termcap' conecpt which later became 'terminfo'. It is a file that provides all of the capabilities that a terminal may have, as well as the escape sequences required to trigger these effects. <br>

### <p>&nbsp;</p>

## Where does NCurses fit into this?
### The original Curses library is essentially a wrapper that prevents someone from having to deal with raw terminal codes. Now although NCurses is a clone of the original Curses library, it also provides a framework to create better looking Text-based User Interfaces (TUIs).
### A few examples of NCurses's capabilites include moving the cursor to any point in the terminal, changing the color of the text and background, and handling events for mouse interaction.

### <p>&nbsp;</p>

## Alternatives
### FINAL CUT
### C++ Library
### Unix-like Systems

### <p>&nbsp;</p>

### termbox
### C Library - Has a Python module as well
### Linux Systems


### <p>&nbsp;</p>

# My Experience with NCurses
## NCurses (New Curses) vs PDCurses (Public Domain Curses)
### Both of them are continuations of curses, and offer ports to Windows systems. However, I've read online that NCurses is more stable, more user friendly, and offers functionality such as menu and form support whereas PDCurses does not.<br>

### <p>&nbsp;</p>

## Windows Subsystem for Linux (WSL)
### Before I realized that there was a port developed for NCurses to Windows and MinGW32, I figured NCurses was only available on Linux systems. <br> 
### To use NCurses this way, I had to install WSL in order to use it since I don't own any hardware running a Linux system. <br>
### The distribution I used was Ubuntu 22.04.2 LTS which was availble in the Microsoft Store.

### <p>&nbsp;</p>

# Example Code
### Main Code
<img src="images/code1.png"  width=480>

### Cursor Placement Code
<img src="images/code2.png"  width=720>

### Result
<img src="images/output1.png"  width=1200>

### Bordered Window Code
<img src="images/code3.png"  width=720>

### Result
<img src="images/output2.png"  width=960>

### <p>&nbsp;</p>

# Applications built using NCurses
<!-- Source -->
<!-- https://htop.dev/images/htop-2.0.png -->
### htop (Interactive Process Viewer for Linux)
<img src="images/htop.png"  width=960>

### Nano (Text Editor for Linux Terminals)
<img src="images/nano_logo.jpg"  width=960>

<!-- Source -->
<!-- https://www.youtube.com/watch?v=YgNVkB8cI80 -->
<!-- Allows user to place windows wherever they want. -->
### NetHack (NCurses Interface Version)
<img src="images/nethackncurses.gif"  width=960>

### Alien: Isolation Console Remake
### Original Splash Screen
<img src="images/og_alien1.jpg"  width=960>

### Remake Splash Screen
<img src="images/ncurses_alien1.png"  width=960>

### Original Personal Screen
<img src="images/og_alien2.jpg"  width=960>

### Remake Personal Screen
<img src="images/ncurses_alien2.png"  width=960>

<!-- Source -->
<!-- https://www.youtube.com/watch?v=LgvLfR2zG3g&list=PLTTuTDBxpjWjnSc316lTqKRyUuN1yu1uM&index=15&t=1s -->
<!-- Creates own graphics library to visualize a 3D game using NCurses to place pixels anywhere in terminal. -->
### 3D Terminal Game (by KayOS Code on YouTube)
<img src="images/ncursesgame.gif"  width=960>