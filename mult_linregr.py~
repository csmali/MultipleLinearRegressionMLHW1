
from xlrd import open_workbook
import copy

#Evaluate the linear regression
NUMBER_OF_STUDENTS=649
NUMBER_OF_TEST = 519
NUMBER_OF_TRAINING = 130
wb = open_workbook('/home/mali/Desktop/python/MLhw1/student-por.xls')
samples = []
test = []
mean_r=[]
std_r=[]
#Some gradient descent settings
def std_deviation(X,ind):
	X_norm = copy.deepcopy(X)
	tempsum=float(0)
	for columnIndex in range(0,ind):
		for sample in X_norm:
			tempsum=tempsum + (sample[columnIndex]-mean_r[columnIndex])**2
		std_r.append((tempsum / len(X_norm)) ** 0.5)
def feature_normalize(X,ind):
	X_norm = copy.deepcopy(X)
	tempsum=0
	for columnIndex in range(0,ind):
		for sample in X_norm:
			tempsum=tempsum+sample[columnIndex]
		mean_r.append(tempsum/len(X_norm))
		tempsum=0
	std_deviation(X,ind)
	for columnIndex in range(0,ind):
		for sample in X_norm:
			if std_r[columnIndex]>0:
				sample[columnIndex]=(sample[columnIndex]-mean_r[columnIndex])/std_r[columnIndex]
			else:
				sample[columnIndex]=(sample[columnIndex]-mean_r[columnIndex])
			
	return X_norm
	
theta = []
for i in range(0,30):
	theta.append(0)

iterations = 500

alpha = 0.001

def gradient_descent(X,theta, alpha, num_iters):

    #y ussu dizim tek boyutlu
    predictions = []
    for row in range(0, NUMBER_OF_TRAINING-1):	
	predictions.append(0) 
    for i in range(num_iters):
	for row in range(0, NUMBER_OF_TRAINING-1):
		ytemp = sum( [X[row][i]*theta[i] for i in range(len(theta))] )
        	predictions[row]=ytemp 
		ytemp=0
	
	# size of theta 30
	theta_size = 30
	errorsum=0
	for it in range(theta_size):
		for row in range(0, NUMBER_OF_TRAINING-1):
			errorsum = errorsum + (X[row][30]-predictions[row])*X[row][it]
		theta[it] = theta[it] + alpha * errorsum
		errorsum=0
    #    theta_size = theta.size
   # print predictions
    return theta

def readExcel(rowArray,startIndexofRowArray,LastIndexofRowArray):
	for sheet in wb.sheets():
		#number_of_rows = sheet.nrows
		number_of_rows=NUMBER_OF_TRAINING
		for row in range(startIndexofRowArray, LastIndexofRowArray):
			sample = []
			for cell in range(0,31):
				if isinstance(sheet.cell(row,cell).value, basestring):
					if sheet.cell(row,cell).value == 'GP':
						sample.append(1)
					elif sheet.cell(row,cell).value == 'MS':
						sample.append(-1)
					elif sheet.cell(row,cell).value == 'F':
						sample.append(1)
					elif sheet.cell(row,cell).value == 'M':
						sample.append(-1)
					elif sheet.cell(row,cell).value == 'U':
						sample.append(1)
					elif sheet.cell(row,cell).value == 'R':
						sample.append(-1)
					elif sheet.cell(row,cell).value == 'LE3':
						sample.append(1)
					elif sheet.cell(row,cell).value == 'GT3':
						sample.append(-1)
					elif sheet.cell(row,cell).value == 'T':
						sample.append(1)
					elif sheet.cell(row,cell).value == 'A':
						sample.append(-1)
					elif sheet.cell(row,cell).value == 'mother':
						sample.append(1)
					elif sheet.cell(row,cell).value == 'father':
						sample.append(-1)
					else:
						sample.append(0)
				else:
					sample.append(sheet.cell(row,cell).value)
			rowArray.append(sample)

	return rowArray

samples = readExcel(samples,1,NUMBER_OF_TRAINING)
samples = feature_normalize(samples,31)
test =readExcel(test,NUMBER_OF_TRAINING,650)

# sum( [a[i][0]*b[i] for i in range(len(b))] ) dot product 
for counter in range(0,NUMBER_OF_TEST-1):

	for cell in range(0,30):
		#print cell
		test[counter][cell] = test[counter][cell]-mean_r[cell]

theta = gradient_descent(samples, theta, alpha, iterations)

normalizedTestData = feature_normalize(test,30)

def compute_costMSE():
	sumofErrors=float(0)
	for row in range(0, NUMBER_OF_TEST+1):
		sumofErrors = sumofErrors + ((sum(normalizedTestData[row][i]*theta[i] for i in range(len(theta)))+mean_r[30] - test[row][30]) ** 2)
	sumofErrors = sumofErrors / NUMBER_OF_TEST

   	return sumofErrors

def compute_costMAE():
	sumofErrors=float(0)
	for row in range(0, NUMBER_OF_TEST+1):
		sumofErrors = sumofErrors + abs((sum(normalizedTestData[row][i]*theta[i] for i in range(len(theta)))+mean_r[30] - test[row][30]))
	sumofErrors = sumofErrors / NUMBER_OF_TEST

   	return sumofErrors

print compute_costMSE()
print compute_costMAE()








