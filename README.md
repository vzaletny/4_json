# Prettify JSON

This application gets any raw JSON file and prints it on the screen in convenient format

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash
$ python pprint_json.py <path to JSON file>
```
Launch on Windows do the same way

For instance:

```bash
python pprint_json.py c:\Temp\alco_shops.json

{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "properties": {
                "Attributes": {
                    "Address": "улица Академика Павлова, дом 10",
                    "AdmArea": "Западный административный округ",
                    "ClarificationOfWorkingHours": null,
                    "District": "район Кунцево",
                    "IsNetObject": "да",
                    "Name": "Ароматный Мир",
                    "OperatingCompany": "Ароматный Мир",
                    "PublicPhone": [
                        {
                            "PublicPhone": "(495) 777-51-95"
                        }

```



You can use -h option to get some help

```bash
python pprint_json.py -h
usage: pprint_json.py [-h] JSON file

Pretty print any raw JSON file

positional arguments:
  JSON file   Path to incoming raw JSON file

optional arguments:
  -h, --help  show this help message and exit

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
