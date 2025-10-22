FROM node:16
ARG APP_VERSION=1.0
LABEL version="1.0" \
      description="LABEL is metadata, ARG is available while building image (can be passed in --build-arg)"
RUN useradd -m nodeuser
USER nodeuser
RUN echo "Building version $APP_VERSION"
WORKDIR /home/nodeuser/app
VOLUME /home/nodeuser/data
COPY package*.json ./
RUN npm install
COPY index.js ./
CMD ["npm", "start"]
