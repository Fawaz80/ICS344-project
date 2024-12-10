# Splunk Universal Forwarder Setup

    ## Installation
    - Download from [Splunk Website](https://www.splunk.com).
    - Install using:
      bash
      dpkg -i splunkforwarder*.deb
      

    ## Configuration
    - Add inputs in `inputs.conf`:
      
      [monitor:///var/log/honeypots/]
      sourcetype=honeypot_logs
      
    - Add outputs in `outputs.conf`:
      
      [tcpout]
      defaultGroup = default-autolb-group
