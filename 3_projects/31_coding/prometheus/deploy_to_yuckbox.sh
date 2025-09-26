#!/bin/bash
# prometheus deployment script for yuckbox
# run this from NEUROMANCER to deploy to yuckbox

set -e  # exit on any error

echo "🚀 PROMETHEUS DEPLOYMENT TO YUCKBOX"
echo "=================================="

# configuration
YUCKBOX_USER="ian"  # adjust as needed
YUCKBOX_HOST="yuckbox"  # adjust hostname/ip as needed
YUCKBOX_PATH="/home/ian/prometheus"  # adjust path as needed
LOCAL_PATH="/Users/ian/NEUROMANCER/3_projects/31_coding/prometheus"

echo "📦 preparing deployment package..."

# create deployment directory
mkdir -p prometheus_deploy
cd prometheus_deploy

# copy all prometheus files
cp ../prometheus_monitoring_system.py .
cp ../prometheus_config.py .
cp ../run_prometheus.py .
cp ../requirements_prometheus.txt .
cp ../README_prometheus.md .

# create systemd service file
cat > prometheus.service << 'EOF'
[Unit]
Description=Prometheus Market Intelligence Agent
After=network.target

[Service]
Type=simple
User=ian
WorkingDirectory=/home/ian/prometheus
ExecStart=/usr/bin/python3 /home/ian/prometheus/run_prometheus.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

# create deployment script for yuckbox
cat > deploy_on_yuckbox.sh << 'EOF'
#!/bin/bash
# run this on yuckbox to complete setup

echo "🔧 setting up prometheus on yuckbox..."

# create prometheus directory
mkdir -p /home/ian/prometheus
cd /home/ian/prometheus

# install python dependencies
echo "📦 installing python dependencies..."
pip3 install --user -r requirements_prometheus.txt

# create data directories
mkdir -p prometheus_data
mkdir -p prometheus_logs
mkdir -p prometheus_models

# set up environment variables
echo "🔑 setting up environment variables..."
cat >> ~/.bashrc << 'BASHRC'
# prometheus configuration
export ALPHA_VANTAGE_API_KEY="YOUR_ALPHA_VANTAGE_KEY_HERE"
export PYTHONPATH="/home/ian/prometheus:$PYTHONPATH"
BASHRC

# install systemd service
echo "⚙️ installing systemd service..."
sudo cp prometheus.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable prometheus

# set permissions
chmod +x run_prometheus.py
chmod +x prometheus_monitoring_system.py

echo "✅ prometheus setup complete!"
echo "📝 next steps:"
echo "   1. edit ~/.bashrc and add your alpha vantage api key"
echo "   2. source ~/.bashrc"
echo "   3. sudo systemctl start prometheus"
echo "   4. sudo systemctl status prometheus"
echo "   5. journalctl -u prometheus -f  # to watch logs"
EOF

chmod +x deploy_on_yuckbox.sh

# create rsync command
echo "📤 uploading files to yuckbox..."
rsync -avz --progress . ${YUCKBOX_USER}@${YUCKBOX_HOST}:${YUCKBOX_PATH}/

echo "✅ deployment package uploaded!"
echo ""
echo "🔧 next steps:"
echo "   1. ssh into yuckbox: ssh ${YUCKBOX_USER}@${YUCKBOX_HOST}"
echo "   2. cd ${YUCKBOX_PATH}"
echo "   3. ./deploy_on_yuckbox.sh"
echo "   4. edit ~/.bashrc with your alpha vantage api key"
echo "   5. sudo systemctl start prometheus"
echo ""
echo "📊 monitoring commands:"
echo "   sudo systemctl status prometheus    # check status"
echo "   journalctl -u prometheus -f         # watch logs"
echo "   sudo systemctl restart prometheus   # restart service"
echo "   sudo systemctl stop prometheus      # stop service"
