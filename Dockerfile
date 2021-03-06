FROM python:3.7 

# Install NodeJS
RUN apt-get update
RUN apt-get install nodejs -y

# RUN curl -L https://www.npmjs.com/install.sh | sh

# # Install Comunica SPARQL
# RUN npm install -g @comunica/actor-init-sparql

# Install pip dependencies
ADD requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8808
ENTRYPOINT [ "python3" ]
CMD [ "src/api.py" ]
