import csv
import statistics
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import random

df=pd.read_csv('py/medium_data(1).csv')
data=df["reading_time"].to_list()

mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
#print("The mean is ",mean)
#print("The standard deviation is ",std_deviation)

#fig=ff.create_distplot([data],["Math_score"],show_hist=False)
#fig.show()

#Function to get the mean of the data samples
def random_set_of_mean(counter):
    dataset=[]
    mean_list=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
    #std_deviation=statistics.stdev(dataset)
    #print("The sample mean is ",mean)
    #print("The sample's standard deviation is ",std_deviation)

#Function to get the mean of 100 data points 1000 times and plot the graph
mean_list=[]
for i in range(0,1000):
    set_of_mean=random_set_of_mean(100)
    mean_list.append(set_of_mean)

#Function to plot the mean on the graph
mean=statistics.mean(mean_list)
std_deviation=statistics.stdev(mean_list)
#print("The sample distribution mean is ",mean)
#print("The sample distribution standard deviation is ",std_deviation)
fig=ff.create_distplot([mean_list],["Temperature"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="Mean"))
#fig.show()

first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)

#Finding the mean of the fisrt data
df=pd.read_csv('py/sample_2(P-111).csv')
data=df["reading_time"].to_list()
mean_of_sample1=statistics.mean(data)
#std_deviation_of_sample1=statistics.stdev(data)
print("The mean of sample 1 is ",mean_of_sample1)
#print("The standard deviation of sample 1 is ",std_deviation_of_sample1)
fig=ff.create_distplot([mean_list],["Student Marks 1"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample1,mean_of_sample1],y=[0,0.17],mode="lines",name="Mean of Sample"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="Std.deviation 1 end"))
fig.show()

#Finding the mean of the second data (Students who had extra classes)
df=pd.read_csv('py/sample_2(P-111).csv')
data=df["reading_time"].to_list()
mean_of_sample2=statistics.mean(data)
#std_deviation_of_sample2=statistics.stdev(data)
print("The mean of sample 1 is ",mean_of_sample2)
#print("The standard deviation of sample 2 is ",std_deviation_of_sample2)
fig=ff.create_distplot([mean_list],["Student Marks 2"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample2,mean_of_sample2],y=[0,0.17],mode="lines",name="Mean of Sample 2"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="Std.deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="Std.deviation 2 end"))
fig.show()

#Finding the mean of the third data (Students who were enforced with registers)
df=pd.read_csv('py/sample_2(P-111).csv')
data=df["reading_time"].to_list()
mean_of_sample3=statistics.mean(data)
#std_deviation_of_sample3=statistics.stdev(data)
print("The mean of sample 3 is ",mean_of_sample3)
#print("The standard deviation of sample 3 is ",std_deviation_of_sample2)
fig=ff.create_distplot([mean_list],["Student Marks 3"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[mean_of_sample3,mean_of_sample3],y=[0,0.17],mode="lines",name="Mean of Sample 3"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="Std.deviation 1 end"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="Std.deviation 2 end"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="Std.deviation 3 end"))
fig.show()

#Finding the 'z-score' using this formula
z_score=(mean_of_sample1-mean)/std_deviation
print("The z score is ",z_score)