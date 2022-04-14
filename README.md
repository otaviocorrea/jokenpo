<h1 align="center">
   JOKENPO
</h1>

<div align="center">
  <a href="#-Project">Project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Execution">Execution</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Rules">Rules</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-Settings">Settings</a>&nbsp;&nbsp;&nbsp;
</div>

<p align="center">
  <p align="center">
  <img alt="jokenpo" src="./assets/img/header_preview.png" width="100%">
</p>

## 💻 Project

A simple but amazing Jokenpo game developed in python for language fixing!

## 📦 Execution

  ```bash
  $ python main.py
  ```

## 📜 Rules

- Each victory you win will be counted `3` points;
- Each tie between you and the machine will count `1` point;
- Each loss will count `-1` point to the current total score;
- A total of `10` points are required to finish the match;
- To select the move, type, in uppercase or lowercase, the respective word of the move;
  - 🪨 Stone;
  - 📄 Paper;
  - ✂️ Scissors.
- The results will be shown at the end of the match but it is always possible to check in rank.txt.
- 
##### ⚠️ All settings, which are present in the [settings.py](https://github.com/otaviocorrea/jokenpo/blob/master/cfg.py) file, can be manipulated to make the game easier or harder.⚠️

## ⚙️ Settings

This system/game has some settings that can be changed, either in order to facilitate or even make the matches difficult. To do this, access the [settings file](https://github.com/otaviocorrea/jokenpo/blob/master/cfg.py) and adjust as desired.

|      property      |         type        |  default  |                        action                         | 
|:-------------------|:--------------------|:----------|:------------------------------------------------------|
|pointsNeeded        | `integer`           |    10     | Sets the number of points needed to finish the match  |
|points_when_winning | `integer`           |    3      | Sets the number of points the player earns for winning|
|points_on_tie       | `integer`           |    1      | Sets the number of points the player gets for a tie   |
|points_on_losing    | `integer`           |   -1      | Sets the number of points the player earns on losing  |
|options             |  `Array<Integer>`   | [1, 2, 3] | Defines the options to be evaluated                   |
