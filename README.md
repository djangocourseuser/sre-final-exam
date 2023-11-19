# Web Application monitoring by Prometheus (For SRE Final Exam)

This is a setup for familiarize with a Prometheus Monitoring System. Setup includes preconfigred Prometheus and node-exporter instances for monitoring local machine, a sample Web Application (in this particular case a Django Application) as an example of usage Prometheus Client for generating own, custom metrics and a Grafana instance with preconfigured dedicated dashboards, for a nice visualisation of generated Prometheus metrics.

### Requirements:  
- `docker` and `docker-compose` services

### Running:  
1. Clone repository to your local machine.
1. Open terminal and exec command `docker-compose up`.
1. Check your `localhost`.

### Setup specification:
***Prometheus*** instance runs on port `9090`  
***Node exporter*** instance runs on port `9100`  
***Alertmanager*** instance runs on port `9093`  
***Grafana*** instance runs on port `3000`  
*Note: Default credentials are `admin`/`admin `*  
***Web-app*** runs on port `8000`
