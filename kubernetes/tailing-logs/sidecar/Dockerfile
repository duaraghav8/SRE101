FROM busybox

# Copy the script into the container
COPY sidecar-script.sh /sidecar-script.sh

# Make the script executable
RUN chmod +x /sidecar-script.sh

# Run the script
CMD ["/sidecar-script.sh"]
