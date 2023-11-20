# LAB 3-0: EMR Cluster

| Information |  |
| --- | --- |
| Course name | Tópicos especiales en Telemática |
| Course ID | ST0263 |
| Name | Jacobo Rave Londoño (jravel@eafit.edu.co) |
| Teacher | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |

# 1. Task
Create an AWS EMR Cluster in Amazon

# 2. Issues solved 

- [x] AWS S3 bucket creation
- [x] AWS EMR Cluster creation
- [x] SSH connection to the master node instance.
- [x] Functional Hue service.
- [x] Functional JupyterHub service.
      

# 3. Execution environment

## Usage guide

Steps to follow for a correct develop of the lab 3-0.

---

### Section 1: AWS S3 bucket creation

We need to set up an AWS S3 bucket to keep the notebooks that we'll generate using the AWS EMR cluster.

1.  Access the AWS web console and look for the S3 service.
  
   ![Screenshot 2023-11-17 182322](https://github.com/jacevareafit/jravel-st0263/assets/68928490/dc09dd62-53ee-47b3-b5a1-15e9bc15e0d8)

    
2. Click on `Create bucket`:
   
    ![Screenshot 2023-11-17 182328](https://github.com/jacevareafit/jravel-st0263/assets/68928490/38c2757e-d3d1-42c9-931c-730fa385868a)


    
3. Name the bucket and leave the all the next options as default and select the `Create Bucket` button.

![Screenshot 2023-11-17 182412](https://github.com/jacevareafit/jravel-st0263/assets/68928490/5d9756ae-edca-4f72-9157-9668246ff36e)
![Screenshot 2023-11-17 182420](https://github.com/jacevareafit/jravel-st0263/assets/68928490/d7326f36-94d6-4d06-9fa4-9758598ea36d)
  
    
---

### Section 2: AWS EMR cluster creation

1. Look up for the EMR service.
    
   ![Screenshot 2023-11-17 182502](https://github.com/jacevareafit/jravel-st0263/assets/68928490/87c84303-e19a-4530-b546-b3b23026bd50)

    
2. Click on `Create cluster`.
    
   ![Screenshot 2023-11-17 182507](https://github.com/jacevareafit/jravel-st0263/assets/68928490/381dfc9d-3493-416d-a858-59f51265de1d)


3. Name the cluster, select the version `emr-6.14.0` and select `Custom` in the **Application Bundle** section. Select the following applications and enable both `Use for Hive table metadata` and `Use for Spark table metadata`.
    ![WhatsApp Image 2023-11-18 at 11 10 13 AM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/7446808a-3bf7-4055-8ee4-41f253708f1d)
    ![Screenshot 2023-11-17 182645](https://github.com/jacevareafit/jravel-st0263/assets/68928490/2bb82438-96a2-43e9-ad50-43889e3be7b5)

    
4. Edit the **Cluster termination** section and assign termination after a three (3) hour idle time.
    
   ![Screenshot 2023-11-17 182809](https://github.com/jacevareafit/jravel-st0263/assets/68928490/95ebbf38-cc8d-4fdf-8e8b-f910a521db34)


5. Leave all the next options as default and go to the **Software settings** section.
   
6. Select the `Enter configuration` option and paste the following configuration:
    
    ```json
    [
      {
        "Classification": "jupyter-s3-conf",
        "Properties": {
          "s3.persistence.enabled": "true",
          "s3.persistence.bucket": "your_bucket_name"
        }
      }
    ]
    ```
    the field s3.persistence.bucket must be name with your bucket name created before.
   
![Screenshot 2023-11-17 182914](https://github.com/jacevareafit/jravel-st0263/assets/68928490/9e0a7322-0c24-4afc-9bf8-01dcfbfd7a9d)

7. Go to the section **Security configuration and EC2 key pair** and in the option **Amazon EC2 key pair for SSH to the cluster** choose a custom key or the deafult one.
    
   ![Screenshot 2023-11-17 182928](https://github.com/jacevareafit/jravel-st0263/assets/68928490/6f5eefda-181d-494f-b25e-6400357b3b14)


8. In the section '**Identity and Access Management (IAM) roles** select these options:

    - **Amazon EMR Service Role**: EMR_DefaultRole
    - **EC2 Instance Profile for Amazon EMR**: EMR_EC2_DefaultRole
    - **Custom Auto Scaling Role**: LabRole
      
![Screenshot 2023-11-17 182951](https://github.com/jacevareafit/jravel-st0263/assets/68928490/777f2c44-d7a8-4633-a49b-2c99dd941155)
![Screenshot 2023-11-17 182957](https://github.com/jacevareafit/jravel-st0263/assets/68928490/57aed4b5-56b9-4375-872b-a08a1140a493)

    
9. Finally, click on `Create cluster`.
    
![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/9468f5e5-82bc-4030-b6ce-d2af67cebc00)


---


### Section 3: Edit security groups for the applications

IMPORTANT: The following steps should only be performed once, each time a cluster is created, destroyed or cloned.

1. search for the EMR service.
    
    ![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/fd1ddb66-dda5-4908-bdf0-fa279ab996aa)

    
2. Select the option **Block public access** Within the Amazon EMR menu.
    
    ![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/7b1fd006-83d2-48a4-ac49-c10f51a5db8c)

    
3. Select the `Edit` button. In the **Block public access** section select the `Turn off` option and select the `Save` button.

    ![WhatsApp Image 2023-11-18 at 11 11 53 AM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/e1990f9d-e371-4b85-aa94-27d46081d3c0)
   ![WhatsApp Image 2023-11-18 at 11 12 12 AM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/73eb74ff-3b2c-4f13-b813-fe36c4363210)
![WhatsApp Image 2023-11-18 at 11 12 24 AM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/f678cd72-e5ae-46d2-ae49-28e707237688)


4. Go to **Clusters** and select the `Cluster ID` that has the status 'Waiting'. Then select the `Applications` option.
    
    ![WhatsApp Image 2023-11-18 at 11 14 31 AM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/db6b5978-aeee-4afa-867b-d180a0d51005)

    The TCP ports above must be opened, in addition to TCP ports 22, 14000 and 9878. 

5. Search for the EC2 service. Then, go to `Security groups` section.
    
   ![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/86aa11d0-a198-47ab-b7a8-7643999a9240)

6. Click on the ID of the SG that has the name ‘ElasticMapReduce-master’.
    
    ![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/e2fdba9d-09fd-4cb5-bc86-611fc31593d6)


7. Click on `Edit inbound rules`.
    
![WhatsApp Image 2023-11-18 at 11 38 49 AM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/eaf39659-14e8-45dd-9939-c2d2544d8b46)

8. For each of the ports shown in the steps 4, perform the following:
    - Click on `Add rule`:
    - Select the `Custom TCP` option, enter the port number and select the 'Anywhere-IPv4' option:
    - Type the port.
    - Click on `Save rules` once you have added all.

---

### Section 4: Access to Primary node

1. Within the Amazon EMR menu go to **Clusters** and select the `Cluster ID` that has the create before.
2. Click on the URL `Connect to the Primary node using SSH` and follow the instructions there. 
    
    ![WhatsApp Image 2023-11-18 at 11 57 13 AM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/0f27161c-d912-4575-b8f9-a3f61fc035a6)

3. A successful SSH connection to the master node of the cluster will look like this:
    ![WhatsApp Image 2023-11-18 at 12 44 13 PM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/61630022-7775-44de-a27d-e9b33be07c92)

   

4. You will need to edit the 'hue.ini' file by following these steps: 
    1. Type the following command in the terminal:
   
        ```bash
        sudo nano /etc/hue/conf/hue.ini
        ```
        
    2. Find the line containing 'webhdfs_url' and change the port. You should put the HDFS Name Node port found in the Applications section over your cluster.

       ![WhatsApp Image 2023-11-18 at 11 14 31 AM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/cc0c2db0-4e00-4ae8-9591-565fc31eb913)

        As you can see, the selected port must be 9870

        ![WhatsApp Image 2023-11-18 at 12 50 19 PM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/8a3ba478-b901-488a-b2f3-3bc38b8690a3)

        
    3. Save the changes over the file.
    4. Restart the Hue service using the following command:
        
        ```bash
        sudo systemctl restart hue.service
        ```
        
---

### Section 5: Hue service

1. Go to **Clusters** and select the `Cluster ID` that has the status 'Waiting'. Then select the `Applications` option.
    ![WhatsApp Image 2023-11-18 at 11 11 12 AM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/bf3ff0aa-3162-4f4e-9cd6-0dc5e83a3331)

    
2. Select the URL of the 'Hue' field. Then, enter the user 'hadoop' and a password of your choice.
![WhatsApp Image 2023-11-18 at 12 57 20 PM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/91ac42ce-aa93-4928-aaf1-01654d1851c3)

 


✅ You just have finished the config of hue services so you can now manage files through Hue for HDFS.

---

### Parte 7: Using JupyterHub

1. Log into the AWS web console and search for the EMR service, select the `Cluster ID` that has the status 'Waiting'; then select the **Applications** option.!

2. Select the URL of the 'JupyterHub' field. Now, enter the user 'jovyan' and password 'jupyter'.
   [WhatsApp Image 2023-11-18 at 1 01 55 PM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/e525a568-97a6-44cd-a9ae-29c19607cea4)
   
3. Select the `New` button and select the `PySpark` option:
    ![WhatsApp Image 2023-11-18 at 1 03 23 PM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/e0f635b0-c667-4656-bb43-b733fbfce804)
    
4. Verify the Spark context variables are installed:
    ![WhatsApp Image 2023-11-18 at 1 05 01 PM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/868db71f-d389-4995-a74b-2495ce440c12)

✅ You just have finished the config of JupyterHub services so you can now build PySpark notebooks.
