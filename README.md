## Infinity Gallery

### 29/05/2022

## Author

[Winston Musasia]

# Description

A personal gallery application that I display my photos for others to see.Users can search for different categories of photos, copy a link to the photo to share with their friends and also view photos based on the location they were taken.


## Live link


## User Story

* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
* Search for different categories of photos. (ie. Travel, Food)
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.

## Setup and Installation

##### Clone the repository
```bash
git@github.com/BM-Winston/Infinity-Gallery.git
```
##### Install requirements 
```bash
cd Infinity-Gallery pip install -r requirements.txt
```
### Install and activate virtual environment
```bash
python3 -m venv virtual - source env/in/activate
```
 ##### Database  
  SetUp your database. Add user and password, host then make migrations. 
 ```bash 
python manage.py makemigrations gallery
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 

##### Tests 
 ```bash 
 python manage.py test 
```

Open application at '127.0.0.1.8000' at your web browser



## Technologies Used

* Python
* Django
* Heroku
* HTML
* CSS

# Known Bugs


## License
MIT

Authors Information

[musasiawinston@gmail.com]

Winston Musasia (c) 2022





