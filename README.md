# User API Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Endpoints](#endpoints)
   - [User Endpoints](#user-endpoints)
   - [Seller Endpoints](#seller-endpoints)
   - [Order Endpoints](#order-endpoints)
   - [Authentication Endpoints](#authentication-endpoints)
3. [Authentication](#authentication)
4. [Models](#models)
5. [Usage](#usage)

## Introduction
The User Management API is a user management system that provides endpoints for creating and managing users, sellers, and orders. The API uses JSON Web Tokens (JWT) for authentication.

## Endpoints

### User Endpoints
- **POST /createuser/**: Create a new user
- **GET /createuser/**: List all users
- **GET /createuser/{id}/**: Get a user by ID
- **PUT /createuser/{id}/**: Update a user
- **PATCH /createuser/{id}/**: Partially update a user
- **DELETE /createuser/{id}/**: Delete a user

### Seller Endpoints
- **POST /createseller/**: Create a new seller
- **GET /createseller/**: List all sellers
- **GET /createseller/{id}/**: Get a seller by ID
- **PUT /createseller/{id}/**: Update a seller
- **PATCH /createseller/{id}/**: Partially update a seller
- **DELETE /createseller/{id}/**: Delete a seller

### Order Endpoints
- **POST /orders/**: Create a new order
- **GET /orders/**: List all orders
- **GET /orders/{id}/**: Get an order by ID
- **PUT /orders/{id}/**: Update an order
- **PATCH /orders/{id}/**: Partially update an order
- **DELETE /orders/{id}/**: Delete an order

### Authentication Endpoints
- **POST /token/**: Obtain an access token
- **POST /token/refresh/**: Refresh an access token

## Authentication
The API uses JSON Web Tokens (JWT) for authentication. To obtain an access token, send a POST request to `/token/` with your **username** and **password**.


## Models

The API uses the following models:

- **User**: A user object with attributes:
  - `id`: Unique identifier for the user
  - `username`: The username of the user
  - `password`: The password of the user

- **Seller**: A seller object with attributes:
  - `id`: Unique identifier for the seller
  - `user`: The user associated with the seller
  - `products`: A list of products offered by the seller

- **Product**: A product object with attributes:
  - `id`: Unique identifier for the product
  - `name`: The name of the product
  - `price`: The price of the product

- **Purchase**: A purchase object with attributes:
  - `id`: Unique identifier for the purchase
  - `user`: The user making the purchase
  - `product`: The product being purchased
  - `date`: The date of the purchase

- **TokenObtainPair**: A token object with attributes:
  - `access`: The access token
  - `refresh`: The refresh token

---

## Usage

To use the API, follow these steps:

1. **Obtain an access token** by sending a POST request to `/token/` with your **username** and **password**.

2. **Include the access token** in the `Authorization` header of all requests:
   ```bash
   Authorization: Bearer {access_token}

3. You can use the API endpoints to create, read, update, and delete users, sellers, and orders.

---

## Practicing with the API

You can practice using the API with the following tools:

- **Swagger Docs**: Access the Swagger documentation at [http://localhost:8000/doc/](http://localhost:8000/doc/) to explore the API endpoints and test them out.

- **Postman**: Use [Postman](https://www.postman.com/) to send requests to the API endpoints and test their functionality.
