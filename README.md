# Spelling Bee Solver
> This program solves the New York Times Spelling Bee game

## Table of Contents
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)


## General Information
- This program creates a regular expression and uses `words_alpha.txt` (from [here](https://github.com/dwyl/english-words)) to find the possible words

## Technologies used
- Python 3.8.10

## Features
- Input the letters manually
- Receive a list of possible words
- Have the program automatically input the possibilities into the game
- Compare with a list of answers (if known) to see what words the program missed

## Setup
- Use `sudo python3 wordleHelper.py` to run the program (sudo is required for the auto-type functionality)

## Usage
- Follow the prompts and fill in the information requested in the terminal
- You will first be asked to input the letters, starting with the required letter
- You will then be asked if you want to be shown the list of possible words or if you want to auto-type the words
- If you select auto-type, go back to the game in your browswer and click on the text input field of the game, then press "esc" to start the input
- Beware! If you click out of the game before the auto-typing is complete, it will continue to type wherever you click!
- Before closing the program you are able to compare the algorithm's answers with a text file containing the real answers, this will of course only work if you have filled the `answers.txt` file

## Project Status
This project is complete

## Room for Improvement
- Retrieve the game letters automatically
- Make a GUI
- Better control over the auto-typing

## Acknowledgements
- The list of English words `words_alpha.txt` comes from [here](https://github.com/dwyl/english-words)
