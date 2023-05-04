#Base image
FROM node:lts-alpine

#Install serve package
RUN npm i -g serve

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package.json yarn.lock ./

# install project dependencies
RUN yarn

# Copy the project files
COPY . .

# Build the project
RUN yarn build

# Expose a port
EXPOSE 3000

# Executables
CMD [ "serve", "-s", "dist" ]