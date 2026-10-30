# Mastery Project

### _By:_ Vivaan Loiwal

This is the code for my project in Mastery, a class where we get to follow our passions.

## Introduction

This class begun with our teacher, Ana Paula Giorgi (AP) teaching us how real companies brainstorm ideas, such as IDEO, and the engineering process, which we'll need for our ideas. We followed this process in a fun starting project - pencilcases. Each of us interviewed one of our other classmates, and got the specifications for our pencilcases. Then, we made quick prototypes, and pitched them to the class, showing why our pencilcase turned out good, and its features.

## My Idea

This beginning process ended, and we began brainstorming. Any idea was a good idea, but we had to trim down our list to ones which were possible, not too expensive or inaccessible, and which fit our passion, and which we would be determined to finish.

## The Spark and Direction

AP called this our **SPARK**, which is our reason, and drive for doing this. After we thought about this, and came up with ideas, we filled out some worksheets for why we wanted to do this project, and what guaranteed that we would see it through. After these, and one-on-ones, we moved on to our **DIRECTION**, which is where we're going to go with our project. After this process, I decided to go along robotics, one of my largest passions, and something I would always continue.

## My Project

After some more research, I decided I was going to make a ball-balancing robot, like this robot from the Raspberry Pi Official Magazine: <br><br>![babot ball-balancing robot image](images/balancing_robot_inspiration.png)<br><br>
But I wanted to make everything on my own - no downloading premade CAD, or code.

## How It Works

This robot uses computer vision to track a ball on a clear plate. There is a camera mounted under the plate, and it sees the ball. Then, it calculates the angles of the arms, tilting the ball towards the target position. I would need to get all of the parts, using a Raspberry Pi, and design a PCB to connect them. Also, I would have to CAD the arms, and the joints, so I decided to use Onshape. Also, I will need to learn OpenCV, because I want to code all of this in python, the language I'm most comfortable with.

## Side Project(s)

This led me to do some side projects, to acquire the knowledge I needed. So first, I needed to learn more about PCB design, and soldering and connecting parts. So I decided to make a coin "flipping" robot, which would use a PCB, an OLED display, and a button, so when you pressed it, and picks 1 or 2, and displays "heads" or "tails" on the OLED. This was a simple, but effective project, and it taught me how to solder and combine the parts and make a real thing. But this project took a while, because it took over 2 weeks for the PCB to arrive, which I designed on [EasyEDA.com](https://easyeda.com), and ordered from [PCBWay.com](https://pcbway.com). But in that time, I decided to learn OpenCV, and with the help of Claude, created three things, which you can see in the [openCV folder](openCV), and in [ball balancer/Ball Tracker](ball%20balancer/Ball%20Tracker).

## Coin Flipper

First, I tested using a breadboard, because all of my parts arrived before the PCB, and it worked pretty well - all of the wiring and code worked - [Watch it work](https://github.com/user-attachments/assets/ba926a66-a484-422e-8f71-145f48802697)

After the PCB finally arrived, I combined everything, and it turned out like this: ![Final Coin Flipper Video](images/SRC.mp4)

## Final Project

### Parts List

I used Claude to help me come up with my parts list, which filled all of my requirements. I had to cut some things which would have been nice, but were too expensive. This parts list is at [ball balancer/parts-list.md](ball%20balancer/parts-list.md), and after some iterations, I got it down to around $130, which would fit my budget. After sending this to my teacher, I found out that we had a Raspberry Pi 3B v1.2, so I'm using that, along with the SD card and power which we have.

### PCB Design

For this project, I needed a more complicated PCB, with spots for servos, a camera, and a lot of other parts, but they had to be removable, or for me to solder wires in. This meant I had to make a lot of ports for me for these. Also, my Raspberry Pi 3B had it's headers on top, so I had to design the PCB to go upside down, and plug into that. This PCB didn't have to be too complicated though - it only had to fit a servo controller, the Raspberry Pi, and spots for the battery to be soldered in. Also, my warm-up project's PCB didn't arrive for a while, due to a shipping error, so I switched to [JLCPCB.com](https://www.jlcpcb.com), which was cheaper, and had more delivery options.

### An Unfortunate Detour

For me, I faced a large problem with the Raspberry Pi, because I got a used one from school, which couldn't connect to wifi, so I spent multiple days trying to get it connected to some wifi, so that I could upload my code. Finally, I took it home, and plugged it in directly to my wifi router, giving it wifi so I could upload my code. I uploaded the code, but it stopped halfway through, because it ran out of storage. After some looking, it turned out that it only had an 8GB SD card, which was too small for the modules I needed, and the code, so I had to wait for a 16- or 32GB card. After two days, our IT gave me a 128GB SD card, which was way more than I needed, but worked. Also, in this time, my parts finally got ordered from my teacher, which meant I could almost start.

### Soldering Practice

I needed to learn soldering, where you use a REALLY hot iron (at 400 degrees celcius) to melt soldering tin onto an electrical joint to combine them. This is commonly used on PCBs, which I was going to use, to connect parts to it. I have the Plusivo soldering kit, which has everything I needed, so for about two hours, I learned and practiced soldering on some perfboards off amazon, using resistors which I had. It was good practice, and the top ended up looking like this: <br>
![Soldering practice image](images/soldering.jpg)

### STATUS UPDATE | 10/29/16

As of now, I’ve completed my warm-up project, except for the PCB which will arrive in less than 2 weeks, and began the code for my final project, along with ordering parts for it, and setting up the SD card. My next steps include learning how to solder, and re-setting up the SD card, which is now 128GB and uploading my code to it. I'll then work on any code which I can do without tuning, such as the PID, and then when my parts arrive, I will assemble it, CAD and print my 3d-printed parts (which I will upload here), and I'll tune the code, and make it work!
