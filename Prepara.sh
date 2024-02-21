#!/bin/bash

# Instalar Java 7
sudo yum install java-1.7.0-openjdk-devel -y

# Definir variável de ambiente JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk

# Baixar o Apache Tomcat 7
wget https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.108/bin/apache-tomcat-7.0.108.tar.gz

# Extrair o arquivo baixado
tar -xzvf apache-tomcat-7.0.108.tar.gz

# Mover o Tomcat para /opt
sudo mv apache-tomcat-7.0.108 /opt/tomcat7

# Definir variável de ambiente CATALINA_HOME
export CATALINA_HOME=/opt/tomcat7

# Adicionar o usuário tomcat
sudo useradd -r -m -U -d /opt/tomcat7 -s /bin/false tomcat

# Ajustar permissões
sudo chown -R tomcat: /opt/tomcat7/conf
sudo chmod -R g+r /opt/tomcat7/conf
sudo chmod g+x /opt/tomcat7/conf
sudo chown -R tomcat: /opt/tomcat7/logs
sudo chown -R tomcat: /opt/tomcat7/temp
sudo chown -R tomcat: /opt/tomcat7/webapps
sudo chown -R tomcat: /opt/tomcat7/work

# Criar arquivo de serviço para o Tomcat
sudo bash -c 'cat <<EOF > /etc/systemd/system/tomcat7.service
[Unit]
Description=Apache Tomcat 7
After=syslog.target network.target

[Service]
Type=forking
User=tomcat
Group=tomcat

Environment=JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk
Environment=CATALINA_PID=/opt/tomcat7/temp/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat7
Environment=CATALINA_BASE=/opt/tomcat7

ExecStart=/opt/tomcat7/bin/startup.sh
ExecStop=/opt/tomcat7/bin/shutdown.sh

Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF'

# Recarregar os serviços do systemd
sudo systemctl daemon-reload

# Iniciar o Tomcat
sudo systemctl start tomcat7

# Habilitar o Tomcat para iniciar na inicialização do sistema
sudo systemctl enable tomcat7

# Verificar o status do Tomcat
sudo systemctl status tomcat7
