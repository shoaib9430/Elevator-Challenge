# Elevator
Elevator management system using Rest Apis

## Installation
1. Running locally
    - Clone the repository
    - Create a virtual environment
    - Activate the virtual environment and install the requirements
    - Run the server
   ```bash
    - git clone
    - cd ElevatorX
    - virtualenv venv
    - source venv/bin/activate
    - pip install -r requirements.txt
    - python manage.py runserver
    ```
2. Prod ready app using docker
    - Clone the repository
    - Run the docker-compose file
    ```bash
    - git clone
    - cd ElevatorX
    - docker-compose up -d --build
    ```
   
## Postman Collection
- [Postman Collection](https://api.postman.com/collections/17813279-9e4ed033-9914-4d74-998a-e9b6168df077?access_key=PMAT-01H1E4204J1AQQP8KFJ04VMQV0)

## Project Structure
```
.
├── Dockerfile
├── README.md
├── docker-compose.yml
├── ElevatorX
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models
│   │   ├── __init__.py
│   │   ├── elevator.py
│   │   ├── elevator_request.py
│   │   └── elevator_system.py
│   ├── serializers
│   │   ├── __init__.py
│   │   ├── elevator_serializer.py
│   │   ├── elevator_request_serializer.py
│   │   └── elevator_system_serializer.py
│   ├── viewsets
│   │   ├── __init__.py
│   │   ├── elevator_request_viewset.py
│   │   ├── elevator_system_viewset.py
│   │   └── elevator_viewset.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
└── erd.png
```

## Thought Process
- The elevator system has a name, number of elevators and number of floors
- An elevator system can have many elevators signifying one-to-many relationship
- An elevator has a number, current floor, direction, next stop, is door open, is operational
- An elevator has a one to many relationship with the requests. 

### Design thought
  - First, I tried to design with considering only one elevator systems where I will store N objects for elevators depincting an elevator system.
  - But I realised that the above approach might not be scalable as this app will only depict one elevator system and will have to destroy all elevators when creating a new one. 
  - Then I created seprate model for Elevator System and Elevator. This way I can create multiple elevator systems and each elevator system can have multiple elevators.

### Assumptions
- The elevator system is created with a name, number of elevators and number of floors
- The elevator system is created with all the elevators in the system in the ground floor
- The elevator system is created with all the elevators in the system in operational state
- Upon recieving request, system will assign the nearest elevator to the requested floor
   
## Usage

1. Create new elevator system
    - Endpoint: ```POST  /api/v1/elevator-systems/```
    - Request body:
    ```json
    {
        "system_name": "Homeland",
        "number_of_elevators": "2",
        "number_of_floors": "6"
    }
    ```

2. Get elevator system info
    - Endpoint: ```GET  /api/v1/elevator-systems/<system-name>```
    - Lists all the elevators in the system and their current status
    
3. Create elevator request
    - Endpoint: ```POST  /api/v1/elevator-systems/<system-id>/create-elevator-request```
    - Request body:
    ```json
    {
      "requested_from_floor": 5,
      "requested_to_floor": 3
    }
    ```
   
4. Get elevator requests
    - Endpoint: ```GET  /api/v1/elevator-systems/<system-id>/elevators/<selevator-id>/requests/```
    - Lists all the requests made to the elevator

5. Get elevator request
    - Endpoint: ```GET  /api/v1/elevator-systems/<system-id>/elevators/<elevator-id>/status/```
    - Responds with the current status of the elevator, current_floor, direction, next_stop, etc.

6. Update elevator info
    - Endpoint: ```PATCH  /api/v1/elevator-systems/2/elevators/3/```
    - Request body:
    ```json
    {
      "id": 3,
      "elevator_number": 1,
      "current_floor": 1,
      "is_door_open": false,
      "direction": -1,
      "is_operational": false,
      "elevator_system": 2
    }
    ```
#
