# EvilPackage Testkit

This Python package simulates typical adversary tactics to help assess the effectiveness of Detection and Response 
controls in identifying and mitigating threats posed by malicious Python packages.
 

| Attack Tactic | Attack Technique                                         | Platforms                   | Notes |
|---------------|----------------------------------------------------------|-----------------------------|-------|
| Discovery     | T1592  Gather Victim Host Information                    | Windows, Linux, Darwin      |       |
| Evasion       | T1497.001  Virtualization/Sandbox Evasion: System Checks | Windows, Linux, Darwin      |       | 
| Collection    | T1115  Clipboard Data                                    | Windows, Linux, Darwin      |       | 
| Collection    | T1113  Screen Capture                                    | Windows, Linux, Darwin      |       |  
| Collection    | T1539  Steal Web Session Cookie                          | Windows(TBD), Linux, Darwin |       | 
| Execution     | T1059.006  Command and Scripting Interpreter: Python     | Windows(TBD), Linux, Darwin |       |
| Exfiltration  | T1567.004 Exfiltration Over Webhook (TBD)                | Windows, Linux, Darvin      |       |
| Exfiltration  | T1567.003 Exfiltration to Text Storage Sites (TBD)       | Windows, Linux, Darvin      |       | 
| Persistence   | T1547.013 Linux persistence with .config/autostart       | Linux                       |       |
| Persistence   | T1546.004 Unix Shell Configuration Modification          | Linux                       |       |  
| Persistence   | T1053.005 Windows persistence with schtask (TBD)         | Windows                     |       | 


## Disclaimer

This package is meant for testing and educational purposes only, and should not be used for malicious activities. 
Also, ensure to follow all ethical guidelines and legal regulations in your area related to ethical hacking and cybersecurity.


# Usage

1. Install the package from the repository

```shell
git clone git@github.com:petermat/evil-package.git
pip install ./evil_package
```

2. Observe execution of listed Attack Techniques

3. Tune your Detection and Response until happy with the results. 


