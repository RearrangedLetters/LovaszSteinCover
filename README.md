# Lovasz Stein Graph Covering

## Set Up
This project has a couple of dependencies. 
For creating the animations used in the presentation, please make sure
Manim Community and the necessary dependencies are installed.
To achieve this, check the section for your operating system in the
[Manim Installation Guide](docs.manim.community/en/stable/installation.html).

All scripts are written to be run in a Linux terminal.
If you're working on a different operating system there might be additional steps.
Otherwise, you can run compile_latex in the folder Presentation to compile the presentation,
including a bibliography.
To recreate the images rendered with manim, execute run_manim in the folder Animations.

## Project Overview
This repository accompanies a presentation on the Lovász-Stein theorem and an application.
The presented proofs of said theorems are based on the book Extremal Combinatorics: With Applications in Computer Science
by Stasys Jukna.
The presented application has been adapted from the paper 
'The Stein-Lovasz Theorem and Its Applications to Some Combinatorial arrays' by Deng et al.

Additionally, to the LaTex code for the presentation itself and the Manim code to create some images in the
presentation, the repository comes with an implementation of the Lovász-Stein algorithm.
While this algorithm is based on the presented algorithm, some adjustments have been made to achieve a more
reasonable time complexity.
There are other, reasonably simple, changes one could make to further improve the time complexity.