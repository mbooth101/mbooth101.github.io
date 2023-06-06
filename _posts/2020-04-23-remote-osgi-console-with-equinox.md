---
layout: single
author_profile: true
title: Using the remote OSGi console with Equinox
date: 2020-04-23 15:00
tags: eclipse osgi
---

You may be familiar with the OSGi shell you get when you pass the ```-console``` option to Equinox on the command line. Did you know you can also use this console over Telnet sessions or SSH sessions? This article shows you the bare minimum needed to do so.

To recap, the minimal bundle set needed to start Equinox with the console is as follows:

```text
org.apache.felix.gogo.command_1.0.2.v20170914-1324.jar
org.apache.felix.gogo.runtime_1.1.0.v20180713-1646.jar
org.apache.felix.gogo.shell_1.1.0.v20180713-1646.jar
org.eclipse.equinox.console_1.4.0.v20190819-1430.jar
org.eclipse.osgi_3.15.200.v20200214-1600.jar
```

All of these bundles are available in the **Equinox SDK** zip file available from the [Equinox Downloads](https://download.eclipse.org/equinox/) site. As of writing the latest release is [Equinox SDK 4.15](https://download.eclipse.org/equinox/drops/R-4.15-202003050155/download.php?dropFile=equinox-SDK-4.15.zip).

Extract these bundles into a directory, then inside that directory create a ```configuration/config.ini``` file with the following content:

```ini
osgi.bundles=\
    org.apache.felix.gogo.runtime,\
    org.apache.felix.gogo.command,\
    org.apache.felix.gogo.shell,\
    org.eclipse.equinox.console
```

Now you can start this minimal Equinox, with console, by passing the ```-console``` option, for example:

```console
$ java -jar org.eclipse.osgi_*.jar -console
osgi> ss
"Framework is launched."


id      State       Bundle
0       ACTIVE      org.eclipse.osgi_3.15.200.v20200214-1600
1       ACTIVE      org.apache.felix.gogo.runtime_1.1.0.v20180713-1646
2       ACTIVE      org.apache.felix.gogo.command_1.0.2.v20170914-1324
3       ACTIVE      org.apache.felix.gogo.shell_1.1.0.v20180713-1646
4       ACTIVE      org.eclipse.equinox.console_1.4.0.v20190819-1430
osgi> exit
Really want to stop Equinox? (y/n; default=y)  
```

### Over Telnet

Starting the console in a Telnet session instead is very easy, you just need to pass a port number with the ```-console``` option, for example:

```console
$ java -jar org.eclipse.osgi_*.jar -console 1234
```

From another terminal, you can then connect to the Telnet session like this, using the port you specified above:

```console
$ telnet localhost 1234
Trying ::1...
Connected to localhost.
Escape character is '^]'.
osgi> ss
"Framework is launched."


id      State       Bundle
0       ACTIVE      org.eclipse.osgi_3.15.200.v20200214-1600
1       ACTIVE      org.apache.felix.gogo.runtime_1.1.0.v20180713-1646
2       ACTIVE      org.apache.felix.gogo.command_1.0.2.v20170914-1324
3       ACTIVE      org.apache.felix.gogo.shell_1.1.0.v20180713-1646
4       ACTIVE      org.eclipse.equinox.console_1.4.0.v20190819-1430
osgi> disconnect
Disconnect from console? (y/n; default=y) 
Connection closed by foreign host.
```

Notice the use of the ```disconnect``` command this time, which allows you to end the console session without causing Equinox to exit. You can of course still use ```exit``` if you wish to terminate Equinox remotely.

You may also set the port in the ```configuration/config.ini``` file with the addition of this line:

```ini
osgi.console=1234
```

And that will start the console as a Telnet session automatically on port 1234 without needing to pass ```-console``` at all, but if you do pass ```-console``` it will override any setting you have in the ```configuration/config.ini``` file.

### Over SSH

To start a console session in an SSH session, a few more bundles are needed:

```text
org.apache.felix.gogo.command_1.0.2.v20170914-1324.jar
org.apache.felix.gogo.runtime_1.1.0.v20180713-1646.jar
org.apache.felix.gogo.shell_1.1.0.v20180713-1646.jar
org.apache.sshd.osgi_2.4.0.v20200318-1614.jar
org.eclipse.equinox.console_1.4.0.v20190819-1430.jar
org.eclipse.equinox.console.jaas.fragment_1.0.300.v20200111-0718.jar
org.eclipse.equinox.console.ssh-1.2.600-SNAPSHOT.jar
org.eclipse.osgi_3.15.200.v20200214-1600.jar
org.slf4j.api_1.7.2.v20121108-1250.jar
```

All of these bundles are available in the **Equinox SDK** zip file available from the [Equinox Downloads](https://download.eclipse.org/equinox/) site. As of writing the latest release is [Equinox SDK 4.15](https://download.eclipse.org/equinox/drops/R-4.15-202003050155/download.php?dropFile=equinox-SDK-4.15.zip).

Extract these bundles into a directory, then inside that directory create a ```configuration/config.ini``` file with the following content:

```ini
osgi.bundles=\
    org.apache.felix.gogo.runtime,\
    org.apache.felix.gogo.command,\
    org.apache.felix.gogo.shell,\
    org.apache.sshd.osgi,\
    org.eclipse.equinox.console,\
    org.eclipse.equinox.console.jaas.fragment,\
    org.eclipse.equinox.console.ssh@start,\
    org.slf4j.api
osgi.console.ssh=127.0.0.1:1234
osgi.console.ssh.useDefaultSecureStorage=true

```

Equinox uses [JAAS](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jaas/JAASRefGuide.html) to authenticate SSH sessions, the default provider of which must be configured by creating a JAAS configuration file, for example ```configuration/console.authentication.config``` with the following content:

```text
equinox_console {
    org.eclipse.equinox.console.jaas.SecureStorageLoginModule REQUIRED;
};
```

Then when starting Equinox you need to tell it where the JAAS configuration is by setting the ```java.security.auth.login.config``` system property. The default JAAS implementation stores its credentials in a file you must specify with the ```org.eclipse.equinox.console.jaas.file``` system property:

```console
$ java -Dssh.server.keystore=configuration/hostkey.ser \
       -Dorg.eclipse.equinox.console.jaas.file=configuration/store \
       -Djava.security.auth.login.config=configuration/console.authentication.config -jar org.eclipse.osgi_*.jar
```

The default JAAS provider creates one default user account with username/password credentials of equinox/equinox. After you log in with these credentials, you will be prompted to create a new account and the default account will be removed.

Once Equinox is started, from another terminal you can connect to the SSH session like this:

```console
$ ssh -p 1234 equinox@127.0.0.1
The authenticity of host '[127.0.0.1]:1234 ([127.0.0.1]:1234)' can't be established.
RSA key fingerprint is SHA256:7x3eOsDRM5lyL5vRsVREy8hIawIfqRiZ7CBnk6GkfRA.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[127.0.0.1]:1234' (RSA) to the list of known hosts.
Password authentication
Password: 
Currently the default user is the only one; since it will be deleted after first login, create a new user:
username: mbooth
password: 
Confirm password: 
roles: admin
osgi> disconnect
Disconnect from console? (y/n; default=y) 
Connection to 127.0.0.1 closed.
```

On subsequent connections you will be required to supply the newly created credentials:

```console
$ ssh -p 1234 mbooth@127.0.0.1
Password authentication
Password: 
osgi> disconnect
Disconnect from console? (y/n; default=y) 
Connection to 127.0.0.1 closed.
```

Once logged in there are various commands for managing user accounts, passwords and roles. Type ```help``` at the OSGi console prompt to find out about these commands. It is possible to implement custom JAAS providers that can use different credential stores, but that is out of the scope of this article.

### Public Key Authentication 

It's common to want to use public key authentication with SSH and you may configure Equinox to do that instead of using JAAS authentication. First create your SSH key-pair as normal and create a file that contains the list of authorised keys that Equinox should consult when you attempt to connect:

```console
$ ssh-keygen -f ~/.ssh/equinox
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/mbooth/.ssh/equinox
Your public key has been saved in /home/mbooth/.ssh/equinox.pub
The key fingerprint is:
SHA256:0k7MSbLLzhhzI7Gw6oSYEx8Fv5UpNHMPTdOUDj8rplQ mbooth@thinkpad-p50
The key's randomart image is:
+---[RSA 3072]----+
|  . + oooo..     |
|   + + =o.o      |
|    + = o+       |
|   . + BE.+      |
|. o o o.S  o     |
|o+ + +.=o .      |
|=.o =.=o..       |
|.o   O..         |
|o.  . o          |
+----[SHA256]-----+

$ cat ~/.ssh/equinox.pub > configuration/equinox_authorized_keys
```

Next you will need to remove the following line from your ```configuration/config.ini``` file:

```ini
# Remove this line
osgi.console.ssh.useDefaultSecureStorage=true
```

Now when you start Equinox, instead of telling it about the JAAS configuration, you must tell it about the authorised keys file:

```console
$ java -Dssh.server.keystore=configuration/hostkey.ser \
       -Dssh.server.authorized_keys=configuration/equinox_authorized_keys -jar org.eclipse.osgi_*.jar
```

And that allows you to use your SSH key instead of a username/password pair when connecting to the SSH console session:

```console
$ ssh -i ~/.ssh/equinox -p 1234 localhost
The authenticity of host '[localhost]:1234 ([127.0.0.1]:1234)' can't be established.
RSA key fingerprint is SHA256:m2JKy2fRZA1aqvxHBBe+Awsgk98ryI29fH03Rg7jeHw.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:1234' (RSA) to the list of known hosts.
osgi> disconnect
Disconnect from console? (y/n; default=y) 
Connection to localhost closed.
```

Pretty nifty, eh?
