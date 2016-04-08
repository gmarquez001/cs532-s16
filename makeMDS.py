#Acquired for Shawn Jones
#!/usr/local/bin/python

# all code here stolen shamelessly from 
# "Programming Collective Intelligence, Chapter 3"

import sys
import argparse 

sys.path.insert(0, '../libs')

import clusters

blognames,words,data=clusters.readfile('blogdata1V2.txt')

coords = clusters.scaledown(data)

clusters.draw2d(coords, blognames, jpeg='blogs2dV2.jpg')

