# OvirtVMBackup
Scripts for backup VM with Ovirt API

Algorithm

1.- Generate Snapshot to a VM
2.- Clone VM from snapshot
3.- Validate export domain for backups
4.- Export VM
4.- Move export VM to another location ( for integrate with third party software backup )
5.- Generate xml from running VM snapshot
6.- Modify xml to add storageId and Disks from clone VM ovf
7.- Finish

##### What is this repository for? #####

* Script for Backup VM in RHEV/Ovirt
* Version 0.1

lperez@i-t-m.com

luis.luimarin@gmail.com
