#total number of months included in dataset?
import os
import csv
csvpath=os.path.join('Resources','budget_data.csv')
txtpath=os.path.join('analysis','budget_analysis.txt')
months_list=[]
net=0
changes=[]
count=0
with open (csvpath) as csvfile:
      
  #set path for csv file
 csv_reader =csv.reader( csvfile , delimiter ="," )

  #Reading the header out
 csv_header =next(csv_reader)


  #read through each row of data after header:
 for lines in csv_reader:
     # print(lines[1])
      months_list.append(lines[0])
      net=net+int(lines[1])

      if count>0:
         changes.append(int(  lines [1])- previousprofitloss)

      previousprofitloss=int(lines[1])  
      count +=1 
print(len(months_list))
print(net)
avg_change=round(sum(changes)/len(changes),2)
print(avg_change)
  #greatest increase in profit/loss
greatest_increase=max(changes)
 #greatest decrease
greatest_decrease=min(changes)
print(greatest_increase,greatest_decrease)
max_index=changes.index(greatest_increase)
min_index=changes.index(greatest_decrease)
max_month=months_list[max_index+1]
min_month=months_list[min_index+1]
print(max_month,min_month)

output_text=(
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {len(months_list)}\n"
f"Total: ${net}\n"
f"Average Change: ${avg_change}\n"
f"Greatest Increase in Profits: {max_month} (${greatest_increase})\n"
f"Greatest Decrease in Profits: {min_month} (${greatest_decrease})" 

)

print(output_text)
with open (txtpath,"w") as txtfile:
 txtfile.write(output_text)
