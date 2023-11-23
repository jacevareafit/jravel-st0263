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
    
![Screenshot 2023-11-20 144906](https://github.com/jacevareafit/jravel-st0263/assets/68928490/126964eb-0746-42a7-b852-743e2aa1e658)

