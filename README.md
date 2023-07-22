# Broadband Speed Logger ⏱️

Welcome to the Broadband Speed Logger project! This application is built to monitor and log your internet download/upload speed at regular intervals. It's particularly suited for devices like a Raspberry Pi.

## Overview 📝

Broadband Speed Logger is a potent tool for tracking your internet speed metrics. This application leverages the power of "speedtest-cli" to capture data and provides a user-friendly HTML/JavaScript webserver interface to display the results. Moreover, it uses cron for scheduling regular checks, making it an ideal solution for continuous monitoring on systems like a Raspberry Pi.

## Features 🎮

- Regular internet speed logging
- Local HTML / JavaScript interface for viewing results
- Scheduling functionality with cron
- Optimized for Raspberry Pi devices
- Manual and automatic running modes

## Technologies Used 💻

This project has been developed using the following technologies:

<code><img height="50" src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-plain.svg" alt="HTML5"></code>
<code><img height="50" src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-plain.svg" alt="JavaScript"></code>
<code><img height="50" src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" alt="Python"></code>
<code><img height="50" src="https://github.com/devicons/devicon/blob/master/icons/ubuntu/ubuntu-plain.svg" alt="Ubuntu"></code>
<code><img height="50" src="https://github.com/devicons/devicon/blob/master/icons/raspberrypi/raspberrypi-original.svg" alt="Raspberry Pi"></code>
<code><img height="50" src="https://github.com/Jack-Development/Jack-Development/blob/main/resources/IntelliJ_Icon.svg" alt="IntelliJ"></code>

## Dependencies 📦

This program is dependent on having [speedtest-cli](https://github.com/sivel/speedtest-cli), [pandas](https://github.com/pandas-dev/pandas), and http.server installed on your Python installation.

If you are having issues loading the modules then you need to ensure you have the following installed in pip:

```
pip3 install speedtest-cli
pip3 install pandas
```

## Usage 🕹️

### Manual

In a manual system, the user will run the python script "[main.py](https://github.com/Jack-Development/broadbandSpeed/blob/main/main.py)" whenever they wish to get a new reading for their speed. This would then be stored under a file with the name "data,[Day],[Month],[Year].csv" in the root directory.

You can run the speed test by executing the following in the root directory:

```
python3 main.py
```

To start the website interface, you can run this command, also in the root directory:

```
python3 -m http.server
```

If this file exists then the results will be appended to the end of the dataframe. If not then a new file will be generated for that day, which can then be appended to at a later time.

### Automatic

If you wish to have the application be run on an independent system, then you can make it automatically query and output the results, without any input from the user.

This can be easily done on a Raspberry Pi, as it is a small system that can run the programs without issue. Many of the instructions are similar to the Manual method.

You can use whichever preferred way you want to run the commands, however I found it easiest to use "[cron](https://en.wikipedia.org/wiki/Cron)", which came preinstalled in the Raspbian OS I was using.

Within cron you can begin to edit the methods you wish to run by executing the follow in the terminal:

```
crontab -e
```

When the file is opened you can add the following commands, which will boot the website on startup in its own thread, and also execute the Python script every 5 minutes:

```
0,*/5 * * * * cd /path/to/file && python3 main.py
@reboot cd /path/to/file && python3 -m http.server &
```

If you wish to edit how frequently the command runs then you can edit the section procedding the command to edit the frequency, you can use [Crontab Guru](https://crontab.guru/) (An online crontab frequency maker) to create your own timings.

With all these enabled you can reboot and the program should begin to log by itself! So even if your Pi loses power you should still be able to recover after power returns!

## Contributions 🤝

Feel free to fork this project, make improvements, and submit pull requests. All contributions are welcome!

## License 📄

This project is licensed under the MIT License. Please see the [LICENSE](LICENSE) file for more details.
