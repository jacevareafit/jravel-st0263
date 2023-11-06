
Para levantar un cluster de Amazon EKS (Elastic Kubernetes Service) y desplegar una aplicación de WordPress utilizando AWS RDS y un balanceador de carga, el proceso paso a paso se puede dividir en varias partes principales: la creación del cluster EKS, la configuración del entorno local, la instalación de WordPress con Helm y RDS, y finalmente la configuración de los registros DNS. Aquí tienes una guía detallada para cada uno de estos pasos.

# Paso 1: Crear el Cluster EKS
1. Accede a la consola de AWS y navega hasta el servicio EKS.
2. Cambia a la región donde quieres desplegar tu cluster.
3. Selecciona "Create Cluster" y sigue los pasos proporcionados por la interfaz para configurar tu cluster. Incluye detalles como:
   - Nombre del cluster
   - Versión de Kubernetes
   - Roles de IAM
   - VPC y subredes
4. Una vez configurado, inicia la creación del cluster y espera a que AWS lo provisione completamente.

# Paso 2: Configurar el Entorno Local
1. Abrir AWS CloudShell o configurar AWS CLI en tu máquina local.
2. Instalar Helm:
   sh
   sudo yum install openssl -y 
   curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 > get_helm.sh
   chmod 700 get_helm.sh 
   ./get_helm.sh
   
3. Agregar el repositorio Bitnami a Helm:
   sh
   helm repo add bitnami https://charts.bitnami.com/bitnami
   
4. Configurar `kubectl`:
   - En sistemas basados en Unix:
     sh
     mkdir -p $HOME/.kube
     nano $HOME/.kube/config
     
   - En Windows:
     sh
     mkdir %USERPROFILE%\.kube
     notepad %USERPROFILE%\.kube\config
     
   - Añadir la configuración de `kubectl` como se indica en el panel de EKS (reemplaza los placeholders con la información de tu cluster).
5. Añadir la variable `KUBECONFIG` al archivo de perfil de tu shell (`/.bashrc` o `/.bash_profile`):
   sh
   export KUBECONFIG=$HOME/.kube/config
   
6. Ejecutar `source ~/.bashrc` para aplicar los cambios.

# Paso 3: Crear un Node Group
1. Vuelve a la consola de EKS y selecciona tu cluster.
2. En la sección "Compute", crea un Node Group con la configuración deseada.
3. Espera a que AWS termine de crear el Node Group y los nodos estén en estado "Ready".

### Paso 4: Instalar WordPress con Helm y RDS
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


Una vez que los registros DNS se propaguen, deberías poder

 acceder a tu WordPress mediante la URL `www.example.com`.

### Nota Final
Este es un proceso simplificado y asume cierto nivel de familiaridad con AWS y la línea de comandos. En un entorno de producción, también tendrías que considerar la seguridad, el monitoreo, la gestión de costos y otros aspectos importantes del despliegue en la nube.
