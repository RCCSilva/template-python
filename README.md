# Python Template

```shell
sudo apt-get update
sudo apt-get install python3-venv
```

## Python Setup

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Database Setup

```shell
chmod +x ./scripts/reset_database.sh
sudo ./scripts/reset_database.sh
```