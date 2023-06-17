# mathFunctions
A program that provides math functions including a spread function and a pseudorandom number generator. The spread function takes an array and performs a hash operation based on a module value, producing a modified array. The pseudorandom number generator generates a sequence of pseudorandom numbers based on a given seed, module value, multiplier, and increase value.

<p align="center">
  <br>
  <img src="https://storage.googleapis.com/kaggle-competitions/kaggle/3867/media/rn3.gif" alt="pic" width="500">
  <br>
</p>
<p align="center" >
  <a href="#Files">Files</a> •
  <a href="#Features">Features</a> •
  <a href="#how-to-use">How To Use</a> 
</p>

## Files

- src: the file that implements de solution.

## Features
The main features of the application include:
- Spread function: It takes an array as input and applies a hash function based on a module value, resulting in a modified array with spread elements.
- Pseudorandom number generator: It generates a sequence of pseudorandom numbers using the linear congruential method. It requires inputs such as the module value, multiplier value, increase value, and seed value.
- Menu-based interface: The code presents a menu where users can choose between the spread function and pseudorandom number generator options.
- User input: The code prompts the user to provide input values such as the module, array length, array elements, and pseudorandom number generator parameters.
- Output display: The code displays the results of the spread function and the generated sequence of pseudorandom numbers.
- Error handling: The code includes error checking to ensure valid user inputs and displays an error message for invalid options.

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

...
```bash
# Clone this repository
$ git clone https://github.com/bl33h/mathFunctions

# Open the folder
$ cd src

# Run the app
$ python mathFunctions.py

```
