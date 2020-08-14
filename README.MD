# Sonar Parse Project

![Alt text](assets/ui_preview.png?raw=true)

End to end solution to extract, transform, load data from a downstream datasource into a modular lightweight web application powered by ReactJS, Tornado, and MongoDB. 

### Architecture 

![Alt text](assets/architecture.png?raw=true)

The hardest architecture decision was ultimately which database to use to collect the data. One of the reasons I went with Mongo was due to the nature of the data - JSON data and the requirement to query the data for specific value patterns. These both play to the strengths of Mongo and with the right indexing pattern can result in fast, efficient data retrieval.

### Installation

Clone or download the package: 

``` bash
git clone https://github.com/MalwareSec/Sonar-Analysis.git
```

or for older versions of git

``` bash
git lfs clone https://github.com/MalwareSec/Sonar-Analysis.git
```

Build and create necessary containers:

``` bash
docker-compose up --build -d
```

Note: This step will take a couple of minutes, once all of the containers have been built, the ETL process is kicked off and within minutes should have populated the database.

To visit the UI, navigate to:

``` bash
http://localhost:3000/
```

### API

![Alt text](assets/postman.png?raw=true)

The API supports one main route and a health check. The postman collection can be downloaded from the /assests folder. 

``` json
{
    "name": "Health Check",
    "request": {
        "method": "GET",
        "header": [],
        "url": {
            "raw": "http://localhost:8080/health-check",
            "protocol": "http",
            "host": [
                "localhost"
            ],
            "port": "8080",
            "path": [
                "health-check"
            ]
        }
    },
    "response": []
},
{
    "name": "Get Records Post",
    "request": {
        "method": "POST",
        "header": [],
        "body": {
            "mode": "raw",
            "raw": "{\"search\": \"incapsula.com\"}"
        },
        "url": {
            "raw": "http://localhost:8080/records",
            "protocol": "http",
            "host": [
                "localhost"
            ],
            "port": "8080",
            "path": [
                "records"
            ]
        }
    },
    "response": []
}
```

And similarly can be queried via curl:

``` bash
curl --location --request POST 'http://localhost:8080/records' \
--header 'Content-Type: text/plain' \
--data-raw '{"search": "incapsula.com"}'
```

Note: The API does not currently implement pagination. This results in records being returned in full and a less than ideal user experience when a query is performed that results in > 10,000 records that are all trying to be loaded on a single page. Given more time, this could be solved through pagination on the API side and parallax scrolling on the UI.

### Testing

``` bash
cd sonar_parse_etl
python -m unittest
``` 


