![Postmortem](image.gif)

Postmortem Report: Web Application Outage
Issue Summary
Duration: August 12, 2024, 10:00 AM to August 12, 2024, 2:00 PM (UTC)
Impact: The web application was inaccessible for approximately 4 hours, affecting 60% of users who experienced downtime or transaction failures.
Root Cause: The outage was caused by a misconfiguration in the Nginx server, which blocked incoming connections due to a typo in the configuration file.
Timeline
10:00 AM UTC: Monitoring system detected high latency and triggered an alert.
10:15 AM UTC: An engineer noticed the alert and started investigating the issue.
10:30 AM UTC: Initial investigation focused on potential network issues, including firewall settings.
11:00 AM UTC: Discovered that the Nginx configuration file had a typo causing the issue.
11:30 AM UTC: The incident was escalated to the backend team for further resolution.
12:00 PM UTC: The misconfiguration was corrected and the Nginx server was restarted.
2:00 PM UTC: Service was fully restored, and normal operations resumed.
Root Cause and Resolution
Detailed Cause: The Nginx server configuration contained a typo, which resulted in a blockage of all incoming traffic and caused the application to become inaccessible.
Resolution: The configuration file was updated to correct the typo. After applying the fix, the server was restarted, and service was restored.
Corrective and Preventative Measures
Improvements:
Implement a configuration validation step before changes are applied to the server.
Enhance monitoring to include alerts for configuration issues.
Tasks:
Develop and deploy automated tests for configuration files to catch syntax errors.
Set up alerts for server start failures and other potential misconfigurations.