# LAB 3-1: File Management with HDFS and S3

| Information |  |
| --- | --- |
| Course name | Tópicos especiales en Telemática |
| Course ID | ST0263 |
| Name | Jacobo Rave Londoño (jravel@eafit.edu.co) |
| Teacher | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |

# 1. Task

Manage the files given ([datasets](https://github.com/st0263eafit/st0263-232/tree/main/bigdata/datasets)) in HDFS and S3 services.

---

# 2. Issues solved

- [x] Create AWS S3 public bucket.
- [x] File management HDFS with terminal.
- [x] File management in HDFS with HUE.
- [x] File management in S3 with HUE.

---

# 3. Execution environment

## Usage guide
Steps to follow for a correct develop of the lab 3-1.

### Section 1: Create AWS S3 public bucket

1. Search for the S3 service.
   
![Screenshot 2023-11-20 144418](https://github.com/jacevareafit/jravel-st0263/assets/68928490/d178c81f-4868-4a05-8d28-68247c9cda50)
   
2. Select the `Create bucket` button.
   
![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/b6faa223-416e-44f6-83f4-7ae4520b769f)


3. Enter a name for the bucket; then in the section **Object Ownership** select the option `ACLs enabled` and check the box `Object writer`.
   
![Screenshot 2023-11-20 144503](https://github.com/jacevareafit/jravel-st0263/assets/68928490/15728805-95bf-485c-9f4e-5c2e65e622e6)
![Screenshot 2023-11-20 144629](https://github.com/jacevareafit/jravel-st0263/assets/68928490/aab6d1e5-b1a4-4a77-b463-a79f7364f6a1)

    
4. Then in the **Block Public Access settings for this bucket** section remove the check from the 'Block all public access' option and select the checkbox ‘I acknowledge that the current settings might result in this bucket and the objects within becoming public.’:
    
![Screenshot 2023-11-20 144622](https://github.com/jacevareafit/jravel-st0263/assets/68928490/282999bf-6503-4ac9-8d83-c8d908a9edff)


5. Leave the following options as default and select the `Create Bucket` button:
   
![Screenshot 2023-11-20 144705](https://github.com/jacevareafit/jravel-st0263/assets/68928490/2c50fd45-ae71-46ac-b557-7e2fb476b238)
    
6. Once in the S3 menu, select the name of the previously created bucket:
   
7. Select the **Permissions** section and look for the **Access control list (ACL)** subsection, once there, select the `Edit` button.
    
![Screenshot 2023-11-20 144727](https://github.com/jacevareafit/jravel-st0263/assets/68928490/d44acc7c-992b-467f-8c64-508c483d8bc3)

8. Check the 'List' and 'Read' boxes for 'Everyone (public access)' and 'Authenticated users group (anyone with an AWS account)'; then check the option 'I understand the effects of these changes on my objects and buckets.'; finally select the `Save changes` button:

![Screenshot 2023-11-20 144953](https://github.com/jacevareafit/jravel-st0263/assets/68928490/ef717fed-e6b2-4636-8cef-b48131a770d0)

9. Download this [example file](https://github.com/st0263eafit/st0263-232/blob/main/bigdata/datasets/airlines.csv) and click the `Download raw file` button:
    
![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/598edf3b-6a1b-495b-9959-c9a98ca718e2)

10. Return to the main bucket interface, select the name of the previously created bucket and drag the downloaded file into it, then select the `Upload` button.

![Screenshot 2023-11-20 145148](https://github.com/jacevareafit/jravel-st0263/assets/68928490/5c251c11-d17a-440b-8cae-641043ea3aa2)

    
11. Select the name of the previously uploaded file and then, in the **Properties** section under ****Object overview**** copy the 'Object URL'.
    
![Screenshot 2023-11-20 145314](https://github.com/jacevareafit/jravel-st0263/assets/68928490/b3edf480-4db6-41e8-9e1d-752de8ee4d8a)

    
12. In a browser window paste the previously copied URL leaving aside '/airlines.csv'.

![Screenshot 2023-11-20 150643](https://github.com/jacevareafit/jravel-st0263/assets/68928490/e9d389a9-8d55-40b3-88c6-7a70ea41c882)

You now have an AWS S3 public bucket.

Important: If you want to read the files from the public bucket, you can use the following command through the AWS CLI:

```bash
aws s3 ls s3://your_bucket
```
Command to read the previously created bucket

```bash
aws s3 ls s3://jravelnotebook2
```
  ![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/4c81804d-18ef-4d2e-a2f8-c6dd95540e01)


---

### Section 2: File management HDFS with terminal

1. We need to create an AWS EMR cluster, here the guide '[Creating an EMR Cluster](https://github.com/jacevareafit/jravel-st0263/blob/main/lab3-0/readme.md)' for this purpose.
   
2. Connect to SSH
   
3. After establishing a connection to the primary node we will create a folder called 'gutenberg-small' inside the path '/user/hadoop/datasets' using the following commands:

    1. Create the directory 'datasets' inside the path 'user/hadoop/'.
   
    ```bash
    hdfs dfs -mkdir /user/hadoop/datasets
    ```

    2. Create the directory 'gutenber-small' inside the path 'user/hadoop/datasets/'.
   
    ```bash
    hdfs dfs -mkdir /user/hadoop/datasets/gutenberg-small
    ```

    3. List directories and files present in /user/hadoop/ path
   
    ```bash
    hdfs dfs -ls /user/hadoop/datasets
    ```
    
6. To put the contents of a local to the directory '/user/hadoop/datasets/gutenberg-small' use the following command. 
    
    ```bash
    hdfs dfs -put <YOUR_LOCAL_FOLDER> /user/hadoop/datasets/gutenberg-small/
    ```

You can now manage files to HDFS from the EMR cluster using the terminal.

---

### Section 3: File management in HDFS with HUE

1. Search for the EMR service.
   
![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/8bb5ecc3-4bfc-4ea9-ab98-a2f0c7bbf81b)

2. Select the 'Cluster ID' that has the status 'Waiting'; then select the **Applications** option.
3. Select the URL of the **Hue** field and enter the 'hadoop' user and a password.
4. Select the **Files** section:
   
![Screenshot 2023-11-20 160724](https://github.com/jacevareafit/jravel-st0263/assets/68928490/c89d52f4-d8ad-4845-8bc3-bf98b3d7aff0)


5. If you have been following the previous steps right, you must found the folder **gutenberg-small**. Otherwise, create the folder in `New` button:

![Screenshot 2023-11-20 160959](https://github.com/jacevareafit/jravel-st0263/assets/68928490/3c385a00-f513-4a57-a127-8f18097b44a9)

6. Select the `Upload` button:
    
![Screenshot 2023-11-20 161008](https://github.com/jacevareafit/jravel-st0263/assets/68928490/efea0070-9591-4a48-9f62-0ac692b9c2b0)


You can now upload files to HDFS of the EMR cluster via HUE.

