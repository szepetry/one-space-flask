#!/bin/bash
# Start the ssh-agent
eval "$(ssh-agent -s)"

# Add the SSH key stored in the environment variable
echo "$SSH_PRIVATE_KEY" | tr -d '\r' | ssh-add -

# Disable host key checking
export GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"

# Run your original build command
python run.py
