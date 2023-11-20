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
    
   

---


