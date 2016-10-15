import fitbit.fitbit_api as fitbit
"""

For the activities/log/calories resource, each data point also includes the level field that reflects calculated activity level for that time period 
( 0 - sedentary; 1 - lightly active; 2 - fairly active; 3 - very active.)
"""

def getOptionText(input_score):
	input_score=str(input_score)
	activitySummary={ "0": 'sedentary', '1' :'lightly active',  '2':'fairly active', '3': 'very active', '-1':"not so active"}
	return activitySummary[input_score]
	
try:
	activitySummary=fitbit.getActivitySummary()
	sleepLastNight=fitbit.getSleepLastNight()
except Error as e:
	print "something went wrong calling the fitbit api"

fitbit_summary_text='Yesterday you did {only} {steps} steps and slept {only} {sleep} hours'.format(steps=activitySummary['steps'], 
																							 only='only' if activitySummary["activeScore"]<0 else '',
																							sleep=sleepLastNight)
fitbit_activity_summary='In general, you were {option}. Some stats for you: total distance:{td}, lightly active minutes:{am}, sedentary minutes:{sm}'.format(
	option=getOptionText(activitySummary['activeScore']),
	td=activitySummary["distances"][0]["distance"],
	am=activitySummary["lightlyActiveMinutes"],
	sm=activitySummary["sedentaryMinutes"]
	)
""" Tags in JSON we can use

distances -> [{u'distance': 0.44, u'activity': u'total'}, {u'distance': 0.44, u'activity': u'tracker'}, {u'distance': 0, u'activity': u'loggedActivities'}, {u'distance': 0, u'activity': u'veryActive'}, {u'distance': 0, u'activity': u'moderatelyActive'}, {u'distance': 0.4, u'activity': u'lightlyActive'}, {u'distance': 0, u'activity': u'sedentaryActive'}]
sedentaryMinutes -> 1216
lightlyActiveMinutes -> 34
caloriesOut -> 1419
caloriesBMR -> 1310
marginalCalories -> 41
fairlyActiveMinutes -> 0
veryActiveMinutes -> 0
activityCalories -> 99
steps -> 590
activeScore -> -1
"""

print fitbit_summary_text
print fitbit_activity_summary