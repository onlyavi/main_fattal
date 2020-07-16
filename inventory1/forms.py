from django import forms
from .models import Stock, SupplierInformation, StockTemp, TemplateList
import io
import csv
from django.contrib.auth.models import User
from history0.models import StockHistory

class StockCreateForm(forms.ModelForm):
    class Meta:
        model=Stock
        
        #The fields I want to use
        fields=['category_name', 'item_fattal_code', 'item_name', 'quantity_item', 'item_unit_kind', 'description']
    
    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        category_name =self.cleaned_data.get('category_name')
        item_fattal_code =self.cleaned_data.get('item_fattal_code')
        if (not category_name) and (not item_name) and (not item_fattal_code) :
            raise forms.ValidationError('You must fill at least one field ITEM CODE or ITEM NAME ')
        #instance = Stock.objects.get(id)
        #print (instance.item_name)
        # if item_name != instance.item_name:
        #     if item_name:                
        for instance in Stock.objects.all():
            if (instance.item_name == item_name):
                raise forms.ValidationError(item_name +' Already exist')
            
        return item_name
    def clean_item_fattal_code(self):
        item_name = self.cleaned_data.get('item_name')
        category_name =self.cleaned_data.get('category_name')
        item_fattal_code =self.cleaned_data.get('item_fattal_code')
        if (not category_name) and (not item_name) and (not item_fattal_code):
            raise forms.ValidationError('You must fill at least one field ITEM CODE or ITEM NAME ')
    
       
    #     if item_fattal_code:
        for instance in Stock.objects.all():    
            if (instance.item_fattal_code == item_fattal_code) and (int(instance.item_fattal_code) < 990000):
                raise forms.ValidationError('item code '+ str(item_fattal_code) +' Already exist')
        return item_fattal_code

class TemplateListForm(forms.ModelForm):
    class Meta:
        model=TemplateList
        
        #The fields I want to use
        fields=['alchol_kind']
    

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()
#     #file_data=request.FILES['file']
#     if  not file_data.name.endswith('.xlsx'):
#         messages.error(request, "This is not a valid file format (only csv or excel xlsx")
#         raise ValidationError('You must fill at le')
#     elif file_data.name.endswith('.xlsx'):
#         wb = openpyxl.load_workbook(file_data)

#         # getting a particular sheet by name out of many she ets
#         worksheet = wb["Sheet1"]
#         print(worksheet)

#         # getting all sheets
#         sheets = wb.sheetnames
#         print(sheets)

#         # getting active sheet
#         active_sheet = wb.active
#         print(active_sheet)
        
#         excel_data = list()
#         print (worksheet.iter_rows())
#         print ("****** rows: ", worksheet.max_row) 
#         print ("****** col: ", worksheet.max_column) 
        

#         #print("number of columns: ", worksheet.iter_cols())       
        
#         # _, created = Stock.objects.update_or_create(
#         #             item_fattal_code=worksheet["A2"].value,
#         #             item_name= worksheet["B2"].value,

#         #     )
       
#         # iterating over the rows and
#         # getting value from each cell in row
#         row_counter=0
#         first_run = True
#         for  row in worksheet.iter_rows(min_row=1):
#             row_data = list()
#             print ("top=",row_counter)
        
#             for cell in row:
#                 row_data.append(str(cell.value))
                

#             excel_data.append(row_data)
#             # print(excel_data)
#             # print(len(excel_data))
#             # print(excel_data[0][0])
#             # #print (excel_data[row_counter])
#             # print ("****")
#             # print (len(row_data))    
#             # print (type(excel_data))
#             # print (len(excel_data))
#             # print (row_data[0])
#             # print (row_data[1])
#             # print("************")
            
#             #item_fattal_code_check = column[0]
#             #clean_excel_item_fattal_code(item_fattal_code_check,skip)

#             #item_name_check= column[1]
#             #clean_excel_item_name(item_name_check,skip)
            
#             #sup_name= column[2]
#             #clean_excel_supplliers_name(sup_name,sskip)
#             #print ("row counter: ", row_counter)
#             skip=False
#             sskip=False
#             print (row_counter)
#             print (row_data)
#             for nonedata in range(row_counter):
#                 if row_data[nonedata] =='None':
#                     row_data[nonedata]=''
#                     print ("found none")
#             #before clean_excel_item_fattal_code 0   
#             if not row_data[row_counter] =='None' and (first_run == False) :
#                 #before clean_excel_item_fattal_code 
#                 if row_data[row_counter].isnumeric:
#                     item_fattal_code_check = row_data[row_counter]
#                     clean_excel_item_fattal_code(item_fattal_code_check,skip)
#                     print (skip, " num ", row_data[row_counter], "=item fattal code ", row_counter, "=row counter" )

