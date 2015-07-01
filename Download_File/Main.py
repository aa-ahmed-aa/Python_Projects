from urllib import request

url="http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=5&e=28&f=2015&g=d&a=2&b=27&c=2014&ignore=.csv"

#function to Download the txt file
def fun_Download(csv_url):

    #connect to the web page
    response=request.urlopen(csv_url)

    #read the data in csv
    csv=response.read()

    #make sure that the written data to
    csv_str=str(csv)

    #arrange the txt file in lines
    lines=csv_str.split("\\n")

    #write the data to a file
    f=open('goog.csv','w')
    for line in lines:
        f.write(line+'\n')
    f.close()

fun_Download(url)