
doc = '''
#%RAML 1.0
title: python-12
mediaType:  application/json
baseUri: http://localhost/challengeapi{version}
version: 0.0.1
protocols: [HTTP, HTTPS]
securitySchemes:
  JWT:
    description: API request auth by OAuth 2.0.
    type: OAuth 2.0
    describedBy:
      headers:
        Authorization:
          type: string
      responses:
        400:
          description: 
            Unauthorized
    settings:
      signatures : ['HMAC-SHA256']

types:
  Auth:
    type: object
    discriminator: token
    properties: 
        token: string

  Agent:
    type: object
    discriminator: agent_id
    properties: 
      agent_id: integer
      user_id: integer
      name: 
        type: string
        maxLength: 50
      status: boolean
      environment:
        type: string
        maxLength: 20
      version: 
        type: string
        maxLength: 20
      address: 
        type: string
        maxLength: 39
    example:
        agent_id: 5
        user_id: 6
        name: Arthur Dent
        status: true
        environment: Marvin
        version: 0.0.1
        address: example.com

  User:
    type: object
    discriminator: user_id
    properties:
      user_id: integer
      name:
        type: string
        maxLength: 50
      email:
        type: string
        maxLength: 254
      password:
        type: string
        maxLength: 50
      last_login:
        type: date-only
      group_id: integer
        
  Group:
    type: object
    discriminator: group_id
    properties: 
      group_id: integer
      name:
        type: string
        maxLength: 20
    example:
      group_id: 3
      name: coracao_de_ouro

  Event:
    type: object
    discriminator: event_id
    properties:
      event_id: integer
      agent_id: integer
      level: 
        type: string
        maxLength: 20
      payload: string
      shelved: boolean
      data: datetime-only
    example:
      event_id: 4
      agent_id: 2
      level: admin
      payload: request
      shelve: false 

/auth/token:
  post:
    description: show the token
    body:
      application/json:
        username: string
        password: string
    
    responses:
      200:
        body:
          application/json:
            type: Auth
      400:
        body:
          application/json: 
              {"error": "Error"}         
      
/agents:
  get:
    description: show all agents
    securedBy: JWT
    
    responses:
      200:
        body:
          application/json:
            example: response {[
                "agent_id" => 1, 
                "agent_name" => "Ford"],[
                "agent_id" => 2, 
                "agent_name" => "Douglas"],
                }
      400:
        body:
          application/json: 
              {"error": "unauthorized"}
  post:
    description: add new agent
    securedBy: JWT
    body:
      application/json:
        properties:
          name:
            type: string
            maxLength: 50
          status:
            type: bool
          environment:
            type: string
            maxLength: 20
          version:
            type: string
            maxLength: 5
          address:
            type: string
            maxLength: 39
          example: 
            {"name": "Zaphod",
            "status": true,
            "environment": "MARVIN",
            }  
            

  /{id}:
    get:
      description: search agent by id
      securedBy: JWT
      responses: 
        200:
          body:
            application/json: 
                response{agent[]}
        400:
          body:
            application/json: 
              {"error": "Unauthorized"}
        404:
          body:
            application/json: 
              {"error": "Bad Request"}
    
  /{id}/events:
      get:
        description: search a event by agent' id
        securedBy: JWT
        responses:
          200:
            body:
              application/json: 
                response{Event[]}
          400:
            body:
              application/json: 
                {"error": "Unauthorized"}
          404:
            body:
              application/json: 
                {"error": "Bad Request"}
        
/groups:
  get:
    description: show all grupos
    securedBy: JWT
    responses: 
      200:
        body: 
          application/json,
                response{Group[]}
      400:
        body:
            application/json:
              example: 
                {"error": "unauthorized"}
  post:
    description: add new agent
    securedBy: JWT
    body:
      application/json:
        properties:
          name:
            type: string
            maxLength: 20
          example: {
              "name": "coracao_de_ouro",
            }  
  /{id}:
    get:
      description: search groups by id
      securedBy: JWT
      responses: 
        200:
          body:
            application/json, 
                response{Event[]}
        400:
          body:
            application/json: 
                {"error": "Unauthorized"}
        404:
          body:
            application/json: 
              {"error": "Bad Request"}
    
/users:
  post:
    description: add new user
    securedBy: JWT
    body:
      application/json:
        properties:
          name:
            type: string
            maxLength: 50
          password:
            type: string
            maxLength: 50
          email:
            type: string
            maxLength: 254
          last_login:
            type: date-only
        example: 
            {"name": "Zaphod",
            "email": "beeblebrox@ogalaxy.com",
            "password": "f0urty-Tw0",
            "last_login": "2001-05-11"
            }
    responses:
      200:
        body:
            application/json, 
                response{User[]}            
      400:
        body:
            application/json: 
                {"error": "unauthorized"}
  get:
    description: show all users
    securedBy: JWT
    responses:
      200:
        body:
            application/json, 
                response{User[]}
      400:
        body:
            application/json: 
              {"error": "unauthorized"}

  /{id}:
    get: 
      description: search user by id
      securedBy: JWT
      responses:
        200:
          body:
            application/json, 
                response{User[]}
        400:
          body:
            application/json: 
              {"error": "unauthorized"}
        404:
          body:
            application/json: 
              {"error": "Bad Request"}
'''
