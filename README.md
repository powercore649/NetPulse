# Broadband Speed Logger

An application designed to be run on a device such as a Raspberry Pi.

Intended to be used to log internet Download / Upload speed at regular intervals.

Made up of three components:
* Python - Based on "speedtest-cli"
* HTML / JavaScript webserver
* cron

## Skills Used

<code><img height="50" src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-plain.svg" alt="html"></code>
<code><img height="50" src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-plain.svg" alt="javascript"></code>
<code><img height="50" src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" alt="python"></code>

<code><img height="50" src="https://github.com/devicons/devicon/blob/master/icons/ubuntu/ubuntu-plain.svg" alt="ubuntu"></code>
<code><img height="50" src="https://github.com/devicons/devicon/blob/master/icons/raspberrypi/raspberrypi-original.svg" alt="raspberry"></code>
<code><img height="50" src="https://github.com/Jack-Development/Jack-Development/blob/main/resources/IntelliJ_Icon.svg" alt="IntelliJ"></code>

## Dependencies

This program is dependent on having [speedtest-cli](https://github.com/sivel/speedtest-cli), [pandas](https://github.com/pandas-dev/pandas), and http.server installed on your Python installation.

If you are having issues loading the modules then you need to ensure you have the following installed in pip:

```console
pip3 install speedtest-cli
pip3 install pandas
```

## Development Info

This application can be run in two seperate ways. Manual and automatic.

### Manual

In a manual system the user will run the python script "[main.py](https://github.com/Jack-Development/broadbandSpeed/blob/main/main.py)" whenever they wish to get a new reading for their speed.
This would then be stored under a file with the name "data,[Day],[Month],[Year].csv" in the root directory.#

You can run the speed test by executing the following in the root directory:

```console
python3 main.py
```

To start the website interface you can run this command, also in the root directory:
```console
python3 -m http.server
```

If this file exists then the results will be appended to the end of the dataframe. If not then a new file will be generated for that day, which can then be appended to at a later time.

### Automatic

If you wish to have the application be run on an independent system, then you can make it automatically query and output the results, without any input from the user.

This can be easily done on a Raspberry Pi, as it is a small system that can run the programs without issue. Many of the instructions are similar to the Manual method.

You can use whichever preferred way you want to run the commands, however I found it easiest to use "[cron](https://en.wikipedia.org/wiki/Cron)", which came preinstalled in the Raspbian OS I was using.

Within cron you can begin to edit the methods you wish to run by executing the follow in the terminal:

```console
crontab -e
```

When the file is opened you can add the following commands, which will boot the website on startup in its own thread, and also execute the Python script every 5 minutes:

```console
*/5 * * * * cd /path/to/file && python3 main.py
@reboot cd /path/to/file && python3 -m http.server &
```

If you wish to edit how frequently the command runs then you can edit the section procedding the command to edit the frequency, you can use [Crontab Guru](https://crontab.guru/) (An online crontab frequency maker) to create your own timings.

With all these enabled you can reboot and the program should begin to log by itself! So even if your Pi loses power you should still be able to recover after power returns!