#                 #before clean_excel_item_name  1
#                 if row_data[row_counter + 1].isalpha:
#                     item_name_check= row_data[row_counter+1]
#                     print ("before calling function= ", skip, " item name= ", item_name_check)
#                     clean_excel_item_name(item_name_check,skip)
#                     print (skip, " after fiunction ", row_data[row_counter], "=item name ", row_counter, "=row counter" )
#                 #before clean_excel_sub_category_name   2            
#                 # if (row_data[row_counter + 2]).isalnum:
#                 #     sub_category_name= row_data[row_counter+2]
#                 #     clean_excel_sub_category_name(sub_category_name,skip)
#                 #     print (skip, " sub+_category ", row_data[row_counter+2], "=sub category ", row_counter, "=row counter" )   
#                 #     print (skip, " alpha")
                
#                 # #before suplier name   3
#                 # if (row_data[row_counter + 3].isalnum:
#                 #     supplliers_name= row_data[row_counter+3]
#                 #     clean_excel_supplliers_name(supplliers_namek,skip)
#                 #     #print (skip, " alpha ", row_data[row_counter], "=item name ", row_counter, "=row counter" )   
#                 #     #print (skip, " alpha")

#                 # #before suppliers_fattal_code  4 - no need to be clean. can be duplicate in same row input
#                 # if (row_data[row_counter + 4].isalnum:
#                 #     suppliers_fattal_code= row_data[row_counter+3]
#                 #     #clean_excel_suppliers_fattal_code(suppliers_fattal_code,skip)
#                 #     #print (skip, " alpha ", row_data[row_counter], "=item name ", row_counter, "=row counter" )   
#                 #     #print (skip, " alpha")
                
                
                
#                 if skip == False:
#                     print(type(row_data[row_counter]), " ", row_data[row_counter])
#                     item_fattal_code_converted = int(row_data[row_counter])
#                     _, created = Stock.objects.update_or_create(
#                         item_fattal_code=item_fattal_code_converted,
#                         item_name= row_data[row_counter+1],
#                         sub_category_name=row_data[row_counter+2],
#                         suppliers_fattal_code= row_data[row_counter+4],
#                         category_name='',
#                         description='',
                        

#                     )

#                 if sskip == False:
#                     _, created = SupplierInformation.objects.update_or_create(
#                         suppliers_name=row_data[row_counter+3]
 
#                    ) 
#                 if skip == True:
#                     skip = False
#                 if sskip == True:
#                     sskip = False
#             first_run = False
#             row_counter = 0            
            


#         #print(excel_data[1])
#         #print (excel_data[1][4])
#         # reading a cell
#         #print(worksheet["A1"].value)

#     #return redirect ('/')
#         #return render(request, 'excel_upload1.html', {"excel_data":excel_data})
 
    

    
        
class StockSearchForm(forms.ModelForm):
    class Meta:
        model=Stock
        #The fields I want to use
        fields=['category_name','item_name', 'item_fattal_code']
    
    

      
class StockFullSearchForm(forms.ModelForm):
    class Meta:
        model=Stock
        #The fields I want to use
        
        fields=['category_name','item_name','quantity_min','quantity_max','item_fattal_code_begin', 'item_fattal_code_end', 'description']
   
   
    # def clean_item_name(self):
    #     item_name = self.cleaned_data.get('item_name')
    #     if (not item_name):
    #         raise forms.ValidationError('This field is required')
    #     # for instance in Stock.objects.all():
    #     #     if instance.category == category:
    #     #         raise forms.ValidationError(category +' Already exist')
    
    #     return item_name 

   
    
        
