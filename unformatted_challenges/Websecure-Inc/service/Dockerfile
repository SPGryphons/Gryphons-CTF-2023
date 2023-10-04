# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json first for caching purposes
COPY WebSecure-Inc-Challenge/package*.json ./

# Install application dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY WebSecure-Inc-Challenge .

# Specify the port the app runs on
EXPOSE 3000

# Command to run the application
CMD [ "node", "server.js" ]
