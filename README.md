# หลักการทำงานของ MYWEBAPPMODEL

## 📕1. [DjangoApp](https://github.com/Lynnn01/MyWebappModel/tree/main/DjangoApp)

```sh
django-admin startproject [ชื่อ Project]
```

>**🔺 main folder ของ project โดยใช้คำสั่งดังกล่าวในการสร้าง project**

## 📕2. [env](https://github.com/Lynnn01/MyWebappModel/tree/main/env)

```sh
pyton -m vene env
```

>**🔺การจำลอง environment เพื่อใช้ในการทำงานภายใน project**

## 📕3. [requirments.txt](https://github.com/Lynnn01/MyWebappModel/blob/main/requirments.txt)

```py
django >= 3
```
>**🔺 การควบคุม Version ในการติดตั้ง django ภายใน environment โดยการใช้คำสั่งในการติดตั้ง ดังนี้**

```sh
pip install -r requirments.txt
```

## 📕4. [MainApp](https://github.com/Lynnn01/MyWebappModel/tree/main/MainApp)

```sh
python manage.py startapp [ชื่อ Projectapp]
```
>**🔺 สร้าง sub-folder ในการสร้าง ProjectApp ภายใน DjangoApp**

## 📕5. [template](https://github.com/Lynnn01/MyWebappModel/tree/main/templates)
>**❗️ folder สำหรับการกำหนดลักษณะของแต่ละ pages โดยจะมีการเรียกใช้จาก [views.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/views.py)**

