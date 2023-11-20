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

1. Go to the AWS web console and search for the EMR service.
    
    <img width="684" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/1ddb76cf-1af7-4bb5-94c7-264f31346247">
    
2. Click on `Create cluster`.
    
    <img width="1336" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/d754e8dd-1eab-4d58-9004-40d7d7f8e906">

3. Enter a name for the cluster, select the version `emr-6.14.0` and select `Custom` in the **Application Bundle** section. Then, select the following applications and enable `Use for Hive table metadata` and `Use for Spark table metadata`.
    
    <img width="622" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/a0e26ce1-549e-4d9d-a724-59b176076eb8">
    
4. Edit the **Cluster termination** section and assign termination after a three (3) hour idle time.
    
    <img width="621" alt="image" src="https://github.com/Jguerra47/jsguerrah-st0263/assets/68879896/8136031e-c371-46a9-8714-a02a8e2fd342">



