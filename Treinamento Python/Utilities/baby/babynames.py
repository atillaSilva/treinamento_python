#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  arquivo = open(filename, 'r')
  html = arquivo.read()
  arquivo.close()
  for i in html.split():
      if i != None:
          arquivo = open(i, 'r')
          arquivo_html = arquivo.read()
          resposta = {}
          match = re.search(r'<h3 align="center">Popularity in \d\d\d\d</h3>', arquivo_html)
          year = match.group()
          year = year[-9:-5]
          resposta[year] = []
          for i in arquivo_html.split('\n'):
              match = re.search(r'<tr align="right"><td>\d*</td><td>\w*</td><td>\w*</td>', i)
              if match != None: 
                  resto = match.group()
                  inicio = resto.find('<td>') + 4
                  fim = resto.find('</td>')
                  numero = resto[inicio:fim]
                  inicio = resto[fim+9:].find('</td>')
                  resposta[year].append(resto[fim+9:fim+9+inicio] + ' ' + numero)
                  fim = fim+9+inicio
                  inicio = resto[fim+9:].find('</td>')
                  resposta[year].append(resto[fim+9:fim+9+inicio] + ' ' + numero)  
          print resposta
          arquivo.close()
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  extract_names(args[0])
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
