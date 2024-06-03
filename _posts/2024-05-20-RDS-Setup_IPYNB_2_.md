---
toc: True
comments: True
layout: post
title: RDS Setup
author: Ethan Z
---

# RDS Setup

## 0. What is RDS? What can we use RDS for?
Amazon's RDS (Relational Database Service) "is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks". Essentially, it boils down to having a large database hosted in the cloud that can be accessed from anywhere, and can be scaled up or down as needed. You can probably tell by now that it seems like an amazing tool for hosting large amounts of info across multiple projects, and it very much is! RDS can handle up to 

## 1. AWS RDS Setup
Before we can do anything further, we need to, obviously, setup RDS. Fortunately, here's a step by step guide:
### 1.a Getting Started
Open up the amazon RDS page and click on create database.

![Orange button Create Database](https://cdn.discordapp.com/attachments/642877065195946004/1244909150459265085/Screen_Shot_2024-05-28_at_12.04.26_AM.png?ex=665ebc7e&is=665d6afe&hm=07e9a9751297e2f096f0e5398a3f8ce1b7e624eff598e13a4e4b7fcf94ce7025&)

From here, we have 2 choices. Standard and Easy create. For this blog, lets use the standard create.

### 1.b Select Database Type
Here we have several different database types that can be selected. Select the database type you want to use. For this blog, we will use MySQL. Most of the steps will (probably) be the same (or at least similar) for other database types.

![Select Database Type](https://cdn.discordapp.com/attachments/642877065195946004/1244910833809756231/Screen_Shot_2024-05-28_at_12.11.06_AM.png?ex=665ebe10&is=665d6c90&hm=4aa5c6ddee3e66ca1396a5232b6dbf9273629fa76dd5bdd9f30a7a2d8d7a8c35&)

### 1.c DB Templates
There are 3 DB templates: Production, Dev/Test, and Free Tier. Each one has it's own use cases and strengths.

![DB Templates](https://cdn.discordapp.com/attachments/642877065195946004/1244911966351265822/Screen_Shot_2024-05-28_at_12.15.37_AM.png?ex=665ebf1e&is=665d6d9e&hm=ca98e9090de6e6131ecb42f06b5dd91e24d60c90f048b56ef0c5e95bdd7bce1f&)

This table will break it down:

| Template | Use Case | Strengths |
|----------|----------|-----------|
| Production | Production workloads | High Availability, Durability, and Scalability |
| Dev/Test | Development and Testing | Cost-Effective, Easy to Use |
| Free Tier | Learning and Experimenting | Free for 12 months, Easy to Use |

For this blog, we will use the Free Tier template (and if your using RDS for a project, you might want to do this as well). This also means we don't really have to worry about the Availability and durability settings.

### 1.d DB Details
Lets give our database a name, and a username and password. Make sure to remember these, as we will need them later. For projects in CSA, please adhere to Mr. Mortensen's naming conventions, but if none are given, lets just use the name of your group and your period. For example, if you are in group 1 and period 1, you could name your database `group1P1`. For this blog, we will be using "RDSDemoP1".

Next, lets set the username and password. Enter a master username, usually it's just admin. For passwords, I would recommend using self managed, as it is a lot simpler to use. Specify, confirm, and **note down** your master password. IF YOU LOSE THIS PASSWORD YOU ARE ***__COOKED__***

![DB Details](https://cdn.discordapp.com/attachments/642877065195946004/1244912879992569927/Screen_Shot_2024-05-28_at_12.19.15_AM.png?ex=665ebff7&is=665d6e77&hm=e1f1e8e2574df413aa624514629bfb3a2640ce262bdbd5d53a1e60d2afb86ec0&)

### 1.e Instance Configuration
We don't really have to worry about this section!

### 1.f Storage
Again, not too much to worry about unless you have a project that needs a really large storage size. Change it to something reasonable, not something insane. (please i beg you)

### 1.g Connectivity
This section is where things get a bit confusing.

The first big choice is whether to connect your RDS to an EC2 or not. Both have their own use cases and advantages, broken down in this table.

| EC2 | No EC2 |
|-----|--------|
| Easy setup | Have to set up using separate database server |
| Less controllability | Easier to do custom settings/debugging |
| Lower processing power | Can be as powerful as you need it to be on your own server |
| Costs money for the instance | no instance required |

We don't really have t worry about changing the VPC, as the default one is fine.

![Connectivity](https://cdn.discordapp.com/attachments/642877065195946004/1244914493562294282/Screen_Shot_2024-05-28_at_12.25.38_AM.png?ex=665ec178&is=665d6ff8&hm=21dfd3f7b8c7708ca8ad60f5189a061f7838f33c0aa570355619d797a4239bb3&)

If you're not using an EC2, select yes on public access, otherwise you will not be able to access the RDS. If you're using an EC2 in the same VPC, it would probably be in the best interest of security to select no.

If you are using an EC2, you can select the security group that the EC2 is in. If you are not using an EC2, you can select the security group that the RDS is in. For this blog, we will not be using an EC2, so we will select the security group that the RDS is in. The group will probably end up being Default if you are doing the same thing as me.

![Connectivity](https://cdn.discordapp.com/attachments/642877065195946004/1244914829358137415/Screen_Shot_2024-05-28_at_12.26.58_AM.png?ex=665ec1c8&is=665d7048&hm=09cad316f1b4ef81b283c5549998730dca03d329b2297ba6b59fbde29a81f208&)

Nothing else really has to be done here except for the RDS Proxy which just makes your database more secure. However, it isn't nesscary and it is also a paid feature.

### 1.h Tags, Authentication, and Monitoring
Don't worry about adding any tags to your RDS, but do make sure your RDS is set to Password Authentication. Otherwise, you won't be able to properly access your RDS. Enhanced monitoring isn't required but is a nice feature to have when debugging.

![Image](https://cdn.discordapp.com/attachments/642877065195946004/1244916279249469471/Screen_Shot_2024-05-28_at_12.32.46_AM.png?ex=665ec322&is=665d71a2&hm=84ae7c825d9816114a909e132b83725e030ba3c26af79b232cdfffd9b132dfad&)

### 1.i Additional Options
Most people skip this section which is why their RDS doesn't work. **PLEASE PAY ATTENTION TO THIS SECTION!** Expand the Additional Options dropdown first.

Specify a database name for the RDS. **If you do not specify a database name, Amazon RDS does not create a database.** For this blog, we'll use the name "RDSDemoDB". The other options can be kept default.

![Name Settings](https://cdn.discordapp.com/attachments/642877065195946004/1244917298926583859/Screen_Shot_2024-05-28_at_12.36.45_AM.png?ex=665ec415&is=665d7295&hm=c2adfe50daf5e9a9e4960fa907e7e515bcd8e134df335974773e8cc8b6433b1e&)

Make sure to enable backups, as that is one of the main strengths of an RDS that allow it to be so reliable.

![Backup Settings](https://cdn.discordapp.com/attachments/642877065195946004/1244917688166514688/Screen_Shot_2024-05-28_at_12.38.22_AM.png?ex=665ec472&is=665d72f2&hm=459a8167523c5c27348e1a6dd1def2322d83e7f041659812d57f092068a6a7c2&)

Enable encryption logging, and deletion protection as you please, just keep in mind that disabling these settings may be bad for the security of your RDS.

![Best Practice Settings](https://cdn.discordapp.com/attachments/642877065195946004/1244917833780170793/Screen_Shot_2024-05-28_at_12.38.54_AM.png?ex=665ec495&is=665d7315&hm=5aa498fa6dcebada9030b774a99ba1bb38a5bc403e8c5ae07e136441fff81d3d&)


### 1.j Review and Create
Review your settings, hit the giant CREATE DATABASE button, and you're done! Congratulations! You have successfully created an RDS!
