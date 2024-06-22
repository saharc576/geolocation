## Instructions
#### Prerequisites  
Make sure you have docker installed on your machine

#### Run
- Clone this project
- Simply run the following command `docker-compose up --build dream`.
- Access the Swagger using the browser at `localhost:8123/docs`
- Trigger the endpoint with whatever request id and ip you'd like, and receive the enriched data.


### Tests Plans
Test using pytest & unittests

##### Caching
- Mock the ip-geolocation external service 
- Assert it is called only once on several consecutive calls (due to caching)

#### Correctness
- Create multiple test cases with ips from all around the world.
- Call the endpoint
- Assert the response is correct
