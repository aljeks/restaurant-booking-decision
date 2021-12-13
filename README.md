# restaurant-booking-decision
ML project based on Zomato API data to select restaurant to visit

### Problem description

Zomato API Analysis is one of the most useful analysis for foodies who want to taste the best cuisines of every part of the world which lies in their budget. 
This analysis is also for those who want to find the value for money restaurants in various parts of the country for the cuisines. 
Additionally, this analysis caters the needs of people who are striving to get the best cuisine of the country and which locality of that country serves that cuisines with maximum number of restaurants.

Main goal of this project is to get prediction of probability (0,1) for the question: Do I have to book a table in the restaurant with these features?
After asking the model with your set of features you will get the result.
For example: yes, you have to visit this restaurant with proba = 0.83

I hope you will have the best expirience with the recommended restaurant and enjoy the best cuisine in the city.

### What data do I use

All Data has been collected from the Zomato API. The collected data has been stored in the Comma Separated Value file Zomato.csv

You can get access to this from Kaggle: https://www.kaggle.com/akashram/zomato-restaurants-autoupdated-dataset/version/1?select=zomato.csv

Each restaurant in the dataset is uniquely identified by its Restaurant Id Every Restaurant contains the following variables:

• Restaurant Id: Unique id of every restaurant across various cities of the world 

• Restaurant Name: Name of the restaurant 

• Country Code: Country in which restaurant is located 

• City: City in which restaurant is located 

• Longitude: Longitude coordinate of the restaurant's location 

• Latitude: Latitude coordinate of the restaurant's location 

• Cuisines: Cuisines offered by the restaurant 

• Average Cost for two: Cost for two people in different currencies

• Currency: Currency of the country 

• Has Table booking: yes/no 

• Has Online delivery: yes/ no 

• Is delivering: yes/ no 

• Price range: range of price of food 

• Aggregate Rating: Average rating out of 5 

• Votes: Number of ratings casted by people



### Dependency and enviroment management and run
To install the dependencies and activate the env execute on linux:

#pipenv install scikit-learn==1.0 numpy flask gunicorn

#pipenv run gunicorn --bind 0.0.0.0:9696 predict:app


Also you can run pre-installed jupyter-notebook for better UI

#jupyter-notebook


Don't forget to clone project from git

#git clone https://github.com/aljeks/restaurant-booking-decision.git


Then just open address http://localhost:8888/ in your browser (jupyter-notebook or Anaconda should be up)

And enjoy /restaurant-booking-desision/notebook.ipynb

### Containerization and run
Dockerfile is provided with the git project

To build docker container run:

#sudo docker build -t predict .

To run just builded container run:

#sudo docker run -it --rm -p 9696:9696 predict


### Cloud deployment

At first you have to get your AWS cloud machine.

Read more about this here https://mlbookcamp.com/article/aws 
and here https://mlbookcamp.com/article/aws-ec2

Don't forget to setup security settings in AWS console and open TCP 9696 port

Using address of your server navigate there

#ssh -i "jupiter.pem" ubuntu@ec2-18-222-227-70.us-east-2.compute.amazonaws.com


If you on your AWS ec2 server just clone your project from git

#git clone https://github.com/aljeks/restaurant-booking-decision.git


Then build docker container with all files provided:

#sudo docker build -t predict .


And finally run docker instance

#sudo docker run -d --rm -p 9696:9696 predict


(Optional) If you want to get inside container for some reason run it like

#sudo docker run -it --rm --entrypoint=bash predict


After this you can send a POST request to the cloud via jupyter notebook 

'restaurant-booking-decision/notebook.ipynb'

It's in the bottom of the file with the label: 'Test example with request to AWS cloud service'

Or just run this curl from terminal, for example Cygwin:

#
curl --location --request POST 'http://ec2-18-222-227-70.us-east-2.compute.amazonaws.com:9696/predict' --header 'Content-Type: application/json' --data-raw '{"restaurant_name": "via_delhi", "country_code": 214, "city": "abu_dhabi", "longitude": 54.374273233100006, "latitude": 24.4910933909, "cuisines": "indian,north_indian,chinese", "average_cost_for_two": 100, "currency": "emirati_diram(aed)", "has_table_booking": 0, "has_online_delivery": 1, "is_delivering_now": 1, "price_range": 3, "votes": 1148}'




