from xlrd import open_workbook
import copy

#Evaluate the linear regression
NUMBER_OF_STUDENTS=649
NUMBER_OF_TEST = 130
NUMBER_OF_TRAINING = 519
wb = open_workbook('/home/mali/Desktop/MLHW1/MultipleLinearRegressionMLHW1/student-porxls.xls')
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
for i in range(0,36):
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
	theta_size = 36
	errorsum=0
	for it in range(theta_size):
		for row in range(0, NUMBER_OF_TRAINING-1):
			errorsum = errorsum + (X[row][36]-predictions[row])*X[row][it]
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
			for cell in range(0,31):
				
				if isinstance(sheet.cell(row,cell).value, basestring):
					#index of Mjob column is here sample array gains 2 more index cell cell +1 cell +2
					if cell == 8:
						
						sample.append(0)
						sample.append(0)
						sample.append(0)
				
						if sheet.cell(row,cell).value == 'at_home':
							sample[cell]=-1;
						elif sheet.cell(row,cell).value == 'services':
							sample[cell]=1;
						elif sheet.cell(row,cell).value == 'other':
							sample[cell+1]=-1;
						elif sheet.cell(row,cell).value == 'health':
							sample[cell+1]=+1;
						elif sheet.cell(row,cell).value == 'teacher':
							sample[cell+2]=-1;
					
					#index of Fjob column is here sample array gains 2 more index cell cell +1 cell +2
					elif cell == 9:
						sample.append(0)
						sample.append(0)
						sample.append(0)
				
						if sheet.cell(row,cell).value == 'at_home':
							sample[cell+2]=-1;
						elif sheet.cell(row,cell).value == 'services':
							sample[cell+2]=1;
						elif sheet.cell(row,cell).value == 'other':
							sample[cell+3]=-1;
						elif sheet.cell(row,cell).value == 'health':
							sample[cell+3]=+1;
						elif sheet.cell(row,cell).value == 'teacher':
							sample[cell+4]=-1;
						
					#index of reason column is here sample array gains 1 more index cell cell +1 
					elif cell == 10:
						sample.append(0)
						sample.append(0)
						if sheet.cell(row,cell).value == 'home':
							sample[cell+4]=-1;
						elif sheet.cell(row,cell).value == 'reputation':
							sample[cell+4]=1;
						elif sheet.cell(row,cell).value == 'course':
							sample[cell+5]=-1;
						elif sheet.cell(row,cell).value == 'other':
							sample[cell+5]=+1;
					#index of guardian column is here sample array gains 1 more index cell cell +1 
					elif cell == 11:
						sample.append(0)
						sample.append(0)
						if sheet.cell(row,cell).value == 'mother':
							sample[cell+5]=-1;
						elif sheet.cell(row,cell).value == 'father':
							sample[cell+5]=1;
						elif sheet.cell(row,cell).value == 'other':
							sample[cell+6]=-1;

					elif sheet.cell(row,cell).value == 'GP':
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
					elif sheet.cell(row,cell).value == 'yes':
						sample.append(1)
					elif sheet.cell(row,cell).value == 'no':
						sample.append(-1)
					else:
						sample.append(0)
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


samples = feature_normalize(samples,37)
test =readExcel(test,NUMBER_OF_TRAINING,650)

# sum( [a[i][0]*b[i] for i in range(len(b))] ) dot product 
for counter in range(0,NUMBER_OF_TEST-1):

	for cell in range(0,36):
		test[counter][cell] = test[counter][cell]-mean_r[cell]


theta = gradient_descent(samples, theta, alpha, iterations)

normalizedTestData = feature_normalize(test,36)
#print theta
#print len(samples[1]), "length of every sample"

#print len(theta) , "length"
#print mean_r
#print mean_r[36] , "36. mean"
#print len(normalizedTestData[1]) , "length NTD"
#print samples[1]

print mean_r[36]
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

		sumofErrors = sumofErrors + ((sum(samples[row][i]*theta[i] for i in range(len(theta)))- test[row][36]) ** 2)
	sumofErrors = sumofErrors / NUMBER_OF_TRAINING-2

   	return sumofErrors

def compute_costMAETRAINING():
	sumofErrors=float(0)
	for row in range(0, NUMBER_OF_TRAINING-2):

		sumofErrors = sumofErrors + ((sum(samples[row][i]*theta[i] for i in range(len(theta))) - test[row][36]))
	sumofErrors = sumofErrors / NUMBER_OF_TRAINING-2

   	return sumofErrors

def compute_costMSE():
	sumofErrors=float(0)
	for row in range(0, NUMBER_OF_TEST+1):
		sumofErrors = sumofErrors + ((sum(normalizedTestData[row][i]*theta[i] for i in range(len(theta)))*std_r[36] + mean_r[36]- test[row][36]) ** 2)
	sumofErrors = sumofErrors / NUMBER_OF_TEST

   	return sumofErrors

def compute_costMAE():
	sumofErrors=float(0)
	for row in range(0, NUMBER_OF_TEST+1):
		sumofErrors = sumofErrors + abs((sum(normalizedTestData[row][i]*theta[i] for i in range(len(theta)))*std_r[36] + mean_r[36] - test[row][36]))
	sumofErrors = sumofErrors / NUMBER_OF_TEST

   	return sumofErrors

#print compute_costMSETRAINING()
#print compute_costMAETRAINING()

print compute_costMSE()
print compute_costMAE()




'''
After adding Standard deviation feature to code some changes might be happened to the calculation. I am not sure
There still some blanks to fill
I need to re-look all of the code
For second task text parsing should be added.  May be logictic regression should be added as well.
'''
