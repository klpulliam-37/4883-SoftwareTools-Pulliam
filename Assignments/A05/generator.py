import graphviz
import csv
import random
from pprint import pprint

tree = graphviz.Digraph('FamilyTree')

clan_names = []
clan_colors = ['lightgrey', 'purple', 'yellow', 'red', 'lightblue', 'blue', 'green']
clans_found = []
clan_subgraphs = {}
first_names = []
last_names = []
csv_data = []
nodes = []

# with open('griffin_tree.csv', 'r') as data:

"""
Aquire the csv data and store it in a list for later use.
"""
with open('big_data3.csv', 'r') as data:
  csvFile = csv.reader(data)

  for row in csvFile:
    if row[0] != '#pid':
      csv_data.append(row)

  # for row in csv_data:
  #   print(row)

"""
Iterate through csv data and fix inconsistencies.
"""
def clean_data():
  fix_names()

def fix_names():
  # for row in csv_data:
  #   print(row)
  
  for person in csv_data:
    print(person)
    # Do they have a parent? If not, add a new name
    if person[-2] == "":
      person[1] = generate_random_name()
    
    # Is the parent the father? If so, derive name from it. 
    # If not, repeat for other parent.
    else:
      if csv_data[int(person[-2])][2] == "M":
        print(person[-2])
        print(str(csv_data[int(person[-2])]) + "========================>")
        person[1] = generate_random_first_name(csv_data[int(person[-2])][1].split()[1]) # Gets the lastname of the father
        person[-5] = csv_data[int(person[-2])][-5]                                         # Gets the clanname of the father
        # print(csv_data[int(person[-5])][-5])
      else:
        print(person[-3])
        print(str(csv_data[int(person[-3])]) + "<========================")
        person[1] = generate_random_first_name(csv_data[int(person[-3])][1].split()[1])
        person[-5] = csv_data[int(person[-3])][-5]

    # Are they married?
    if person[-4] != "":
      # Are they female?
      if person[2] == "F":
        # person[1] = generate_random_first_name(csv_data[int(person[-4])][1].split()[1]) # Gets the lastname of the spouse
        person[-5] = csv_data[int(person[-4])][-5]
      # If ont female, get their spouse.
      else:
        # csv_data[int(person[-4])][1] = generate_random_first_name(person[1].split()[1])
        csv_data[int(person[-4])][-5] = person[-5]
      # print(csv_data[int(person[-4])])
        
  # for row in csv_data:
  #   print(row)
    print(person)

# def fix_clan_names():
    #

# def fix_parent_child_relationships():
  

# print(csv_data)
"""
Create Nodes
- Create a node for each person
- Once each person is created, 
  loop through and create connections for each
"""
def create_nodes():
  for row in csv_data:
    # clan = int(row[-5])
    
    # If clan dosn't exist in tree, create a new subgraph
    if not clans_found[int(row[-5])]:
      clan_subgraphs[int(row[-5])] = graphviz.Digraph('cluster_' + clan_names[int(row[-5])])
      clan_subgraphs[int(row[-5])].attr(style='filled', color=clan_colors[int(row[-5])])
      clans_found[int(row[-5])] = 1
      
    # Add node to existing clan subgraph
    clan_subgraphs[int(row[-5])].node(row[0], '{Name: | Born-Died: | Age: | Clan:} | {%s | %s | %s | %s}'%(row[1], row[4] + '-' + row[5], row[6], clan_names[int(row[-5])]), shape='record')
    # print("printing subgraph")
    # print(clan_subgraphs[int(row[-5])])

def create_edges():
  for row in csv_data:
    # Checks if person is married
    if row[-4] != '':
      name = row[0] + 'and' + row[-4]
      # Need to add this node to cluster or else it will look weird
      clan_subgraphs[int(row[-5])].node(name, label='', shape='diamond', width='0.2', height='0.2')
      tree.edge(row[0], name, arrowhead='none')
      tree.edge(row[-4], name, arrowhead='none')
      # tree.edge(row[0], row[-4], style='invis')

    # Checks if person has parents
    if row[-2] != '':
      name = row[-2] + "and" + row[-3]
      tree.edge(name, row[0])
      # tree.edge(name, row[0], splines='curved)

def add_subgraphs():
  # Add the subgraphs to the main graph.
  # Done here since all data must be set first before inserting subgraphs
  for clan in clan_subgraphs:
    # print(clan_subgraphs[clan])
    tree.subgraph(clan_subgraphs[clan])

def create_clan_list():
  with open('clan_names.txt', mode='r') as data:
    csvFile = csv.reader(data)

    for row in csvFile:
      clan_names.append(row[0])
      clans_found.append(0)

def create_name_lists():
  with open('asian_firstnames.csv', 'r') as f_names:
    data = csv.reader(f_names)

    for row in data:
      first_names.append(row[1])
    f_names.close()

  with open('asian_lastnames.txt', 'r') as l_names:
    data = csv.reader(l_names)

    for row in data:
      last_names.append(row[0])
    l_names.close()

  # print(first_names)
  # print(last_names)

def generate_random_name():
  random.shuffle(first_names)
  random.shuffle(last_names)
  return first_names[0] + ' ' + last_names[0]

def generate_random_first_name(surname):
  random.shuffle(first_names)
  return first_names[0] + ' ' + surname
    
def write_to_source():
  with open("source.txt", "w") as sourceFile:
    sourceFile.write(tree.source)

"""
Testing area
"""
create_name_lists()
# print(generate_random_name())
# print(generate_random_first_name("Kayoba"))
clean_data()
create_clan_list()
create_nodes()
create_edges()
add_subgraphs()
write_to_source()
# print(clan_names)
# print(clans_found)
# print(clan_subgraphs)