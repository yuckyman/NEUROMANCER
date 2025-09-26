# prometheus yuckbox deployment guide

*deploying prometheus to yuckbox linux server for 24/7 operation*

## overview

yuckbox will run prometheus continuously, collecting market data and making predictions every 30 minutes. we'll monitor it from neuromancer.

## deployment steps

### 1. from neuromancer (macos)

```bash
cd /Users/ian/NEUROMANCER/3_projects/31_coding/

# make deployment script executable
chmod +x deploy_to_yuckbox.sh

# run deployment
./deploy_to_yuckbox.sh
```

this will:
- create deployment package
- upload files to yuckbox via rsync
- create systemd service file
- prepare setup script

### 2. on yuckbox (linux)

```bash
# ssh into yuckbox
ssh ian@yuckbox

# navigate to prometheus directory
cd /home/ian/prometheus

# run setup script
./deploy_on_yuckbox.sh
```

this will:
- install python dependencies
- create data directories
- set up systemd service
- configure environment

### 3. configure api key

```bash
# edit bashrc to add api key
nano ~/.bashrc

# add this line (replace with your actual key):
export ALPHA_VANTAGE_API_KEY="your_actual_key_here"

# reload environment
source ~/.bashrc
```

### 4. start prometheus service

```bash
# start the service
sudo systemctl start prometheus

# enable auto-start on boot
sudo systemctl enable prometheus

# check status
sudo systemctl status prometheus
```

## monitoring from neuromancer

### real-time dashboard

```bash
cd /Users/ian/NEUROMANCER/3_projects/31_coding/
python3 yuckbox_monitoring.py
```

this shows:
- service status (active/inactive)
- memory usage
- database statistics
- recent predictions
- live logs

### manual commands

```bash
# check service status
ssh ian@yuckbox "systemctl status prometheus"

# view live logs
ssh ian@yuckbox "journalctl -u prometheus -f"

# restart service
ssh ian@yuckbox "sudo systemctl restart prometheus"

# stop service
ssh ian@yuckbox "sudo systemctl stop prometheus"
```

## file structure on yuckbox

```
/home/ian/prometheus/
├── prometheus_monitoring_system.py  # main engine
├── prometheus_config.py            # configuration
├── run_prometheus.py               # launcher
├── requirements_prometheus.txt     # dependencies
├── prometheus.db                   # sqlite database
├── prometheus.log                  # activity log
├── prometheus_data/                # data directory
├── prometheus_logs/                # log directory
└── prometheus_models/              # model directory
```

## systemd service details

### service file: `/etc/systemd/system/prometheus.service`

```ini
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
```

### service management

```bash
# start service
sudo systemctl start prometheus

# stop service
sudo systemctl stop prometheus

# restart service
sudo systemctl restart prometheus

# check status
sudo systemctl status prometheus

# view logs
journalctl -u prometheus -f

# disable auto-start
sudo systemctl disable prometheus
```

## troubleshooting

### common issues

1. **service won't start**
   ```bash
   # check logs for errors
   journalctl -u prometheus -n 50
   
   # check if python dependencies are installed
   python3 -c "import requests, numpy, sqlite3"
   ```

2. **api key not working**
   ```bash
   # verify environment variable
   echo $ALPHA_VANTAGE_API_KEY
   
   # reload environment
   source ~/.bashrc
   ```

3. **permission issues**
   ```bash
   # fix ownership
   sudo chown -R ian:ian /home/ian/prometheus
   
   # fix permissions
   chmod +x /home/ian/prometheus/*.py
   ```

4. **database errors**
   ```bash
   # check database file
   ls -la /home/ian/prometheus/prometheus.db
   
   # reset database (if corrupted)
   rm /home/ian/prometheus/prometheus.db
   sudo systemctl restart prometheus
   ```

### monitoring commands

```bash
# check if prometheus is running
ps aux | grep prometheus

# check memory usage
ps aux | grep prometheus | awk '{print $6/1024 " MB"}'

# check disk usage
du -sh /home/ian/prometheus/

# check database size
ls -lh /home/ian/prometheus/prometheus.db
```

## data backup

### backup database

```bash
# create backup
cp /home/ian/prometheus/prometheus.db /home/ian/prometheus/prometheus_backup_$(date +%Y%m%d).db

# download to neuromancer
scp ian@yuckbox:/home/ian/prometheus/prometheus.db /Users/ian/NEUROMANCER/3_projects/31_coding/backups/
```

### automated backup (optional)

```bash
# create backup script
cat > /home/ian/prometheus/backup.sh << 'EOF'
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
cp prometheus.db "prometheus_backup_${DATE}.db"
# keep only last 7 backups
ls -t prometheus_backup_*.db | tail -n +8 | xargs rm -f
EOF

chmod +x /home/ian/prometheus/backup.sh

# add to crontab (daily backup at 2am)
crontab -e
# add: 0 2 * * * /home/ian/prometheus/backup.sh
```

## performance monitoring

### resource usage

prometheus should use:
- **memory**: ~30MB
- **cpu**: minimal (runs every 30 minutes)
- **disk**: ~25MB after 3 months
- **network**: ~1MB per day (api calls)

### optimization

if yuckbox is resource-constrained:

```bash
# reduce monitoring frequency
# edit prometheus_config.py
MONITORING_INTERVAL_MINUTES = 60  # change from 30 to 60

# restart service
sudo systemctl restart prometheus
```

## security considerations

### file permissions

```bash
# secure prometheus directory
chmod 700 /home/ian/prometheus
chmod 600 /home/ian/prometheus/prometheus.db
chmod 644 /home/ian/prometheus/*.py
```

### firewall (if applicable)

```bash
# prometheus doesn't need incoming ports
# only needs outbound https for api calls
```

## success indicators

### after 24 hours, you should see:

1. **service running**: `systemctl status prometheus` shows active
2. **database growing**: `ls -lh prometheus.db` shows increasing size
3. **predictions made**: database contains prediction records
4. **logs active**: `journalctl -u prometheus` shows regular activity

### after 1 week, you should have:

1. **~1,344 predictions** across all symbols
2. **~1,344 market data points** 
3. **~1,344 reward calculations**
4. **consistent 30-minute intervals** in logs

---

**yuckbox is now your prometheus brain! 🧠🤖**

the agent will run 24/7, learning from real market data, building the foundation for autonomous financial intelligence. every prediction, every reward, every piece of data brings us closer to the future of ai.
