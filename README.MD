# EvilPackage Testkit

This Python package simulates typical adversary tactics to help assess the effectiveness of Detection and Response 
controls in identifying and mitigating threats posed by malicious Python packages.
 

| Attack  Tactic | Attack Technique                                         | Platforms                   | Notes |
|----------------|----------------------------------------------------------|-----------------------------|-------|
| Discovery      | T1592  Gather Victim Host Information                    | Windows, Linux, Darwin      |       |
| Evasion        | T1497.001  Virtualization/Sandbox Evasion: System Checks | Windows, Linux, Darwin      |       | 
| Collection     | T1115  Clipboard Data                                    | Windows, Linux, Darwin      |       | 
| Collection     | T1113  Screen Capture                                    | Windows, Linux, Darwin      |       |  
| Collection     | T1539  Steal Web Session Cookie                          | Windows(TBD), Linux, Darwin |       | 
| Execution      | T1059.006  Command and Scripting Interpreter: Python     | Windows(TBD), Linux, Darwin |       |
| Exfiltration   | T1567.004 Exfiltration Over Webhook                      | (TBD)                       |       |
| Exfiltration   | T1567.003 Exfiltration to Text Storage Sites             | (TBD)                       |       | 
| Persistence    | T1547.013 Linux persistence with .config/autostart       | Linux                       |       |
| Persistence    | T1546.004 Unix Shell Configuration Modification          | Linux                       |       |  
| Persistence    | T1053.005 TBD windows persistence with schtask           | Windows(TBD)                |       | 


## Disclaimer

This package is meant for testing and educational purposes only, and should not be used for malicious activities. 
Also, ensure to follow all ethical guidelines and legal regulations in your area related to ethical hacking and cybersecurity.


# Usage

Install the package as from pip

```shell
pip install evil_package
```

or manually

```shell
pip install ...
```




