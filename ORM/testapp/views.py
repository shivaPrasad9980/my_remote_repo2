from django.shortcuts import render
from . models import Employee
# case insensitive
from django.db.models.functions import Lower

# Create your views here.
def employee_view(request):
    # del1 = Employee.objects.get(pk = 6)
    # del1.delete()

    #sorting 
    emp = Employee.objects.all().order_by('esal') #ascending order
    emp = Employee.objects.all().order_by('-esal') #descending
    emp = Employee.objects.all().order_by('-esal')[0] #highest salaried person
    emp = Employee.objects.all().order_by('-esal')[1] # second higest salaried person
    # case insensitive
    # e = Employee(eno = 200,ename='applamma',esal=60000,eadd='nirmal')
    # e.save()
    emp =  Employee.objects.all().order_by(Lower('ename'))
    
    #union 
    q1 = Employee.objects.filter(esal__lt = 15000)
    q2 = Employee.objects.filter(ename__startswith = "J")
    emp = q1.union(q2)

    return render(request,'home.html',{'emp':emp})

from django.db.models  import Avg,Max,Min,Count,Sum
def aggregate_view(request):
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal')),
    min = Employee.objects.all().aggregate(Min('esal')),
    sum = Employee.objects.all().aggregate(Sum('esal')),
    count = Employee.objects.all().aggregate(Count('esal'))
    

    # my_dict = {'avg':avg}#output comes like this ('Average Salary : {'esal__avg': 15045.190476190477}')
    my_dict = {'avg':avg['esal__avg'],'max':max[0]['esal__max'],'min':min[0]['esal__min'],'sum':sum[0]['esal__sum'],'count':count['esal__count']}
    #=======================================================================>
        #adding a record 
        # e = Employee(eno = 20,ename='nani',esal=50000,eadd='adhfkd')
        # e.save()
        # emp = Employee.objects.all()
            #adding multple records at a time
        #--------------------------------------------------------------------->
    
            # emp = Employee.objects.bulk_create([Employee(eno = 100,ename='nani1',esal=50001,eadd='kjlk'),Employee(eno = 101,ename='nani2',esal=50002,eadd='lkjokhj'),
            #                                     Employee(eno = 102,ename='nani3',esal=50003,eadd='sdlkfj')])
            # emp.save()
        #---------------------------------------------------------------------->
    #=======================================================================>

    return render(request,'home.html',my_dict,{'del1':del1}) 