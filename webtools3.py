#!/usr/bin/env python3



def HTMLHeader():
    print("Content-Type: text/html; charset=UTF-8")  # Print headers
    print("")
    print("<html><body>")

def HTMLHeader_s():
    return("Content-Type: text/html; charset=UTF-8")

def HTMLFooter():
    #print('<a href="/index.html">Return to Main Page</a>')
    print('</body></html>')

#def HTMLObjectGenerator(*objects):
#    # Generates a list of objects in HTML format
#    print '''
#	Created the following Managed Object(s):<br>
#	'''
#    for object in objects:
#        print '%s<br>' % object
