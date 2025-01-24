# Use the official Grafana image from Docker Hub
FROM grafana/grafana:latest

# Expose the default Grafana port (3000)
EXPOSE 3000

# Command to run Grafana (this is the default entrypoint in the Grafana image)
CMD ["/bin/bash", "-c", "/bin/grafana-server"]
