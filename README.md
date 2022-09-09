# Text_forecast
App that send a text with the forecast of the next nine hours.

## Description

This app, run on a linux server, send the forecast to a phone number. It download the weather information from the openweathermap API. It send a text using the Twillio APi. The server run the program using CRON.

## Getting Started

### Dependencies

* openweathermap API 3.0
* Twilio package 7.13

### Installing

* Install the app on a linux server /usr/local/bin
*

### Executing program

* use Cron to run the app at the time you want to receive the text
* Step-by-step bullets
```
* run a linux shell
* type crontab -e
* select a text editor if it is the first time
* type the line : minutes hour day-of-the-month month-day-of-the-week send_forecast.py "City"
* chmod +x send_forecast.py
```

## Help
Sometimes, there is a problem and the python script is not executable. Type the problem on google, there is a solution.


## Authors

Emmanuel Guefif

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
