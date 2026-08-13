"""
selection of MPCS exams include a fitness test which is conducted on ground. There will be a batch of 3 trainees, appearing for running test in track for 3 rounds. You need to record their oxygen level after every round. after trainee are finished with all rounds, calculate for each trainee his avarage oxygen level over the 3 rounds and select one with highest oxygen level as the most fit trainee. if more than one trainee attains the same highest avarage level, they all need to be selected

Display most fit Trainee and the highest avarage oxygen level.
 NOTE:
 . The oxygen value entered should not be accpeted if it is not in the range of 0 to 100

 EXAMPLE:
Input Values:
  95
  92
  95
  92
  90 
  95
  92
  90
  92
  90
  92
  90
Output Values:
  Most Fit Trainee: 1,3
"""

trainee = [[], [], [], []]

for i in range(3):
    for j in range(3):
        trainee[i].append(int(input()))
        if trainee[i][-1] not in range(1, 101):
            print("Invalid Values")

for i in range(3):
    trainee[3].append(
        (trainee[2][i] + trainee[1][i] + trainee[0][i]) // 3
    )

maximum = max(trainee[3])

for i in range(3):
    if trainee[3][i] < 70:
        print("Trainee {0} is unfit".format(i + 1))
    elif trainee[3][i] == maximum:
        print("Trainee Number:", i + 1)