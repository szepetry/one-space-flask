#!/bin/bash
# Decode the SSH private key from a single line to the original format
echo "$SSH_PRIVATE_KEY" | tr -d '\r' | sed 's/\\n/\n/g' > /tmp/decoded_key

# Ensure the key has the correct permissions
chmod 600 /tmp/decoded_key

# Start the ssh-agent
eval "$(ssh-agent -s)"

# Add the SSH key stored in the temporary file
ssh-add /tmp/decoded_key

# Debugging SSH connections
export GIT_SSH_COMMAND="ssh -vvv -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no"

# Run your Flask application
python run.py
