from .models import *
from django.shortcuts import render, render
#from .forms import StockCreateForm, SuppliersCreateForm, StockSearchForm,StockUpdateForm, StockFullSearchForm, import_csv, import_excel, StockIssueForm,cleanme,StockIssueForm2



def delete_checked_items(*items_id):
    print ("in delete func")
    print ("items=",items_id)
    #queryset = StockTemp.objects.all()   
    for i in items_id:
        print ("in i loop",i)
        for instance in StockTemp.objects.all():
            print (instance.item_name_issue, "    in instance loop ", instance.id)
            print ('i=',i, " ", "instance=",instance)
            if int(i)==int(instance.id):
                print ("equal")
                instance.delete()
           

    
    
    
    
    return

def update_form_def(update_form,update_db, quantity_update0, quantity_kind0):
    update_form=update_form
    update_db=update_db
    quantity_update=quantity_update0
    quantity_kind=quantity_kind0
    the_choices={}
    tuple_convert = StockTemp.item_unit_kind_choice_issue
    
    for a,b in tuple_convert:
        the_choices.setdefault(a,[]).append(b)

    print ("dictionart \n", the_choices)


    #print ("in function q+q= ",quantity_kind, "\n", quantity_update)
    # print ("***in func ")
    #print (update_form," -update form  update db=",update_db)
    # if update_db == True:
    #     print ("db")
    # if update_form == True:
    #     print ("form")
    # for z in StockTemp.objects.all():
    #     print (z.issue_quantity_transfer, end=' before@@')
    #     print (z.item_unit_kind_issue)




    #******     start the update stock temp and check 
    print (quantity_kind, "before loop checkkeeeeee")
    i=0
    for instance in StockTemp.objects.all():
        print (instance.item_unit_kind_issue, "-ins ",i, "    qu=",quantity_kind[i])
        if  instance.item_unit_kind_issue != "None" :
            print (quantity_kind[i], "    ", the_choices)
            for b in the_choices:
                print (b, "  q=", quantity_kind[i])
                if quantity_kind[i] == b:



                    print("the choice is ok")
                
                    instance.item_unit_kind_issue= (quantity_kind[i])
                    instance.save()
                    break
                else:
                    instance.item_unit_kind_issue = "None"
                    instance.save()


                    
                
        
        else:
            print ("the choice is NOT OK or no need to chasnge")
            instance.item_unit_kind_issue = "-----"
            instance.save()
            print ("")

        
        #print (quantity_update[i])
        if quantity_update[i] !='' and quantity_update[i]!="0":
            #print (quantity_update[i])
            
            #print(type(instance.issue_quantity_transfer) )
            instance.issue_quantity_transfer = int(quantity_update[i])
            instance.save()
        i+=1

   

    return
    

def clear_list(llist):
    print ("in clear list")
    leng= len(llist)
    print ("leng= ",leng)
    
    del llist[:]
       
          
      
    print ("llist= ", llist)
    return llist