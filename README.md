# sql-challenge


#Table Schema
![Schema](https://github.com/Robert-W2019/sql-challenge/blob/main/Employee%20SQL/QuickDBD-export%20(3).png?raw=true)

#Database Analysis

#Dummy Data - private info not disclosed

1. List the following details of each employee: employee number, last name, first name, sex, and salary.
[Q1 Result](https://raw.githubusercontent.com/Robert-W2019/sql-challenge/main/Employee%20SQL/Outputs/Q1.csv)

2. List first name, last name, and hire date for employees who were hired in 1986.
[Q2 Result](https://github.com/Robert-W2019/sql-challenge/blob/main/Employee%20SQL/Outputs/Q2.csv)

3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
[Q3 Result](https://github.com/Robert-W2019/sql-challenge/blob/main/Employee%20SQL/Outputs/Q3.csv)

4. List the department of each employee with the following information: employee number, last name, first name, and department name.
[Q4 Result](https://raw.githubusercontent.com/Robert-W2019/sql-challenge/main/Employee%20SQL/Outputs/Q4.csv)

5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
[Q5 Result](https://github.com/Robert-W2019/sql-challenge/blob/main/Employee%20SQL/Outputs/Q5.csv)

6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
[Q6 Result](https://raw.githubusercontent.com/Robert-W2019/sql-challenge/main/Employee%20SQL/Outputs/Q6.csv)

7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
[Q7 Result](https://raw.githubusercontent.com/Robert-W2019/sql-challenge/main/Employee%20SQL/Outputs/Q7.csv)

8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
[Q8 Result](https://github.com/Robert-W2019/sql-challenge/blob/main/Employee%20SQL/Outputs/Q8.csv)

#Bonus (Optional)

1. Import the SQL database into Pandas.
# Import the Employees Table


```python
employees = pd.read_sql('select * from employees', connection, parse_dates = ['birth_date', 'hire_date' ])
employees.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>emp_no</th>
      <th>emp_title_id</th>
      <th>birth_date</th>
      <th>first_name</th>
      <th>last_name</th>
      <th>sex</th>
      <th>hire_date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>473302</td>
      <td>s0001</td>
      <td>1953-07-25</td>
      <td>Hideyuki</td>
      <td>Zallocco</td>
      <td>M</td>
      <td>1990-04-28</td>
    </tr>
    <tr>
      <th>1</th>
      <td>475053</td>
      <td>e0002</td>
      <td>1954-11-18</td>
      <td>Byong</td>
      <td>Delgrande</td>
      <td>F</td>
      <td>1991-09-07</td>
    </tr>
    <tr>
      <th>2</th>
      <td>57444</td>
      <td>e0002</td>
      <td>1958-01-30</td>
      <td>Berry</td>
      <td>Babb</td>
      <td>F</td>
      <td>1992-03-21</td>
    </tr>
    <tr>
      <th>3</th>
      <td>421786</td>
      <td>s0001</td>
      <td>1957-09-28</td>
      <td>Xiong</td>
      <td>Verhoeff</td>
      <td>M</td>
      <td>1987-11-26</td>
    </tr>
    <tr>
      <th>4</th>
      <td>282238</td>
      <td>e0003</td>
      <td>1952-10-28</td>
      <td>Abdelkader</td>
      <td>Baumann</td>
      <td>F</td>
      <td>1991-01-18</td>
    </tr>
  </tbody>
</table>
</div>



# Import the Departments Table


```python
departments = pd.read_sql('select * from departments', connection)
departments.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dept_no</th>
      <th>dept_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>d001</td>
      <td>Marketing</td>
    </tr>
    <tr>
      <th>1</th>
      <td>d002</td>
      <td>Finance</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d003</td>
      <td>Human Resources</td>
    </tr>
    <tr>
      <th>3</th>
      <td>d004</td>
      <td>Production</td>
    </tr>
    <tr>
      <th>4</th>
      <td>d005</td>
      <td>Development</td>
    </tr>
  </tbody>
</table>
</div>



# Import the Salaries Table


```python
salaries = pd.read_sql('select * from salaries', connection)
salaries
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>emp_no</th>
      <th>salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10001</td>
      <td>60117</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10002</td>
      <td>65828</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10003</td>
      <td>40006</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10004</td>
      <td>40054</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10005</td>
      <td>78228</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>300019</th>
      <td>499995</td>
      <td>40000</td>
    </tr>
    <tr>
      <th>300020</th>
      <td>499996</td>
      <td>58058</td>
    </tr>
    <tr>
      <th>300021</th>
      <td>499997</td>
      <td>49597</td>
    </tr>
    <tr>
      <th>300022</th>
      <td>499998</td>
      <td>40000</td>
    </tr>
    <tr>
      <th>300023</th>
      <td>499999</td>
      <td>63707</td>
    </tr>
  </tbody>
</table>
<p>300024 rows × 2 columns</p>
</div>



# Import the Department Manager Table


```python
dept_manager = pd.read_sql('select * from dept_manager', connection)
dept_manager.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dept_no</th>
      <th>emp_no</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>d001</td>
      <td>110022</td>
    </tr>
    <tr>
      <th>1</th>
      <td>d001</td>
      <td>110039</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d002</td>
      <td>110085</td>
    </tr>
    <tr>
      <th>3</th>
      <td>d002</td>
      <td>110114</td>
    </tr>
    <tr>
      <th>4</th>
      <td>d003</td>
      <td>110183</td>
    </tr>
  </tbody>
</table>
</div>



# Import the Titles Table


```python
titles = pd.read_sql('select * from titles', connection)
titles
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>emp_title_id</th>
      <th>title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>s0001</td>
      <td>Staff</td>
    </tr>
    <tr>
      <th>1</th>
      <td>s0002</td>
      <td>Senior Staff</td>
    </tr>
    <tr>
      <th>2</th>
      <td>e0001</td>
      <td>Assistant Engineer</td>
    </tr>
    <tr>
      <th>3</th>
      <td>e0002</td>
      <td>Engineer</td>
    </tr>
    <tr>
      <th>4</th>
      <td>e0003</td>
      <td>Senior Engineer</td>
    </tr>
    <tr>
      <th>5</th>
      <td>e0004</td>
      <td>Technique Leader</td>
    </tr>
    <tr>
      <th>6</th>
      <td>m0001</td>
      <td>Manager</td>
    </tr>
  </tbody>
</table>
</div>



# Import the Department Employee Table


```python
dept_emp = pd.read_sql('select * from dept_emp', connection)
dept_emp.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>emp_no</th>
      <th>dept_no</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10001</td>
      <td>d005</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10002</td>
      <td>d007</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10003</td>
      <td>d004</td>
    </tr>
    <tr>
      <th>3</th>
      <td>10004</td>
      <td>d004</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10005</td>
      <td>d003</td>
    </tr>
  </tbody>
</table>
</div>

2. Create a histogram to visualize the most common salary ranges for employees.

![Histogram](https://github.com/Robert-W2019/sql-challenge/blob/main/Employee%20SQL/Outputs/output_17_0.png?raw=true)


