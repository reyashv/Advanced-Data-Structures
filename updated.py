import shutil
from PIL import Image
from PIL.ExifTags import TAGS
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
class AVL_Tree(object):
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        list1=[]
        if not root:
            return
        list1.append(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
        for i in list1:
            with open("C:\\Users\\91994\\Documents\\psg\\ads\\recent.txt",'w') as f:
                f.write(i)
            image=Image.open(i)
            image.show()
jan = AVL_Tree()
feb = AVL_Tree()
mar = AVL_Tree()
apr = AVL_Tree()
may = AVL_Tree()
june = AVL_Tree()
july = AVL_Tree()
aug = AVL_Tree()
sept = AVL_Tree()
octo = AVL_Tree()
nov = AVL_Tree()
dec = AVL_Tree()
year0 = AVL_Tree()
year1 = AVL_Tree()
year2 = AVL_Tree()
year3 = AVL_Tree()
year4 = AVL_Tree()
year5 = AVL_Tree()
root1 = None
root2 = None
root3 = None
root4 = None
root5 = None
root6 = None
root7 = None
root8 = None
root9 = None
root10 = None
root11 = None
root12 = None
root2014 = None
root2018 = None
root2019 = None
root2020 = None
root2021 = None
root2022 = None

data1=[]
list2=[]
my_file = open("C:\\Users\\91994\\Documents\\psg\\ads\\pictures.txt", "r")
data = my_file.read()
data1 = data.split("\n")
#print(data1)
my_file.close()
list1=[]
for i in data1:
    image=Image.open(i)
    exifdata = image.getexif()
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if(tag=='DateTime'):
            if isinstance(data, bytes):
                data = data.decode()
            list1.append(f"{tag:25}: {data}")
#print(list1)
for i in list1:
    a=i.split(": ")
    list2.append(a[1])
#print(list2)

#MONTH
list3=[]
y=[]
for i in list2:
    b=i.split(":")
    list3.append(b[1])
#print(list3)
c=0
for i in list2:
    for j in data1:
        #print(j)
        image=Image.open(j)
        exifdata = image.getexif()
        if i in exifdata.values():
            if(list3[c]=='01'):
                root1=jan.insert(root1,j)
                destination="C:\\Users\\91994\\Documents\\psg\\ads\\January"
                shutil.copy(j,destination)
            if(list3[c]=='02'):
                root2=feb.insert(root2,j)
                destination="C:\\Users\\91994\\Documents\\psg\\ads\\February"
                shutil.copy(j,destination)
            if(list3[c]=='03'):
                root3=mar.insert(root3,j)
                destination="C:\\Users\\91994\\Documents\\psg\\ads\\March"
                shutil.copy(j,destination)
            if(list3[c]=='04'):
                root4=apr.insert(root4,j)
                destination="C:\\Users\\91994\\Documents\\psg\\ads\\April"
                shutil.copy(j,destination)
            if(list3[c]=='05'):
                root5=may.insert(root5,j)
                destination="C:\\Users\\91994\\Documents\\psg\\ads\\May"
                shutil.copy(j,destination)
            if(list3[c]=='06'):
                root6=june.insert(root6,j) 
                destination="C:\\Users\\91994\\Documents\\psg\\ads\\June"
                shutil.copy(j,destination)
            if(list3[c]=='07'):
                root7=july.insert(root7,j)
                destination="C:\\Users\\91994\\Documents\\psg\\ads\\July"
                shutil.copy(j,destination)
            if(list3[c]=='08'):
                root8=aug.insert(root8,j)
                destination="C:\\Users\\91994\\Documents\\psg\\ads\\August"
                shutil.copy(j,destination)
            if(list3[c]=='09'):
                root9=sept.insert(root9,j)
                destination="C:\\Users\\91994\\Documents\\psg\\ads\\September"
                shutil.copy(j,destination)
            if(list3[c]=='10'):
                root10=octo.insert(root10,j)
                destination="C:\\Users\\91994\\Documents\\psg\\ads\\October"
                shutil.copy(j,destination)
            if(list3[c]=='11'):
                root11=nov.insert(root11,j)
                destination="C:\\Users\\91994\\Documents\\psg\\ads\\November"
                shutil.copy(j,destination)
            if(list3[c]=='12'):
                root12=dec.insert(root12,j)
                destination="C:\\Users\\91994\\Documents\\psg\\ads\\December"
                shutil.copy(j,destination)
            c=c+1  
print("WELCOME TO PHOTO DIRECTORY!")
print("ENTER WHICH ONE YOU WANT TO DO:")
print()
print("1.VIEW PHOTOS ACCORDING TO MONTH.\n2.VIEW PHOTOS ACCORDING TO YEAR. \n3.VIEW PHOTOS ACCORDING TO DATE. \n4.VIEW RECENTLY VIEWED PHOTO. \n5.CREATE NEW FOLDER MONTHWISE. \n6.VIEW OLDEST PIC. \n7.VIEW LATEST PIC. \n8.EXIT")
ch=int(input("Enter your choice(1-8):"))
if(ch==1):
    a=int(input("Enter Month Number:"))
    if(a==1):
         jan.preOrder(root1)
    if(a==2):
         feb.preOrder(root2)
    if(a==3):
         mar.preOrder(root3)
    if(a==4):
       apr.preOrder(root4)
    if(a==5):
       may.preOrder(root5)
    if(a==6):
       june.preOrder(root6)
    if(a==7):
       july.preOrder(root7)
    if(a==8):
       aug.preOrder(root8)
    if(a==9):
       sept.preOrder(root9)
    if(a==10):
       octo.preOrder(root10)
    if(a==11):
       nov.preOrder(root11)
    if(a==12):
       dec.preOrder(root12)

if(ch==2):
    list4=[]
    for i in list2:
        d=i.split(":")
        list4.append(d[0])
    cy=0
    for i in list2:
        for j in data1:
            image=Image.open(j)
            exifdata=image.getexif()
            if i in exifdata.values():
                if(list4[cy]=='2014'):
                   root2014=year0.insert(root2014,j)
                if(list4[cy]=='2018'):
                   root2018=year1.insert(root2018,j)
                if(list4[cy]=='2019'):
                    root2019=year2.insert(root2019,j)
                if(list4[cy]=='2020'):
                    root2020=year3.insert(root2020,j)
                if(list4[cy]=='2021'):
                    root2021=year4.insert(root2021,j)
                if(list4[cy]=='2022'):
                    root2022=year5.insert(root2022,j)
                cy=cy+1  
     
    y=int(input("Enter year number:"))
    if(y==2018):
        year1.preOrder(root2018)
    if(y==2019):
        year2.preOrder(root2019)
    if(y==2020):
        year3.preOrder(root2020)
    if(y==2021):
        year4.preOrder(root2021)
    if(y==2022):
        year5.preOrder(root2022)

if(ch==3):
    list5=[]
    for i in list2:
        e=i.split(" ")
        list5.append(e[0])
    g=input("Enter date of pic you want to display in yyyy:mm:dd format ")
    if g in list5:
        p=list5.index(g)
        q=data1[p]
        with open("C:\\Users\\91994\\Documents\\psg\\ads\\recent.txt",'w') as f:
            f.write(q)
        image=Image.open(q)
        image.show()
    else:
        print("No pictures of that date :(")
         
if(ch==4):
    print("PRINTING RECENTLY VIEWED PICTURE:")
    with open("C:\\Users\\91994\\Documents\\psg\\ads\\recent.txt",'r') as f:
        image=Image.open(f.read())
        image.show()

if(ch==5):
    print("ALL PICTURES HAVE NOW BEEN PUT INTO FOLDERS!!")

if(ch==6):
    list2.sort()
    print("OLDEST PICTURE:")
    for j in data1:
        image=Image.open(j)
        exifdata = image.getexif()
        if list2[0] in exifdata.values():
            with open("C:\\Users\\91994\\Documents\\psg\\ads\\recent.txt",'w') as f:
                f.write(j)
            image.show()

if(ch==7):
    list2.sort()
    print("LATEST PICTURE")
    for j in data1:
        image=Image.open(j)
        exifdata = image.getexif()
        if list2[-1] in exifdata.values():
            with open("C:\\Users\\91994\\Documents\\psg\\ads\\recent.txt",'w') as f:
                f.write(j)
            image.show()

if(ch==8):
    exit