import sys
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

#Argument 1 must be your plotly username, argument 2 is your api key. Get those by registering for a plotly account.
#Argument 3 is the name of the input file to input data from. Must be in the form: Date \n Download \n Upload \n

plotly.tools.set_credentials_file(username=sys.argv[1], api_key=sys.argv[2])

time = []
download = []
upload = []
lnum = 1
x = 1

file = open(sys.argv[3], 'r')

for line in file:
	
	if lnum == 1:
		#time.append(line[11:13])
		time.append(x)
		x += 1
		lnum = 2
	
	elif lnum == 2:
		download.append(line[10:15])
		lnum = 3
	
	elif lnum == 3:
		upload.append(line[8:12])
		lnum = 1
	
	else:
		raise SystemError('lnum internal error', lnum)
		
	

#trace1 = go.Histogram(
#	x=time,
#	y=download,
#	opacity=0.75
#)

#trace2 = go.Histogram(
#	x=time,
#	y=upload,
#	opacity=0.75
#)

#data = [trace1, trace2]
#layout = go.Layout(barmode='overlay')
#fig = go.Figure(data=data, layout=layout)

#py.iplot(fig, filename='Network Speed Graph')

trace1 = go.Bar(
	x=time,
	y=download,
	name='Download Speed'
)

trace2 = go.Bar(
	x=time,
	y=upload,
	name='Upload Speed'
)

data = [trace1, trace2]
layout = go.Layout(
	barmode='group'
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='Network Speed Graph')

