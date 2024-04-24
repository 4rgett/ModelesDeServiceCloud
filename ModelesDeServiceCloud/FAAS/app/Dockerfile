# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:4-python3.10-appservice
FROM mcr.microsoft.com/azure-functions/python:4-python3.10

ENV LANG=C.UTF-8 \
    ACCEPT_EULA=Y \
    FUNCTIONS_WORKER_RUNTIME=python \
    DOTNET_RUNNING_IN_CONTAINER=true \
    DOTNET_USE_POLLING_FILE_WATCHER=true \
    AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true \
    ASPNETCORE_URLS=http://+:80

COPY requirements.txt /
RUN pip install --upgrade pip &&\
    pip install --no-cache-dir -r /requirements.txt

COPY . /home/site/wwwroot
WORKDIR /home/site/wwwroot

EXPOSE 80