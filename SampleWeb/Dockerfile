#Depending on the operating system of the host machines(s) that will build or run the containers, the image specified in the FROM statement may need to be changed.
#For more information, please see https://aka.ms/containercompat

FROM microsoft/aspnetcore:2.0-nanoserver-1803 AS base
WORKDIR /app
EXPOSE 8008

FROM microsoft/aspnetcore-build:2.0-nanoserver-1803 AS build
WORKDIR /src
COPY ["sampleweb.csproj", "./"]
RUN dotnet restore "./sampleweb.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "sampleweb.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "sampleweb.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "sampleweb.dll"]
