# LAB 3-3: Creation of a DataWarehouse with AWS Redshift, Redshift spectrum and with an ERM cluster and hive
## Course Details

| Information |  |
| --- | --- |
| Course name | Tópicos especiales en Telemática |
| Course ID | ST0263 |
| Name | Juan Sebastian Guerra Hernandez (jsguerrah@eafit.edu.co) |
| Teacher | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |

# 1. Main goal

Store Data from the course dataset in a Datawarehouse and be able to fetch that data with queries

# 2. Issues solved 

- [x] Creation of an AWS redshift cluster.
- [x] Execute basic queries in the 'tickit' demo database
- [x] Create an IAM role for Amazon Redshift and run queries to create an external database
- [x] Creation of an ERM cluster an store data with hive

---

# 3. Execution environment

## Guide

Steps to follow for a correct catalog of the data.

---

### Section 1: Creation of an AWS redshift cluster.

We will have to create an AWS Redshift cluster.

1. Log in to the AWS console and search for the AWS Redshift service.
2. Select the `Clusters` section on the left bar and click `Create cluster`.
3. Choose the `dc2.large` type node and `1` number of nodes.
4. In the section Sample data click the box `Load sample data`

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/0ebbeeba-3b97-4e13-8936-7c08eedf613d">
   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/7aa47862-9773-43e2-b213-c8a8a155a06a">
   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/8d98376f-367a-4b14-bd2c-0ac2bbad53db">
   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/7bb69365-5ee2-4998-bd8d-af6d4b6a2583">




   
