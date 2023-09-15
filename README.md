Sensor-Fault-Detection

Problem Statement

The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.
This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.

Solution Proposed

In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.
The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

Tech Stack Used

1.	Python
2.	Machine learning algorithms
3.	Docker
4.	MongoDB

Infrastructure Required
1.	AWS S3
2.	AWS EC2
3.	AWS ECR
4.	Git Actions


### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```
GIT Commands
New project using git

git init  // to initialize git in the source code
git clone <github_url>// to clone xisting github repo
git add file_name /to add ur changes made in file to git stagging area
git commit -m "message /create commits
git push origin main // origin contains url to github repo ; main >> branch name 

git pull origin main // to pull changes from github repo
