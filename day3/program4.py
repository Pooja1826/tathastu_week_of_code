def duplicate(List) :
    duplicateList = []
    for x in List :
        if x not in duplicateList:
            duplicateList.append(x)
    return duplicateList
size = int(input("Enter the no of element you want to add in list: "))
print("Enter the elment in list one by one")
List = []
for i in range(size):
    List.append(input())
print("List after removing the duplicate is:",duplicate(List))    
