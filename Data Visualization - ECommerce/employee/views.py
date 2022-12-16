from django.shortcuts import render  
from employee.models import Employee  

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import *

# Create your views here.  

def show(request):  
    val_f = 0
    val_s = 0
    list = [
        "Payment Distribution of all branches", 
        "ender Count in E-Commerce Platform", 
        "Type of customers", 
        "Payment Methods",
        "Payment Distribution of all branches",
        "Rating distribution across branches",
        "Sales per Hour",
        "Average sales of all lines of products",
        "Products Sales Count",
        "Product Total Sales",
        "Average rating of product line",
        "Product sales on the basis of gender",
        "Weater Report"
        ]
    if request.method == "POST":
        val_f = request.POST['first_select']
        val_s = request.POST['second_select']
    first(val_f)
    second(val_s)
    return render(request,"index.html", {"val_f": int(val_f), "val_s": int(val_s), "list": list})  

def first(request):
    def switch(request):
        if request == "1":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize=(14,5))
            plt.style.use('fivethirtyeight')
            a= sns.countplot(data=data , palette = 'Set3')
            a.set_xlabel(xlabel= "Gender",fontsize=18)
            a.set_ylabel(ylabel = "Gender count", fontsize = 18)
            a.set_title(label = "Gender Count in E-Commerce Platform", fontsize = 20)
            plt.savefig(os.path.join('employee/static', 'first')) 
            return 1
        elif request == "2":
            data=pd.read_csv("E-Commerce.csv")
            data.groupby(['Gender']). agg({'Total':'count'})
            plt.style.use('ggplot')
            plt.figure(figsize= (14,5))
            a = sns.countplot(x = "Customer type", data = data, palette = "dark")
            a.set_xlabel("Customer type", fontsize = 16)
            a.set_ylabel("Customer Count", fontsize = 16)
            a.set_title("Type of customers", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'first')) 
            return 1
        elif request == "3":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize=(14,5))
            plt.style.use('classic')
            a = sns.countplot(x = "Customer type", hue = "Branch", data = data, palette= "Set3")
            a.set_xlabel(xlabel = "Branches", fontsize = 16)
            a.set_ylabel(ylabel = "Customer Count", fontsize = 16)
            a.set_title(label = "Customer type in different branches", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'first')) 
            return 1
        elif request == "4":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize = (14,5))
            a = sns.countplot(x = "Payment", data = data, palette = "tab10")
            a.set_xlabel(xlabel = "Customer's Payment method", fontsize = 16)
            a.set_ylabel(ylabel = " Customer Count", fontsize = 16)
            a.set_title(label = "Payment Methods", fontsize= 25)
            plt.savefig(os.path.join('employee/static', 'first')) 
            return 1
        elif request == "5":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize = (14,5))
            plt.style.use('classic')
            a = sns.countplot(x="Payment", hue = "Branch", data = data, palette= "Set3")
            a.set_xlabel(xlabel = "Payment method", fontsize = 16)
            a.set_ylabel(ylabel = "Peple Count", fontsize = 16)
            a.set_title(label = "Payment Distribution of all branches", fontsize= 25)
            plt.savefig(os.path.join('employee/static', 'first')) 
            return 1
        elif request == "6":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize=(14,5)) 
            a = sns.boxplot(x="Branch", y = "Rating" ,data =data, palette= "hls")
            a.set_xlabel(xlabel = "Branches", fontsize = 16)
            a.set_ylabel(ylabel = "Rating distribution", fontsize = 16)
            a.set_title("Rating distribution across branches", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'first')) 
            return 1
        elif request == "7":
            data=pd.read_csv("E-Commerce.csv")
            data["Time"]= pd.to_datetime(data["Time"])
            data["Hour"]= (data["Time"]).dt.hour
            plt.figure(figsize=(14,5))
            plt.style.use('classic')
            SalesTime = sns.lineplot(x="Hour", y ="Quantity", data = data).set_title("Sales per Hour")
            plt.savefig(os.path.join('employee/static', 'first')) 
            return 1
        elif request == "8":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize=(14,5))
            plt.style.use('classic')
            a = sns.boxenplot(x = "Quantity", y = "Product line", data = data)
            a.set_xlabel(xlabel = "Qunatity Sales",fontsize = 16)
            a.set_ylabel(ylabel = "Product Line", fontsize = 16)
            a.set_title(label = "Average sales of all lines of products", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'first')) 
            return 1
        elif request == "9":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize=(14,5))
            plt.style.use('classic')
            a = sns.countplot(y='Product line', data=data, order = data['Product line'].value_counts().index)
            a.set_xlabel(xlabel = "Sales count", fontsize = 16)
            a.set_ylabel(ylabel= "Product Line", fontsize = 16)
            a.set_title(label = "Products Sales Count", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'first')) 
            return 1
        elif request == "10":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize=(14,5))
            plt.style.use('classic')
            a = sns.boxenplot(y= "Product line", x= "Total", data = data)
            a.set_xlabel(xlabel = "Total sales", fontsize = 16)
            a.set_ylabel(ylabel = "Product Line", fontsize = 16)
            a.set_title(label = " Product Total Sales", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'first')) 
            return 1
        elif request == "11":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize = (14,5))
            plt.style.use('classic')
            a = sns.boxenplot(y = "Product line", x = "Rating", data = data)
            a.set_xlabel("Rating", fontsize = 16)
            a.set_ylabel("Product line", fontsize = 16)
            a.set_title("Average rating of product line", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'first')) 
            return 1
        elif request == "12":
            data=pd.read_csv("E-Commerce.csv")
            plt.style.use('classic')
            plt.figure(figsize = (14,5))
            a= sns.stripplot(y= "Product line", x = "Total", hue = "Gender", data = data)
            a.set_xlabel(xlabel = " Total sales of products")
            a.set_ylabel(ylabel = "Product Line")
            a.set_title(label = "Product sales on the basis of gender")
            plt.savefig(os.path.join('employee/static', 'first')) 
            return 1
    print(switch(request)) 

