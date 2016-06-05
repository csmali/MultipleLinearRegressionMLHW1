from xlrd import open_workbook
import copy

#Evaluate the linear regression
NUMBER_OF_STUDENTS=1049
NUMBER_OF_TEST = 209
NUMBER_OF_TRAINING = 840
wb = open_workbook('/home/mali/Desktop/MLHW1/MultipleLinearRegressionMLHW1/default_plus_chromatic_features_1059_tracks.xls')
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
for i in range(0,69):
	theta.append(0)

iterations = 300

alpha = 0.001

def gradient_descent(X,theta, alpha, num_iters):

    #y ussu dizim tek boyutlu
    predictions = []
    for row in range(0, NUMBER_OF_TRAINING-1):	
	predictions.append(0) 
    for i in range(num_iters):
	for row in range(0, NUMBER_OF_TRAINING-1):
		ytemp = sum( [X[row][k]*theta[k] for k in range(len(theta))] )
        	predictions[row]=ytemp 
		ytemp=0
	# size of theta 36
	theta_size = 68
	errorsum=0
	for it in range(theta_size):
		for row in range(0, NUMBER_OF_TRAINING-1):
			errorsum = errorsum + (X[row][68]-predictions[row])*X[row][it]
		theta[it] = theta[it] + alpha * errorsum
		errorsum=0
    #    theta_size = theta.size 
    return theta


#after reading excel every sample has 30  essential + 6 additional index of features filled with 1 and 0 or not normalized values
def readExcel(rowArray,startIndexofRowArray,LastIndexofRowArray):
	for sheet in wb.sheets():
		#number_of_rows = sheet.nrows
		number_of_rows=NUMBER_OF_TRAINING
		for row in range(startIndexofRowArray, LastIndexofRowArray):
			sample = []
			for cell in range(0,69):
					if cell == 68:
						sample.append(sheet.cell(row,cell+1).value)
					else:
						sample.append(sheet.cell(row,cell).value)
			rowArray.append(sample)

	return rowArray

'''
samples= readExcel(samples,NUMBER_OF_TEST,650)
samples = feature_normalize(samples,37)

test =readExcel(test,1,NUMBER_OF_TEST)
'''
samples = readExcel(samples,1,NUMBER_OF_TRAINING)


samples = feature_normalize(samples,69)
test =readExcel(test,NUMBER_OF_TRAINING,1049)

# sum( [a[i][0]*b[i] for i in range(len(b))] ) dot product 
for counter in range(0,NUMBER_OF_TEST-1):

	for cell in range(0,68):
		test[counter][cell] = test[counter][cell]-mean_r[cell]


theta = gradient_descent(samples, theta, alpha, iterations)

normalizedTestData = feature_normalize(test,68)
#print theta
#print len(samples[1]), "length of every sample"

#print len(theta) , "length"
#print mean_r
#print mean_r[36] , "36. mean"
#print len(normalizedTestData[1]) , "length NTD"
#print samples[1]

#print mean_r[68]
#print len(samples)
#for row in range(0, NUMBER_OF_TEST):	
	#print sum(normalizedTestData[row][i]*theta[i] for i in range(len(theta)))*std_r[36] + mean_r[36] , "   " ,row, ". data icin hesap"
'''
def compute_costMSE():
	sumofErrors=float(0)
	for row in range(0, NUMBER_OF_TEST+1):
		sumofErrors = sumofErrors + ((sum(normalizedTestData[row][i]*theta[i] for i in range(len(theta)))+mean_r[36] - test[row][36]) ** 2)
	sumofErrors = sumofErrors / NUMBER_OF_TEST
   	return sumofErrors
def compute_costMAE():
	sumofErrors=float(0)
	for row in range(0, NUMBER_OF_TEST+1):
		sumofErrors = sumofErrors + abs((sum(normalizedTestData[row][i]*theta[i] for i in range(len(theta)))+mean_r[36] - test[row][36]))
	sumofErrors = sumofErrors / NUMBER_OF_TEST
   	return sumofErrors
'''
def compute_costMSETRAINING():
	sumofErrors=float(0)
	for row in range(0, NUMBER_OF_TRAINING-2):
		sumofErrors = sumofErrors + ((sum(samples[row][i]*theta[i] for i in range(len(theta)))- samples[row][68]) ** 2)
	sumofErrors = sumofErrors / (NUMBER_OF_TRAINING-2)

   	return sumofErrors

def compute_costMAETRAINING():
	sumofErrors=float(0)
	for row in range(0, NUMBER_OF_TRAINING-2):
		sumofErrors = sumofErrors +  ((sum(samples[row][i]*theta[i] for i in range(len(theta))) - samples[row][68]))
	sumofErrors = sumofErrors / (NUMBER_OF_TRAINING-2)

   	return sumofErrors

def compute_costMSE():
	sumofErrors=float(0)
	for row in range(0, NUMBER_OF_TEST):
		sumofErrors = sumofErrors + ((sum(normalizedTestData[row][i]*theta[i] for i in range(len(theta)))*std_r[68] + mean_r[68]- test[row][68]) ** 2)
	sumofErrors = sumofErrors / NUMBER_OF_TEST

   	return sumofErrors

def compute_costMAE():
	sumofErrors=float(0)
	for row in range(0, NUMBER_OF_TEST):
		sumofErrors = sumofErrors + abs((sum(normalizedTestData[row][i]*theta[i] for i in range(len(theta)))*std_r[68] + mean_r[68] - test[row][68]))
	sumofErrors = sumofErrors / NUMBER_OF_TEST

   	return sumofErrors

#print compute_costMSETRAINING()
#print compute_costMAETRAINING()

print compute_costMSE()
print compute_costMSETRAINING()




'''
After adding Standard deviation feature to code some changes might be happened to the calculation. I am not sure
There still some blanks to fill
I need to re-look all of the code
For second task text parsing should be added.  May be logictic regression should be added as well.
'''
