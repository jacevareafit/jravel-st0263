Integrantes:
Kevin Alejandro Sossa Chavarria
Daniel Jaramillo Valencia
Antonio Carmona Gaviria
Jacobo Rave Londoño

# Proyecto2
Desplegar wordpress en un cluster de kubernetes en AWS

Para levantar un cluster de Amazon EKS (Elastic Kubernetes Service) y desplegar una aplicación de WordPress utilizando AWS y un balanceador de carga hay que crear el cluster EKS, la configuración del entorno local, la instalación de WordPress con Helm y finalmente configurar los registros DNS. 

# Paso 1: Crear el Cluster EKS
1. Accede a la consola de AWS y navega hasta el servicio EKS.
   ![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/51d98d34-76ce-4df0-b6a5-cbdbeeba282c)

3. Cambia a la región donde quieres desplegar tu cluster para evitar problemas usar (oregon us-east-2).
4. Selecciona "Create Cluster"

   ![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/b40e064f-3ea2-4918-acad-1143b4c5d88a)
5. configurar el cluster con:

   - Nombre del cluster
   - Versión de Kubernetes (1.28)
   - VPC
  
     ![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/d08fceab-1b07-4619-b6bb-7b76ac9d7aaa)

6. Una vez configurado, inicia la creación del cluster y espera a que AWS lo provisione completamente.

# Paso 2: Configurar el Entorno Local
1. Abrir AWS CloudShell o configurar AWS CLI en tu máquina local.
   ![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/6fb5b295-a181-426e-8785-000504441f38)

3. Instalar Helm:
   sh
   sudo yum install openssl -y 
   curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 > get_helm.sh
   chmod 700 get_helm.sh 
   ./get_helm.sh
   
4. Agregar el repositorio Bitnami a Helm:
   sh
   helm repo add bitnami https://charts.bitnami.com/bitnami
   
5. Configurar `kubectl`:
   - En sistemas basados en Unix:
     sh
     mkdir -p $HOME/.kube
     nano $HOME/.kube/config
     
   - En Windows:
     sh
     mkdir %USERPROFILE%\.kube
     notepad %USERPROFILE%\.kube\config
     
   - Añadir la configuración de `kubectl` como se indica en el panel de EKS (reemplaza los placeholders con la información de tu cluster).
     
6. Añadir la variable `KUBECONFIG` al archivo de perfil de tu shell (`/.bashrc` o `/.bash_profile`):
   sh
   export KUBECONFIG=$HOME/.kube/config
   
8. Ejecutar `source ~/.bashrc` para aplicar los cambios.

# Paso 3: Crear un Node Group
1. Vuelve a la consola de EKS y selecciona tu cluster.
2. En la sección "Compute", crea un Node Group con la configuración deseada.
   ![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/a7ce2b0c-dd79-4f4f-ad3a-36fc768a2d52)

4. Espera a que AWS termine de crear el Node Group y los nodos estén en estado "Ready".

### Paso 4: Instalar WordPress con Helm
1. Crea una instancia de RDS que WordPress usará como base de datos.
2. Instala WordPress utilizando Helm y configura los valores para conectar con la instancia de RDS:
   sh
   helm install my-release bitnami/wordpress \
     --set wordpressUsername=admin \
     --set wordpressPassword=defaultpass \
     --set externalDatabase.host=<your-rds-endpoint> \
     --set externalDatabase.user=<your-rds-username> \
     --set externalDatabase.password=<your-rds-password> \
     --set externalDatabase.database=<your-rds-database-name> \
     --set mariadb.enabled=false
   
3. Verifica que los pods y los PVCs estén funcionando correctamente:
   sh
   kubectl get pod
   kubectl get pvc
   

# Paso 5: Configurar DNS y Load Balancer
1. Una vez que WordPress esté desplegado, AWS configurará un Load Balancer automáticamente.
2. Ve a la sección de "Load Balancers" en la consola de AWS y copia el DNS Name proporcionado.
3. Configura los registros CNAME en tu DNS para apuntar a este DNS Name. Por ejemplo, si tu dominio es `example.com`, necesitarás dos registros CNAME:
   - Uno para `www.example.com`
   - Uno para `ssh.example.com` si planeas acceder vía SSH (opcional)
   
La configuración exacta de los registros CNAME dependerá del proveedor de DNS que estés utilizando. Asegúrate de reemplazar `<load-balancer-dns-name>` con el nombre DNS del Load Balancer que AWS te proporcionó:

dns
www     IN CNAME <load-balancer-dns-name>.
ssh     IN CNAME <load-balancer-dns-name>.


![WhatsApp Image 2023-11-06 at 6 44 40 PM](https://github.com/jacevareafit/jravel-st0263/assets/68928490/f9787e1b-e03e-4d77-82b1-80fd3fda85bb)


Una vez que los registros DNS se propaguen, deberías poder

 acceder al WordPress mediante la URL `www.example.com`.


# Demo y desarrollo proyecto 2
https://eafit-my.sharepoint.com/personal/jravel_eafit_edu_co/_layouts/15/stream.aspx?id=%2Fpersonal%2Fjravel%5Feafit%5Fedu%5Fco%2FDocuments%2FGrabaciones%2Fproyecto2%2D20231106%5F182339%2DMeeting%20Recording%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview&ga=1

