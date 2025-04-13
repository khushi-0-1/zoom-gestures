# Zoom Gestures 


## Installation and Implementation

### Environment Setup
```bash
python3 -m venv zoom-gestures
source zoom-gestures/bin/activate
pip3 install -r requirements.txt
```

### Virtual Camera Setup

Install [v4l2loopback](https://github.com/umlaeute/v4l2loopback.git)

```bash
sudo modprobe v4l2loopback
```

### Run the main file

```bash
python3 main.py
```

