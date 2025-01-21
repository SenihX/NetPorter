

## **How to Install and Use PortCraft**

### **What is PortCraft?**  
**PortCraft** is a powerful tool used to scan network ports and identify open ports and services. It is ideal for individuals interested in network security and penetration testing.


### **Using PortCraft on Termux**

1. **Update Termux**  
   Start by updating Termux:  
   ``apt update && apt upgrade -y``

2. **Install Required Packages**  
   Install Git and Python with the following command:  
   ``pkg install git python -y``

3. **Clone the PortCraft Repository**  
   Clone the GitHub repository to your Termux environment:  
   ``git clone https://github.com/SenihX/PortCraft.git``

4. **Navigate to the Directory and Install Dependencies**  
   Change to the PortCraft directory and install the required dependencies:  
   ``cd PortCraft``  
   ``pip install -r requirements.txt``

5. **Run PortCraft**  
   Start the tool by executing:  
   ``python3 portcraft.py``


### **Using PortCraft on Kali Linux**

1. **Update the System**  
   Update your Kali Linux system using:  
   ``sudo apt update && sudo apt upgrade -y``

2. **Install Required Packages**  
   Install Git and Python3:  
   ``sudo apt install git python3 python3-pip -y``

3. **Clone the PortCraft Repository**  
   Clone the GitHub repository with the following command:  
   ``git clone https://github.com/SenihX/PortCraft.git``

4. **Navigate to the Directory and Install Dependencies**  
   Change to the PortCraft directory and install dependencies:  
   ``cd PortCraft``  
   ``pip3 install -r requirements.txt``

5. **Run PortCraft**  
   Execute the following command to run PortCraft:  
   ``python3 portcraft.py``
