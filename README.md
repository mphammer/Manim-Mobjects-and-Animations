# Manim-Mobjects-and-Animations

## Overview

Manim is an open-srouce python library for generating videos of Mathematical Visualizations. 

This repo contains code that showcases two of Manim's fundamental resources:
1. MObjects - the objects that you can move around and transform
2. Animations - the different things you can do to the MObjects (moving them around, transforming them, etc.)

[mobjects.py](./mobjects.py) contains code that shows almost all of the mobjects. It shows them one after another with the name at the top. [animations.py](./animations.py) is the same but for almost all of the animations. 

You can use the code as a reference for very simple examples. The Manim Community also has documentation on their website [here (Manim Community)](https://docs.manim.community/en/stable/reference.html). 


## Watch Online

You can view the videos created by each of these files on my [YouTube Channel](https://www.youtube.com/channel/UC3xlS5T2M6we94bCsYneNXA): 

1
[![Watch the video](https://img.youtube.com/vi/bCsk6hnMO5w/default.jpg)](https://youtu.be/bCsk6hnMO5w)

2
<a href="http://www.youtube.com/watch?feature=player_embedded&v=bCsk6hnMO5w" target="_blank">
 <img src="http://img.youtube.com/vi/bCsk6hnMO5w/mqdefault.jpg" alt="Youtube: Manim Animations" width="500" border="10" />
</a>


## Running the Code
You need to have python and manim set up on your computer. Please search for documentation for [setting up Python](https://www.youtube.com/watch?v=M323OL6K5vs) and visit the [Manim Community website to install Manim](https://docs.manim.community/en/stable/installation.html).  

Here are the versions I am using:  
```
$ python --version
Python 3.10.0

$ manim --version
Manim Community v0.17.3
```

These commands will generate each of the videos if you run them in your Terminal:  
```
$ manim -pql mobjects.py
$ manim -pql animations.py
```
