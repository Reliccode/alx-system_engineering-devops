su betty - script that switches the current user to the user betty
whoami - script that prints the effective username of the current user
id -Gn - script that prints all the groups the current user is part of
chown betty hello -  script that changes the owner of the file hello to the user betty
touch hello - a script that creates an empty file called hello
chmod u+x hello - a script that adds execute permission to the owner of the file hello
chmod u+x,g+x,o+r hello - script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello
chmod ugo+x hello - script that adds execution permission to the owner, the group owner and the other users, to the file hello
chmod 007 hello -  a script that sets the permission to the file hello as follows:

Owner: no permission at all
Group: no permission at all
Other users: all the permissions

chmod 753 hello -  script that sets the mode of the file hello to this: -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
chmod --reference=olleh hello - script that sets the mode of the file hello the same as olleh’s mode
chmod -R ugo+x . -  script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users
mkdir -m 751 my_dir - script that creates a directory called my_dir with permissions 751 in the working directory
chgrp school hello - script that changes the group owner to school for the file hello
chown -hR vincent:staff . - script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory
chown -h vincent:staff _hello -  script that changes the owner and the group owner of _hello to vincent and staff respectively.

The file _hello is in the working directory
The file _hello is a symbolic link

chown --from=guillaume betty hello - script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
telnet towel.blinkenlights.nl - script that plays Star Wars IV episode in terminal
