# Honsuri Web service - Backend
Online pub web service for people who drink alone

## Table of Contents
1. [Introduction to Web Services](#1-introduction-to-web-services)
2. [Project Configuration](#2-project-configuration)
3. [Implementation Features](#3-implementation-features)
4. [Wireframe](#4-wireframe)
5. [Role](#5-role)

[Configuration/Execution](#configuration/execution)

## 1. Introduction to Web Services
<img src="https://user-images.githubusercontent.com/45763812/130172366-0e79280d-3ba3-4b21-8249-24ef484daad6.jpg" width="50%" height="50%"/>

- **Online pub web service for people who drink alone** 
- **Intention of the plan** : 
    The spread of COVID-19 has led to an increase in the number of "honsul people" who enjoy drinking alone at home. Accordingly, it developed a web service targeting 'Honsul people'. Users can create an atmosphere through the Honsu-ri website when they are contemplating alone and want to enjoy drinking. You can enjoy drinking alone at home with good music, pretty designs, and guest books that can shake off your worries.
- **Key Features** :
    - The feature to enjoy music through the main music player
    - The feature to filter, locate, and bookmark recipes that make cocktails
    - Guestbook and Overwrite CRUD Features
    - The "Like" and "Report" function in the guest book
    - Membership, login, logout, My Page features

## 2. Project Configuration
### **Technology stacks and libraries**

| Group | Tools | Goal |
| ------ | ------ | ------ |
| Backend | Django | Web Framework |
| Backend | MySQL | Database |
| Backend | drf-yasg | API Documentation |
| Backend | DRF | Restful API Server build |
| Backend | CKEditor | Rich Text use |

## 3. Implementation Features
1. **Mandatory Implementation**
    - Authentication: Member registration / login / logout / My page (written by me, bookmarked recipe)
    - Guest book: guest book (writing, list, search, like), comment (writing, list)
    - Conversation: Find a cocktail that goes well with MBTI
    - Music: Music Player
    - Recipe: Recipe (main, detail, filtering, bookmark)
2. **Selection Implement**
    - Authentication: My page (modifying member information, leaving), login (finding ID, password)
    - Guest book: Modify and delete guest book, report, view details

## 4. Wireframe
- A detailed wireframe was created based on the required/selected implementation function.
- There is a steady stream of updates.
- The wire frame link is as follows: [wire frame link](https://xd.adobe.com/view/e12445c5-9c40-40c8-4a5c-7f21ebde2c3f-9715/)

## 5. Role

| Name | Assigned task |
| ------ | ------ |
| Linda | Backend |
| Jinu | Backend |
| Yunnie | Backend |


# Configuration/Execution
## Configuration
`honsuri-backend` Execute the code below within the folder
```
python -m venv Virtual environment name
source Virtual environment name/bin/activate
pip install -r requirements.txt
```
my_settings.py Add File
## Execution method
### Backend
`honsuri-backend` Run the virtual environment within the folder and then run the code below
```
./manage.py runserver
```
