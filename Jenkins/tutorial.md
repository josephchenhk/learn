默认端口：8080

访问： http://jenkins.atabet.com:8080/

1. [Jenkins忘记密码解决方案](https://blog.csdn.net/h106140873/article/details/95480258)
2. [Reset Jenkins admin password](https://www.lazysystemadmin.com/2018/12/quick-howto-reset-jenkins-admin-password.html)


To reset the jenkins admin password, You can simply disable the security in the config.xml file.

1. If your jenkins is running on the Linux OS, edit the below file.

vi /var/lib/jenkins/config.xml file.

2. Search for the word <useSecurity>true</useSecurity>
and change the word true to false. 

3. Restart the Jenkins server.
service jenkins restart

4. Now go to the Jenkins portal again and Jenkins will not ask any credentials this time. You navigate to "Manage Jenkins" to set the administrator password again.

5. Enable the security again by changing settings to <useSecurity>true</useSecurity> and restart the Jenkins again.
