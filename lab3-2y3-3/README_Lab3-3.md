# LAB 3-3: Creation of a DataWarehouse with AWS Redshift, Redshift spectrum and with an ERM cluster and hive
## Course Details

| Information |  |
| --- | --- |
| Course name | Tópicos especiales en Telemática |
| Course ID | ST0263 |
| Name | Jacobo Rave Londoño (jravel@eafit.edu.co) |
| Teacher | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |

# 1. Main goal

Store Data from the course dataset in a Datawarehouse and be able to fetch that data with queries

# 2. Issues solved 

- [x] Creation of an AWS redshift cluster.
- [x] Execute basic queries in the 'tickit' demo database
- [x] Create an IAM role for Amazon Redshift and run queries to create an external database in AWS s3 bucket
- [x] Creation of an ERM cluster an store data with hive

---

# 3. Execution environment

## Guide

Steps to follow for a correct catalog of the data.

---

## Section 1: Creation of an AWS redshift cluster.

We will have to create an AWS Redshift cluster.

1. Log in to the AWS console and search for the AWS Redshift service.
2. Select the `Clusters` section on the left bar and click `Create cluster`.

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/0ebbeeba-3b97-4e13-8936-7c08eedf613d">
   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/7aa47862-9773-43e2-b213-c8a8a155a06a">
   
3. Choose the `dc2.large` type node and `1` number of nodes.
   
   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/8d98376f-367a-4b14-bd2c-0ac2bbad53db">

4. In the section Sample data click the box `Load sample data`
   
   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/7bb69365-5ee2-4998-bd8d-af6d4b6a2583">

5. In the database configurations use the user `awsuser` and the password `St1800232.`
   
   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/28135f7e-bbb2-4b34-88da-4e689a698d28">

6. In the section associated IAM roles click `Manage IAM roles` and add the role `LabRole` and `myRedshiftRole`

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/5b17fbab-71fc-437a-a605-3801ba19c680">

7. The last but not least is to click `create cluster`
   
   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/293a0a95-24a0-4737-ad61-f5158827be70">



## Section 2: Execute basic queries in the 'tickit' demo database

1. Wait until the cluster is available and click the list menu `Query data` and click the option `Query in query editor v2`

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/5d8e0e21-2658-4c36-86ff-084068d2c011">

2. To connect to the database click the option `Database username and password` and fill the blanks with the credentians given above (Section 1, step 5)

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/960339a6-ba99-4e91-87c5-59be8a476535">

3. Enter to the `sample_data_dev` folder and click the `tickit open samples queries` and click create

    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/7a866529-4659-4142-a793-0867529c9a59">
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/5c518c64-835e-4d80-83c5-f9ff3d851b7f">

4.  Run the samples queries
   
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/93d87ccd-1ff1-4d23-a298-9e9ff8ad0e41">
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/4e24efb0-8d87-4dac-8a79-2d9f1412a482">
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/5057b7fe-9dda-4250-9fff-7b51ce10f08f">
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/be010870-54d8-4b3b-abdd-51949e6cb020">



## Section 3: Create an IAM role for Amazon Redshift and run queries to create an external database  in AWS s3 bucket

1. Log in to the AWS console and search for the IAM Redshift service.

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/6803f07b-6daa-4aae-8b50-97a6c9c9e6e5">

2. Select the left panel, choose Roles and click `Create role`.
   
   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/b0d037bb-dfca-4f2e-9520-90d97d3d9845">

3. Choose AWS service then choose Redshift. pick `choose Redshift - Customizable` and click next.

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/57554cbd-0f3b-4d4c-96fa-83e2b7da52bc">
      
4. The Attach permissions policy page will appear, add AmazonS3ReadOnlyAccess, AWSGlueConsoleFullAccess and AmazonAthenaFullAcces and click next.

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/173988a6-d018-4b84-9e26-b89ced4b44c2">

5. In Role name, enter `myspectrum_role`, review information, then Create role.

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/9bef2035-da9b-4844-9c12-55f9a9d14aaf">

6. Choose the role you just created and then copy the Role ARN to the clipboard. This ARN will be used when you create the external table in
Amazon S3. Important: In the AWS Academy account, it DOES NOT ALLOW YOU TO CREATE Users, Groups, or Roles, so you will get this error so you will get this error:

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/bd2d0f24-d1aa-451b-94c4-b99e5af77419">

But for the purpose of creating the external table in Redshift Spectrum, you can use the default Role: 'LabRole'.

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/90846c31-dc37-4f92-a1f0-f50e207012e0">

7. Create the external database

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/2c18cede-bf8b-4d66-ae3f-45862da51a56">

8. Create a table with external data in S3

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/0fcf9415-b663-4ce3-bbe9-8f17c8879338">

9. Query data

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/38f1bd35-b01a-4fda-b0e2-fe5eed37c2cf">

10. Remember to pause or delete the cluster if you are not going to work anymore because you will still be charged even after finishing the aws lab.

   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/ae6029da-b9a4-4431-88f0-93c7bec38d34">



You can now query your data!


## Section 4: Creation of an ERM cluster an store data with hive 

1. Create an ERM cluster, here is the [guide](https://github.com/jacevareafit/jravel-st0263/tree/main/lab3-0)

2. connect to the primary node with ssh, here is the [guide](https://github.com/jacevareafit/jravel-st0263/tree/main/lab3-0)

3. 


   





   
