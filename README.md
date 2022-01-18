# Finder Project

This project is developed to scrap data from few sites. They are give here:
1. www.ciranet.com
2. https://secure.condocerts.com
3. https://estoppels.com/
4. https://secure.welcomelink.com (first finder)
5. https://www.homewisedocs.com
6. https://sentry.welcomelink.com
7. https://marketplace.communityarchives.com

This project is developed with django 3.2.11 and python version 3.7.7, selenium and beutifulsoap. 
This project containing updated version of chrome browser which is updating from code.

requirements file is included in this repository named rr.txt

# urls description:
1. http://finder.inspecthoa.com/admin <br> 
  This url is to login as admin, and check the data which is saved to db.
2. http://finder.inspecthoa.com/swagger/ <br> 
  This link is used as live postman developed with django swagger. From this link you can test API's, <br> 
  and know what is the data format of this API's. 
3. http://finder.inspecthoa.com/redoc/ <br> 
   From this link you can also know what is the data format of this API's.
4. http://finder.inspecthoa.com/api/address/ <br>
   When you want to get property detains from http://finder.inspecthoa.com you need to send data to this api link. <br>
   This link will return you as much as data, application can retrive.
   
   # Data Format 
   { <br>
    "address":"8236 SW 1st St, Blue Springs, MO 64014"  <br>
   }
   
   This "address" is required. And you need to pass the data format like: "Street, City, Zip_State, State Zip_Code".
  
# Model 
In This project there is a Model/ Table called LocationModel <br>
This model is used to store data of each search opration, in this website. <br> 
This Model/table containing 2 fields. One is "address" and other is "json_data"
  # 1. address: <br>
    is used to save which address is searched by an user.
  # 2. json_data: <br> 
    is used to store the search result of each seach action. 
