# LAB 3-2: Data Catalog with Glue and Athena

## Course Details

| Information |  |
| --- | --- |
| Course name | Tópicos especiales en Telemática |
| Course ID | ST0263 |
| Name | Jacobo Rave Londoño (jravel@eafit.edu.co) |
| Teacher | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |

# 1. Task

Catalog data from the course dataset and be able to send serverless queries

---

# 2. Issues solved and not solved

- [x] Create an AWS S3 bucket to store the data.
- [x] Create a crawler from Glue to catalog the dataset.
- [x] Query from Athena over the tables.
- [x] Store the query results in S3.

---

# 3. Execution environment

## Guide

Steps to follow for a correct catalog of the data.

---

### Section 1: Create an AWS S3 bucket to store the data.

We will have to create an AWS S3 bucket to store the data.

1. Log in to the AWS console and search for the S3 service.
2. Select the `Create bucket` button.
3. Enter a name for the bucket; then in the section **Object Ownership** select the option `ACLs enabled` and check the box `Object writer`. 
    
    Then in the **Block Public Access settings for this bucket** section remove the check from the 'Block all public access' option and select the checkbox ‘I acknowledge that the current settings might result in this bucket and the objects within becoming public.’:

    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/1d45403a-e59c-4528-93c9-915651a54909">
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/9a0c7f92-e2f3-48af-9585-59a2766d17c4">
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/8dd27cb1-b67d-4085-88f4-ae43f3987d58">

4. Leave the following options as default and select the `Create Bucket` button.
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/0b3bd175-6bbd-473e-b667-5f38cec130ad">
    
5. Go to the [datasets](https://github.com/st0263eafit/st0263-232/tree/main/bigdata/datasets) and download them.

6. Return to the main bucket interface, select the name of the previously created bucket and drag the downloaded datasets into it, then select the `Upload` button.
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/7dec941e-7edf-4628-8198-16fe1189dad9">

---

### Section 2: Catalog data with AWS Glue

1. Go to the AWS web console and search for the Crawlers Glue service
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/eadd012e-2d9f-4f2b-81e4-94cdece8e857">
    
2. Click on `Create crawler`.
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/23373b72-4907-4911-a43c-4c9fabc91dc4">

3. Set a name for your crawler, then click on `Next`.
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/7d8011da-da44-4a14-994d-d77b96b28370">

4. In **Choose data sources and classifiers** section, click on `Add a data source`
   
   <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/1c6b1da0-9d6c-4553-bab5-841d27163fec">

5. Navigate through to find the folder you want to catalog.
   
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/355ec8f8-5b47-488f-99cb-b36aab092402">

6. Once selected, click on `Add an S3 data source`
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/9a5ac9a2-90c4-4884-871d-541af454d8b0">

7. The preview of the data source should look like this. Then, click on `Next`

    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/24cafc8d-f8fa-41a0-a243-2657f8e65c45">

8. In the **Configure security settings** section, set the LabRole.
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/8396b0ab-8c42-4db5-a9b2-f573e184e86c">

9. Set the default target database. Keep `On demand` schedule to catalog the data manually.
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/edb1b9df-fdd2-48f3-95ba-9b417fc2ca99">

10. After the previous steps, the crawler should be created successfully.

    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/9dff6a67-b3c9-4a9c-8211-bf228743e4a2">

11. Now you must start to catalog. Select your crawler and then click on `Run` to start the job.

    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/cc0de49a-63b1-4df7-99ae-9a0d0ac1c94d">

12. The new table must be there, with a location from your S3 bucket.
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/25273a7b-f75f-4313-8d9a-0576510808a0">
    
---

### Section 3: Query with Athena

1. Go to the AWS web console and search for the Athena service.
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/c122e927-c4bb-44fb-a49c-221969c6979b">
    
3. We must set a location to store our results. Go to **Settings**. Then, click on `Manage`.

    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/18701676-54c5-4807-a822-a288ca2e8c41">

4. In the _Location of query result_ set a path over your bucket where you want to store.
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/1407c463-bdc1-458a-97ce-992897ee218e"> 

5. Then, click on `Save`. Your settings overview should look like this.
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/8ab9dd51-6f02-4537-8360-633868c552c3">

7. Go back to **Editor** section. Select the table created with your crawler.
    
    <img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/9828921b-4a9c-46ec-ac70-031e8af96365">

You can now query over your catalog dataset with Athena.
    
**Examples**
- Query example:
```sql
  SELECT * FROM “default”.”<YOUR_TABLE>” WHERE lifeex > 80 ORDER BY lifeex desc;
```

<img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/4a3ccc91-23db-4a19-a227-41b9057c1676">


---

### Section 4: Save outputs from queries

1. Log into the AWS web console and search for the S3 service.
2. Select your bucket.
3. Search in the path you selected in Section 3, step 4. This path is defined to store output of your queries.

<img width="820" alt="image" src="https://github.com/jacevareafit/jravel-st0263/assets/68928490/1199c6b3-7284-4560-a6bc-5379c849a4e5">


You can store the output of your queries from Athena in S3 buckets.