def second(request):
    def switch(request):
        if request == "1":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize=(14,5))
            plt.style.use('fivethirtyeight')
            a= sns.countplot(data=data , palette = 'Set3')
            a.set_xlabel(xlabel= "Gender",fontsize=18)
            a.set_ylabel(ylabel = "Gender count", fontsize = 18)
            a.set_title(label = "Gender Count in E-Commerce Platform", fontsize = 20)
            plt.savefig(os.path.join('employee/static', 'second')) 
            return 1
        elif request == "2":
            data=pd.read_csv("E-Commerce.csv")
            data.groupby(['Gender']). agg({'Total':'count'})
            plt.style.use('ggplot')
            plt.figure(figsize= (14,5))
            a = sns.countplot(x = "Customer type", data = data, palette = "dark")
            a.set_xlabel("Customer type", fontsize = 16)
            a.set_ylabel("Customer Count", fontsize = 16)
            a.set_title("Type of customers", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'second')) 
            return 1
        elif request == "3":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize=(14,5))
            plt.style.use('classic')
            a = sns.countplot(x = "Customer type", hue = "Branch", data = data, palette= "Set3")
            a.set_xlabel(xlabel = "Branches", fontsize = 16)
            a.set_ylabel(ylabel = "Customer Count", fontsize = 16)
            a.set_title(label = "Customer type in different branches", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'second')) 
            return 1
        elif request == "4":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize = (14,5))
            a = sns.countplot(x = "Payment", data = data, palette = "tab10")
            a.set_xlabel(xlabel = "Customer's Payment method", fontsize = 16)
            a.set_ylabel(ylabel = " Customer Count", fontsize = 16)
            a.set_title(label = "Payment Methods", fontsize= 25)
            plt.savefig(os.path.join('employee/static', 'second')) 
            return 1
        elif request == "5":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize = (14,5))
            plt.style.use('classic')
            a = sns.countplot(x="Payment", hue = "Branch", data = data, palette= "Set3")
            a.set_xlabel(xlabel = "Payment method", fontsize = 16)
            a.set_ylabel(ylabel = "Peple Count", fontsize = 16)
            a.set_title(label = "Payment Distribution of all branches", fontsize= 25)
            plt.savefig(os.path.join('employee/static', 'second')) 
            return 1
        elif request == "6":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize=(14,5)) 
            a = sns.boxplot(x="Branch", y = "Rating" ,data =data, palette= "hls")
            a.set_xlabel(xlabel = "Branches", fontsize = 16)
            a.set_ylabel(ylabel = "Rating distribution", fontsize = 16)
            a.set_title("Rating distribution across branches", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'second')) 
            return 1
        elif request == "7":
            data=pd.read_csv("E-Commerce.csv")
            data["Time"]= pd.to_datetime(data["Time"])
            data["Hour"]= (data["Time"]).dt.hour
            plt.figure(figsize=(14,5))
            plt.style.use('classic')
            SalesTime = sns.lineplot(x="Hour", y ="Quantity", data = data).set_title("Sales per Hour")
            plt.savefig(os.path.join('employee/static', 'second')) 
            return 1
        elif request == "8":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize=(14,5))
            plt.style.use('classic')
            a = sns.boxenplot(x = "Quantity", y = "Product line", data = data)
            a.set_xlabel(xlabel = "Qunatity Sales",fontsize = 16)
            a.set_ylabel(ylabel = "Product Line", fontsize = 16)
            a.set_title(label = "Average sales of all lines of products", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'second')) 
            return 1
        elif request == "9":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize=(14,5))
            plt.style.use('classic')
            a = sns.countplot(y='Product line', data=data, order = data['Product line'].value_counts().index)
            a.set_xlabel(xlabel = "Sales count", fontsize = 16)
            a.set_ylabel(ylabel= "Product Line", fontsize = 16)
            a.set_title(label = "Products Sales Count", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'second')) 
            return 1
        elif request == "10":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize=(14,5))
            plt.style.use('classic')
            a = sns.boxenplot(y= "Product line", x= "Total", data = data)
            a.set_xlabel(xlabel = "Total sales", fontsize = 16)
            a.set_ylabel(ylabel = "Product Line", fontsize = 16)
            a.set_title(label = " Product Total Sales", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'second')) 
            return 1
        elif request == "11":
            data=pd.read_csv("E-Commerce.csv")
            plt.figure(figsize = (14,5))
            plt.style.use('classic')
            a = sns.boxenplot(y = "Product line", x = "Rating", data = data)
            a.set_xlabel("Rating", fontsize = 16)
            a.set_ylabel("Product line", fontsize = 16)
            a.set_title("Average rating of product line", fontsize = 25)
            plt.savefig(os.path.join('employee/static', 'second')) 
            return 1
        elif request == "12":
            data=pd.read_csv("E-Commerce.csv")
            plt.style.use('classic')
            plt.figure(figsize = (14,5))
            a= sns.stripplot(y= "Product line", x = "Total", hue = "Gender", data = data)
            a.set_xlabel(xlabel = " Total sales of products")
            a.set_ylabel(ylabel = "Product Line")
            a.set_title(label = "Product sales on the basis of gender")
            plt.savefig(os.path.join('employee/static', 'second')) 
            return 1
    print(switch(request)) 

