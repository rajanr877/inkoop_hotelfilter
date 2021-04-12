import csv

file = 'hotels.csv'

"""
Rating Chart
Price	    Rating	    Categories
400 – 999	1.0 – 4.9	Cheapest 
1000 – 1699	5.0 – 6.9	Average
1700 - 2200	7.0 – 10.0	Highest 
"""

def readFile(pfile):
	rows = []
	with open(pfile) as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    for row in csv_reader:
	        rows.append(row)
	return rows
	

def format_data(data):
	print('\n============== YOUR RESULT ==============\n')
	print("Sr.No.\tHotel Code\tState\t\tCost\tRatings")
	for values in data:
		print("{}\t\t{}\t{}\t{}\t\t{}".format(*values))


def classify_states():
	tamilnadu = [datum for datum in csv_data[1:] if datum[2] == 'Tamilnadu']
	maharashtra = [datum for datum in csv_data[1:] if datum[2] == 'Maharashtra']
	karnataka = [datum for datum in csv_data[1:] if datum[2] == 'Karnataka']
	india = csv_data[1:]
	return india, tamilnadu, maharashtra, karnataka


def select_state(p_state):
	i, t, m, k = classify_states()
	map_state = {'india':i, 'tamilnadu':t, 'maharashtra':m, 'karnataka':k}
	if p_state in map_state:
		return map_state[p_state]


def clasify_rating(p_data):
	cheapest = [datum for datum in p_data[1:] if float(datum[4]) <= 4.9]
	average_r = [datum for datum in p_data[1:] if float(datum[4]) >= 5 if float(datum[4]) <= 6.9]
	highest_r = [datum for datum in p_data[1:] if float(datum[4]) >= 7 if float(datum[4]) <= 10]
	return cheapest, average_r, highest_r


def clasify_cost(p_data):
	cheapest = [datum for datum in p_data[1:] if float(datum[3]) <= 999]
	average = [datum for datum in p_data[1:] if float(datum[3]) >= 1000 if float(datum[3]) <= 1699]
	highest = [datum for datum in p_data[1:] if float(datum[3]) >= 1700 if float(datum[3]) <= 2200]
	return cheapest, average, highest


def classify_type(cls_type):
	map_function = {'cost':clasify_cost, 'rating':clasify_rating}
	if cls_type in map_function:
		return map_function[cls_type]


def chose_category(cat,categorised):
	c, a, h = categorised
	map_data = {'cheapest':c, 'average':a, 'highest':h}
	if cat in map_data:
		return map_data[cat]


def options(state, classify, category):
	selected = select_state(state)
	classified_type = classify_type(classify)
	categorised = classified_type(selected)
	final_data = chose_category(category, categorised)
	format_data(final_data)


def user_input():
	state = input("What is the state: ").lower()
	cos_rat = input("Cost or Rating: ").lower()
	category = input("Operation: ").lower()
	return state, cos_rat, category


csv_data = readFile(file)
state, cos_rat, category = user_input()	
# options(state, cos_rat, category)


try:
	options(state, cos_rat, category)
except:
	print("\nIncorrect Value.")
	print("enter any of this state: india, tamilnadu, maharashtra, karnataka")
	print("enter any of this : cost, rating")
	print("enter any of this operation: cheapest, average, highest")