>**🔻 ดังตัวอย่างของไฟล์ [index.html](https://github.com/Lynnn01/MyWebappModel/blob/main/templates/index.html)**

```css
{% extends 'base.html' %}
<!---->
{% block title %}
    หน้าเเรกของฉัน
{% endblock title %}
<!---->
{% block Content %}
{{message}}
<table class="table">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">ID</th>
        <th scope="col">PREFIX</th>
        <th scope="col">NAME</th>
        <th scope="col">LASTNAME</th>
        <th scope="col">PHONE</th>
      </tr>
      
      {% for student in students %}
      <tr>
        <th scope="row">{{ student.id }}</th>
        <td><a href="{% url 'details' student.id %}"> {{ student.std_id }}</a></td>
        <td>{{ student.prefix_str }}</td>
        <td>{{ student.name }}</td>
        <td>{{ student.lastname }}</td>
        <td>{{ student.phone }}</td>
      </tr>
      {% endfor %}

    </thead>
    <tbody>
      
    </tbody>
  </table>
{% endblock Content %}
```
>**🔺 จุดสังเกตที่เห็นได้ชัดคือมีการใช้ for loop ในการวนซ้ำเพื่อเรียกค่าของนักศึกษาทุกคนมาแสดง และมีการเชื่อม url และส่งค่า ID ไปยัง [details.html](https://github.com/Lynnn01/MyWebappModel/blob/main/templates/details.html) เพื่อแสดงข้อมูลแบบเฉพาะเจาะจง**

## 📕6. [views.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/views.py) 

>**❗️ พื้นที่สำหรับการ functions ต่างๆไปยัง ทั้งในส่วนของการเรียกใช้ [template](https://github.com/Lynnn01/MyWebappModel/tree/main/templates) และการสร้าง functions ต่างๆ เพื่อใช้ในการเรียกใช้งาน โดยจะมีการเรียกใช้จาก [urls.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/urls.py)**

```py
from django.shortcuts import render
from . import models

def Home(request):
    context = {}
    students = models.Student.objects.all().order_by("-id")

    for student in students:
        student.prefix_str = getModelChoice(student.prefix, models.prefix_choices)

    context["students"] = students

    return render(request, "index.html", context)

def About(request):
    return render(request, "about.html")

def Contact(request):
    return render(request, "contact.html")
```

>**🔺 functions ที่มีการเรียกใช้ style จาก [template](https://github.com/Lynnn01/MyWebappModel/tree/main/templates) แล้วจะมีใช้ return เพื่อส่งออกค่า ซึ่งในส่วนนี้จะมีการเรียกใช้งานจาก [urls.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/urls.py)**


>**🔻 StudentDetails เป็น function ที่จะถูกเรียกใช้จาก [urls.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/urls.py) ในส่วนแรก และมีการส่งค่าไปยัง [details.html](https://github.com/Lynnn01/MyWebappModel/blob/main/templates/details.html) เป็นส่วนต่อไป**

```py
def StudentDetails(request, id):
    context = {}
    students = models.Student.objects.filter(id=id)
    for student in students:
        student.prefix_str = getModelChoice(student.prefix, models.prefix_choices)
        context["student"] = student
    return render(request, "details.html", context)
```
>**🔺 จุดสังเกตุที่เห็นได้ชัดของ functions นี้คือมีการใช้ filter ในการค้นหาข้อมูลในส่วนของ ID และมีการใช้ functions getModelChoice เพื่อการเปลี่ยนค่า prefix จากตัวเลข เป็นตัวอักษร**

>**🔻 getModelChoice เป็น function เพื่อใช้ในการเปลี่ยนค่า prefix จากตัวเลข เป็นตัวอักษร ซึ่งค่าของ prefix นั้นจะถูกดึงข้อมูลมาจาก [model.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/models.py)**

```py
def getModelChoice(num, choices):
    for choice in choices:
        if choice[0] == num:
            return choice[1]
```
>**🔺 จุดสังเกตุที่เห็นได้ชัดของ function นี้คือมีการใช้ for loop ในการวนซ้ำ และใช้ if เพื่อเช็คข้อมูลของ prefix ที่เป็นตัวเลขทีละค่า จากนั้นจะมีการใช้ return เพื่อส่งข้อมูลของ prefix ที่เป็นตัวอักษรออกไป**

## 📕7. [model.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/models.py)
>**❗️ การสร้างตารางสำหรับการเก็บข้อมูลบนพื้นฐานของ db.sqlite3**

```py
from  django.db  import  models

prefix_choices  = (

(1, "นาย"),

(2, "นางสาว"),

(3, "นาง"),

)
```
>**🔺 prefix_choices จะมีการเก็บค่าข้อมูลในตารางแบบตัวเลขจาก pointer ที่ 0 แต่หลังจาก function getModelChoice มีการดึงค่าไปใช้ จะกระบวนการที่จะดึงค่าจาก pointer ที่ 1 มาใช้แทน**

```py
class  Student(models.Model):

	std_id  =  models.IntegerField()

	prefix  =  models.IntegerField(choices=prefix_choices, default=1)

	name  =  models.CharField(max_length=255)

	lastname  =  models.CharField(max_length=255)

	phone  =  models.CharField(max_length=15)

	address  =  models.TextField()


	class  Meta:

	verbose_name  =  "Student"

	verbose_name_plural  =  "Students"


	def  __str__(self):

	return  self.name


	def  get_absolute_url(self):

	return  reversed("Student_detail", kwargs={"pk": self.pk})
```
>**🔺 Clss Student เพื่อใช้เก็บข้อมูลเกี่ยวกับนักศึกษา**

```py
class Major(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Major"
        verbose_name_plural = "Majors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Major_detail", kwargs={"pk": self.pk})
```
>**🔺 Clss Major ใช้สำหรับเก็บข้อมูลคณะของนักศึกษา**

## 📕8. [urls.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/urls.py)

```py
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home, name='home'),
    path('about',views.About,   name='about'),
    path('contact',views.Contact,   name='contact'),
    path('details/<int:id>', views.StudentDetails, name='details'),
]
```
>**🔺 กำหนด path ของการเรียกใช้งานในแต่ละ page ซึ่งจะมีการดึงข้อมูลทั้งหมดจาก functions ใน [views.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/views.py) มาใช้งาน และแสดงออกมาทางหน้าจอ**
## 📕9. [admin.py](https://github.com/Lynnn01/MyWebappModel/blob/main/MainApp/admin.py)

```py
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("std_id", "prefix", "name", "lastname", "phone", "major")
    search_fields = list_display

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = list_display
```
>**🔺 การแสดงตารางข้อมูลใน admin โดยมีการแสดงแบบแถว และมีการค้นหา**

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

>**🔺 ใช้คำสั่ง makemigrations และ migrate เพื่อสร้างฐานข้อมูล แล้วจึงใช้คำสั่ง  createsuperuser เพื่อสร้าง admin user ในการเข้าถึงฐานข้อมูล**
>
>**❗️ หลังจากการสร้าง หรือปรับเปลี่ยนตารางสำหรับการเก็บข้อมูลใหม่ทุกครั้งๆ จำเป็นจะต้องใช้คำสั่งดังกล่าวเพื่อสร้างฐานข้อมูลใหม่ด้วยเช่นกัน**
## 📕10. การสั่ง Run server
![enter image description here](https://cdn.discordapp.com/attachments/1026853768505081868/1136316668583362671/2023-08-02_221604.png)

```sh
python manage.py runserver
```

>**🔺 สั่ง run server เพื่อใช้งาน**

![enter image description here](https://cdn.discordapp.com/attachments/1026853768505081868/1136315785229373550/2023-08-02_221228.png)

```py
http://127.0.0.1:8000/admin/
```

>**🔺 การเข้าถึง admin และใช้การ login ตาม createsuperuser ที่เราสร้างไว้**

![enter image description here](https://cdn.discordapp.com/attachments/1026853768505081868/1136316700049023137/2023-08-02_221516.png)
>**🔺 ตารางสำหรับการเก็บข้อมูลบนพื้นฐานของ db.sqlite3**

![enter image description here](https://cdn.discordapp.com/attachments/1026853768505081868/1136316685234753627/2023-08-02_221547.png)
>**🔺 การแสดงแบบแถว และการค้นหา**

## 💾 CREDIT
**[💻 YOUTUBE :   Phisan Sookkhee](https://www.youtube.com/watch?v=EC6k9KduQYU&list=PLUD6z42fSjQq785dtC6bl9BTSlO-_EjY9) ❗️**