class StockUpdateForm(forms.ModelForm):
    class Meta:
        model=Stock
        
        fields=['category_name', 'item_fattal_code', 'item_name', 'quantity_item', 'item_unit_kind','description']
  
  
    # def clean_item_name(self):
    #     item_name = self.cleaned_data.get('item_name')
    #     category_name =self.cleaned_data.get('category_name')
    #     item_fattal_code =self.cleaned_data.get('item_fattal_code')
    #     item_code =self.cleaned_data.get(id)
    #     zz= Stock.objects.values('item_name')
    #     if (not category_name) and (not item_name) and (not item_fattal_code) :
    #         raise forms.ValidationError('You must fill at least one field ITEM CODE or ITEM NAME ')
        
       
        
    #     if item_name and item_fattal_code:                
    #         for instance in Stock.objects.all():
    #             if (instance.item_name == item_name) and (instance.) :
    #                 raise forms.ValidationError(item_name +' Already exist')
    #  else:
    #         if item_name:                
    #             for instance in Stock.objects.all():
    #                 if (instance.item_name == item_name):
    #                     raise forms.ValidationError(item_name +' Already exist')
    #         # 
    #     return item_name
    # 
    # # def clean_item_fattal_code(self):
    #     # item_name = self.cleaned_data.get('item_name')
    #     # category_name =self.cleaned_data.get('category_name')
    #     # item_fattal_code =self.cleaned_data.get('item_fattal_code')
    #     # if (not category_name) and (not item_name) and (not item_fattal_code):
    #         # raise forms.ValidationError('You must fill at least one field ITEM CODE or ITEM NAME ')
    #     # else:
    # #    
    #         # if item_fattal_code:
    #             # for instance in Stock.objects.all():    
    #                 # if (instance.item_fattal_code == item_fattal_code) and (int(instance.item_fattal_code) < 990000):
    #                     # raise forms.ValidationError('item code '+ str(item_fattal_code )+' Already exist')
    #     # return item_fattal_code   


class import_csv(forms.Form):
    file_data= forms.FileField()

    def process_csv_data(self):
        csv_file= io.TextIOWrapper( self.cleaned_data('file_data').file)
        csv_data= csv.DictReader(csv_file)
        print (csv_data)

class import_excel(forms.Form):
    file_data= forms.FileField()
    print ("in class import_excel")
    print (file_data)

   
class StockIssueForm2(forms.ModelForm):
    class Meta:
        model=StockTemp
        #his_model=StockHistory
        # fields=[ 'item_fattal_code', 'item_name', 'issue_to_transfer', 'issue_quantity_transfer', 'item_unit_kind','description']
        # fieldsh=['transfer_towhomh']
        fields=['item_unit_kind_issue']

class StockIssueForm(forms.ModelForm):
    class Meta:
        model=StockTemp
        #his_model=StockHistory
        # fields=[ 'item_fattal_code', 'item_name', 'issue_to_transfer', 'issue_quantity_transfer', 'item_unit_kind','description']
        # fieldsh=['transfer_towhomh']
        fields=[ 'item_fattal_code_issue', 'item_name_issue']


    def clean_item_fattal_code_issue(self):
        print ("in clean def")
       
        item_name_issue = self.cleaned_data.get('item_name_issue')
        item_fattal_code_issue =self.cleaned_data.get('item_fattal_code_issue')
        
        
        if (not item_name_issue) and (not item_fattal_code_issue):
            print ("none entered")
            raise forms.ValidationError('You must fill at least one field ITEM CODE or ITEM NAME ')
        

        update_the_form=False        
        for instance in Stock.objects.all():  
            #print ("item_fattal_code_issue= ",item_fattal_code_issue )
            #print ("instance.item_fattal_code=", instance.item_fattal_code)  
            if (str(item_fattal_code_issue) == str(instance.item_fattal_code)):
                print ("found in orginal Stock DB")
                for x in StockTemp.objects.all():
                    if str(item_fattal_code_issue) == str(x.item_fattal_code_issue):
                        StockTemp.formisok=False
                        print ("found in new list  issue db:",StockTemp.formisok)
                        raise forms.ValidationError(str(item_fattal_code_issue) +' Already exist')
                   
                
                #item_fattal_code_issue = instance.item_fattal_code
                #StockTemp.item_name_issue = instance.item_name
               
             #   print ("$$ in IF item_fattal_code_issue=== ",item_fattal_code_issue )
                print (instance.item_name)
                StockTemp.formisok=True
                StockTemp.item_fattal_code_issue= instance.item_fattal_code
                StockTemp.item_name_issue= instance.item_name
                StockTemp.item_unit_kind_issue= instance.item_unit_kind
                



                return item_fattal_code_issue
        
    
        
        return item_fattal_code_issue
    
    


def cleanme(x):
    print(x)
    x+=1
    return x
        


        

class SuppliersCreateForm(forms.ModelForm):
    class Meta:
        model=SupplierInformation
        #The fields I want to use
     #   fields=['suppliers_name','supplier_phone_number','supplier_sale_leader_name','supplier_sale_leader_phone','suppliers_driver_info']
        fields=['suppliers_name']  

