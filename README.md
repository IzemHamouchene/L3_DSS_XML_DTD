# TP 1 : Simple DB manipulation

In this exercise, you will write SQL queries that create a database, tables and insert simple Data.

Diagram : <br/>
![diagram](<assets/diagram.png>)

## Exercise 1 : Create the Database

Write the following SQL queries into _1_create_database.sql_
1. Create a Database named **UniversityDB**
2. Create Table named **teacher** with the following attribute
    * ID Type Integer (Primary Key) auto increment
    * FirstName NVARCHAR (30)
    * LastName NVARCHAR (30)
    * Phone INT
    * Email NVARCHAR (255)
3. Create Table named **student** with the following attribute
    * ID Type Integer (Primary Key) auto increment
    * FirstName NVARCHAR (30)
    * LastName NVARCHAR (30)
    * Phone INT
4. Create Table named **Cours** with the following attribute
    * ID Type Integer (Primary Key) auto increment
    * Name NVARCHAR (30)
5. Create Table named **CoursTeacher** with the following attribute
    * IDCoursTeacher Type Integer (Primary Key) auto increment
    * IdCour INT (FOREIGN KEY)
    * IdTeacher INT (FOREIGN KEY)
    * IdStudent INT (FOREIGN KEY)
    * DayWeek NVARCHAR(30) _should accept only these values : 'Sunday', 'Monday', 'Tuesday' , 'Wednesday' , 'Thursday'_
    * StartHour INT

## Exercise 2 : Insert Data

Write the following SQL queries into _2_insert_data.sql_
1. Insert two teachers
   * (1,sofian,family1,123,`s_f3@gmail.com`)
   * (2,yacin,family2,456,`y_f4@gmail.com`)
2. Insert two students
   * (1,mohamed,family3,123)
   * (2,youcef,family4,456)
3. Insert two cours
   * (1,MultiMedia)
   * (2,BDDA)
4. Insert coursTeacher
   * (1,1,1,Jeudi,8)
   * (1,1,2,Jeudi,8)
   * (2,2,1,Jeudi,9)
     
  Check the Actions tab to see if you have completed the exercise successfully. You should score full marks if all tests have passed (14 points).
