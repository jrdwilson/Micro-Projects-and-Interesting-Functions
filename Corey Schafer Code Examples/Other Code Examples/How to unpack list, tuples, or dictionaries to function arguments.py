# Source: https://thispointer.com/python-how-to-unpack-list-tuple-or-dictionary-to-function-arguments-using/

def updateStudentDetail(name, phone, address):
    print("**********************")
    print("Student Name : ", name)
    print("Student phone : ", phone)
    print("Student address : ", address)
def calculateAverage(*args):
    ''' Function that accept variable length arguments '''
    num = len(args)
    if num == 0:
        return 0;
    sumOfNumbers = 0
    for elem in args:
        sumOfNumbers += elem
    return sumOfNumbers /  num  
      
def updateDetails(**kwargs):
    ''' Function that accept variable length key value pairs '''
    print("**********************")
    if 'name' in kwargs :
        print("Student Name : ", kwargs['name'])
    if 'phone' in kwargs :
        print("Student phone : ", kwargs['phone'])
    if 'address' in kwargs :
        print("Student address : ", kwargs['address'])        
        
    
                
if __name__ == '__main__':
    
    updateStudentDetail("Riti", "3343" , "Delhi")
    print("****** Unpack a List to Function Arguments ******")
    
    details = ["Riti", "3343" , "Delhi"]
    
    updateStudentDetail(details[0], details[1] , details[1])
    
    # Auto unpack elements in list to function arguments with *
    updateStudentDetail(*details)
    
    print("****** Unpack a tuple to Function Arguments ******")
    
    details = ("Riti", "3343" , "Delhi")
    
    # Auto unpack elements in tuple to function arguments with *
    updateStudentDetail(*details)
    
    print("****** Unpack Lists of different size to Function Arguments ******")
    
    list1 = [1,2,3,4,5,6,7,8]
    list2 = [1,2,3,4,5]
    list3 = [1,2,3]
    
    avg = calculateAverage( *list1)
    print("Average = " , avg)
    
    avg = calculateAverage(*list2)
    print("Average = " , avg)
    
    avg = calculateAverage(*list3)
    print("Average = " , avg)
    print("****** Unpack a dictionary to Function Arguments ******")
    
    details = {
        'name' : 'Sam' ,
        'phone' : '112' ,
        'address' : 'London' 
        }
    
    # Auto unpack dictionary to function arguments with **
    updateStudentDetail(**details)
    print("****** Unpack a different size dictionaries to Function Arguments ******")
    
    details = {
    'name' : 'Sam' ,
    'phone' : '112' 
    }
    # Auto unpack dictionary to function arguments with **
    updateDetails(**details)
    
    details = {
    'name' : 'Sam' ,
    'section' : 'A' ,
    'address' : 'London' ,
    'phone' : '112' 
    }
    
    # Auto unpack dictionary to function arguments with **
    updateDetails(**details)