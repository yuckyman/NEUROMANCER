# iOS Shortcut: Send Files to NEUROMANCER Inbox via SSH

This guide shows how to create an iOS Shortcut that automatically sends files (PDFs, images, documents) to your NEUROMANCER inbox using SSH.

## Prerequisites

### 1. SSH Server Setup on Your Machine
Your NEUROMANCER machine needs to be accessible via SSH:

```bash
# Install SSH server (if not already installed)
sudo apt-get install openssh-server

# Enable SSH service
sudo systemctl enable ssh
sudo systemctl start ssh

# Configure SSH for key-based authentication
mkdir -p ~/.ssh
chmod 700 ~/.ssh
```

### 2. SSH Key Setup for iOS
Generate SSH keys on your iOS device and add the public key to your server:

```bash
# On your server, create authorized_keys file
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# Add your iOS public key to this file (you'll get it from the shortcut)
```

### 3. Network Access
Ensure your server is accessible from the internet:
- **Local Network**: Use your local IP (192.168.x.x)
- **Remote Access**: Set up port forwarding or use a service like Tailscale/ZeroTier
- **Security**: Use a non-standard SSH port and fail2ban

## iOS Shortcut Setup

### Step 1: Create New Shortcut
1. Open **Shortcuts** app on iOS
2. Tap **+** to create a new shortcut
3. Add **"Automation"** → **"Create Personal Automation"** → **"Do Not Disturb"** (we'll modify this)

### Step 2: Add File Input
1. Add **"Find Files"** action
2. Configure to accept: **"Ask Each Time"** for file selection
3. Set **"Service"** to **"Files"** and **"iCloud Drive"**

### Step 3: Add SSH Connection
1. Add **"Run SSH Script"** action
2. Configure connection:
   - **Host**: Your server's IP/domain
   - **Port**: 22 (or your custom SSH port)
   - **User**: Your username
   - **Authentication**: **"SSH Key"**
   - **SSH Key**: Generate new key pair

### Step 4: File Transfer Script
Use this script in the **"Run SSH Script"** action:

```bash
#!/bin/bash

# Create inbox directory if it doesn't exist
mkdir -p ~/NEUROMANCER/0_admin/01_inbox

# Generate unique filename with timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
ORIGINAL_NAME="$1"
EXTENSION="${ORIGINAL_NAME##*.}"
BASENAME="${ORIGINAL_NAME%.*}"

# Clean filename (remove special characters)
CLEAN_BASENAME=$(echo "$BASENAME" | sed 's/[^a-zA-Z0-9_-]/_/g')
NEW_FILENAME="${TIMESTAMP}_${CLEAN_BASENAME}.${EXTENSION}"

# Move file to inbox
mv "$1" "~/NEUROMANCER/0_admin/01_inbox/$NEW_FILENAME"

echo "File uploaded: $NEW_FILENAME"
```

### Step 5: Handle File Transfer
1. Add **"Get Details of Files"** action
2. Select **"File Path"** and **"Name"**
3. Add **"Run SSH Script"** with the script above
4. Pass the file path as an argument

### Step 6: Add Notifications
1. Add **"Show Notification"** action
2. Title: **"File Sent to NEUROMANCER"**
3. Body: **"File uploaded successfully"**

## Complete Shortcut Flow

```
┌─────────────────┐
│   Select File   │ ← User selects PDF/image/document
└─────────────────┘
         │
         ▼
┌─────────────────┐
│  Get File Path  │ ← Extract file path for SSH
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   SSH Transfer  │ ← Send file to server inbox
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Notification  │ ← Confirm successful upload
└─────────────────┘
```

## Advanced Features

### 1. Batch File Upload
Modify the shortcut to handle multiple files:

```bash
#!/bin/bash

mkdir -p ~/NEUROMANCER/0_admin/01_inbox

for file in "$@"; do
    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
    ORIGINAL_NAME=$(basename "$file")
    EXTENSION="${ORIGINAL_NAME##*.}"
    BASENAME="${ORIGINAL_NAME%.*}"

    CLEAN_BASENAME=$(echo "$BASENAME" | sed 's/[^a-zA-Z0-9_-]/_/g')
    NEW_FILENAME="${TIMESTAMP}_${CLEAN_BASENAME}.${EXTENSION}"

    mv "$file" "~/NEUROMANCER/0_admin/01_inbox/$NEW_FILENAME"
    echo "Uploaded: $NEW_FILENAME"
done
```

### 2. File Type Validation
Add validation to only accept supported file types:

```bash
#!/bin/bash

SUPPORTED_TYPES=("pdf" "docx" "doc" "txt" "png" "jpg" "jpeg")

# Check file extension
EXTENSION="${1##*.}"
if [[ ! " ${SUPPORTED_TYPES[@]} " =~ " ${EXTENSION} " ]]; then
    echo "Error: Unsupported file type .$EXTENSION"
    exit 1
fi

# Continue with upload...
```

### 3. Metadata Extraction
Extract and send file metadata:

```bash
#!/bin/bash

# Get file info
FILE_SIZE=$(stat -f%z "$1" 2>/dev/null || stat -c%s "$1")
MODIFIED_DATE=$(stat -f%Sm -t "%Y-%m-%d %H:%M:%S" "$1" 2>/dev/null || date -r "$1" +"%Y-%m-%d %H:%M:%S")

# Create metadata file
METADATA_FILE="${1}.metadata"
cat > "$METADATA_FILE" << EOF
Original Name: $(basename "$1")
Size: $FILE_SIZE bytes
Modified: $MODIFIED_DATE
Uploaded: $(date +"%Y-%m-%d %H:%M:%S")
EOF

# Upload both files
# ... rest of upload script
```

## Security Considerations

### 1. SSH Key Management
- Use strong passphrases for SSH keys
- Regularly rotate keys
- Store keys securely on iOS device

### 2. Network Security
- Use VPN when on public networks
- Consider SSH tunneling for additional security
- Monitor SSH access logs

### 3. File Permissions
```bash
# Set proper permissions on inbox directory
chmod 755 ~/NEUROMANCER/0_admin/01_inbox
```

## Testing Your Setup

### 1. Test SSH Connection
```bash
# Test from another machine
ssh -i ~/.ssh/your_key user@your-server "echo 'SSH connection successful'"
```

### 2. Test File Upload
1. Create a test file on iOS
2. Run the shortcut
3. Check if file appears in `/home/ian/NEUROMANCER/0_admin/01_inbox/`
4. Run the processing script to verify it works

### 3. Test Processing Pipeline
```bash
cd /home/ian/NEUROMANCER/0_admin/07_scripts
python process_inbox.py
```

## Troubleshooting

### Common Issues:

1. **"Connection failed"**
   - Check SSH server is running: `sudo systemctl status ssh`
   - Verify firewall settings
   - Test network connectivity

2. **"Permission denied"**
   - Check SSH key is in `~/.ssh/authorized_keys`
   - Verify file permissions: `chmod 600 ~/.ssh/authorized_keys`

3. **"File not found"**
   - Check inbox directory exists and has correct permissions
   - Verify file paths in the shortcut

4. **"Processing failed"**
   - Check Python dependencies are installed
   - Verify Ollama is running
   - Check file permissions

## Integration with NEUROMANCER

Once files are uploaded, they will be automatically processed by the enhanced `process_inbox.py` script:

- **PDFs**: Text extracted using PyMuPDF
- **Word Docs**: Text extracted using python-docx
- **Images**: OCR text extraction using Tesseract
- **Text Files**: Direct processing with URL scraping
- **Metadata**: AI-generated tags and summaries via Ollama
- **Output**: Structured markdown files in `1_ideas/`

This creates a seamless pipeline from iOS device → SSH upload → AI processing → knowledge base integration.