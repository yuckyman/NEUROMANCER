#!/usr/bin/env python3
"""
yuckbox monitoring dashboard
run this from NEUROMANCER to monitor prometheus on yuckbox
"""

import subprocess
import json
import time
from datetime import datetime
import sqlite3
import os

class YuckboxMonitor:
    """monitor prometheus running on yuckbox"""
    
    def __init__(self, yuckbox_user="ian", yuckbox_host="yuckbox"):
        self.yuckbox_user = yuckbox_user
        self.yuckbox_host = yuckbox_host
        self.remote_path = f"/home/{yuckbox_user}/prometheus"
        
    def run_ssh_command(self, command):
        """run command on yuckbox via ssh"""
        full_command = f"ssh {self.yuckbox_user}@{self.yuckbox_host} '{command}'"
        try:
            result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            return False, "", str(e)
    
    def check_service_status(self):
        """check if prometheus service is running"""
        success, stdout, stderr = self.run_ssh_command("systemctl is-active prometheus")
        return success and "active" in stdout
    
    def get_service_logs(self, lines=20):
        """get recent service logs"""
        success, stdout, stderr = self.run_ssh_command(f"journalctl -u prometheus -n {lines} --no-pager")
        return stdout if success else stderr
    
    def get_database_stats(self):
        """get database statistics"""
        success, stdout, stderr = self.run_ssh_command(f"cd {self.remote_path} && python3 -c \"
import sqlite3
import json
try:
    conn = sqlite3.connect('prometheus.db')
    cursor = conn.cursor()
    
    # count records
    cursor.execute('SELECT COUNT(*) FROM market_data')
    market_count = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM predictions')
    pred_count = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM rewards')
    reward_count = cursor.fetchone()[0]
    
    # latest prediction
    cursor.execute('SELECT symbol, direction, confidence, timestamp FROM predictions ORDER BY timestamp DESC LIMIT 1')
    latest_pred = cursor.fetchone()
    
    # accuracy stats
    cursor.execute('SELECT AVG(total_reward) FROM rewards')
    avg_reward = cursor.fetchone()[0] or 0
    
    conn.close()
    
    stats = {
        'market_data_count': market_count,
        'predictions_count': pred_count,
        'rewards_count': reward_count,
        'latest_prediction': latest_pred,
        'average_reward': avg_reward
    }
    
    print(json.dumps(stats))
except Exception as e:
    print(json.dumps({'error': str(e)}))
\"")
        
        if success:
            try:
                return json.loads(stdout)
            except:
                return {"error": "failed to parse database stats"}
        else:
            return {"error": stderr}
    
    def get_system_stats(self):
        """get system resource usage"""
        success, stdout, stderr = self.run_ssh_command("ps aux | grep prometheus | grep -v grep")
        if success and stdout:
            # parse memory usage
            parts = stdout.split()
            if len(parts) > 5:
                memory_mb = float(parts[5]) / 1024  # convert KB to MB
                return {"memory_mb": memory_mb, "status": "running"}
        
        return {"status": "not_running"}
    
    def display_dashboard(self):
        """display monitoring dashboard"""
        print("🔍 PROMETHEUS YUCKBOX MONITORING DASHBOARD")
        print("=" * 60)
        print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # service status
        print("📊 SERVICE STATUS:")
        if self.check_service_status():
            print("   ✅ prometheus service: ACTIVE")
        else:
            print("   ❌ prometheus service: INACTIVE")
        
        # system stats
        sys_stats = self.get_system_stats()
        if sys_stats["status"] == "running":
            print(f"   🧠 memory usage: {sys_stats.get('memory_mb', 0):.1f}MB")
        else:
            print("   🧠 memory usage: N/A (not running)")
        
        print()
        
        # database stats
        print("💾 DATABASE STATISTICS:")
        db_stats = self.get_database_stats()
        if "error" not in db_stats:
            print(f"   📈 market data points: {db_stats.get('market_data_count', 0)}")
            print(f"   🔮 predictions made: {db_stats.get('predictions_count', 0)}")
            print(f"   🎯 rewards calculated: {db_stats.get('rewards_count', 0)}")
            print(f"   📊 average reward: {db_stats.get('average_reward', 0):.3f}")
            
            latest_pred = db_stats.get('latest_prediction')
            if latest_pred:
                symbol, direction, confidence, timestamp = latest_pred
                print(f"   🎲 latest prediction: {symbol} {direction} ({confidence:.2f}) at {timestamp}")
        else:
            print(f"   ❌ database error: {db_stats['error']}")
        
        print()
        
        # recent logs
        print("📝 RECENT LOGS:")
        logs = self.get_service_logs(10)
        if logs:
            for line in logs.split('\n')[-10:]:  # last 10 lines
                if line.strip():
                    print(f"   {line}")
        else:
            print("   no logs available")
        
        print()
        print("🔄 refresh in 30 seconds... (ctrl+c to exit)")

def main():
    """main monitoring loop"""
    monitor = YuckboxMonitor()
    
    try:
        while True:
            os.system('clear')  # clear screen
            monitor.display_dashboard()
            time.sleep(30)  # refresh every 30 seconds
    except KeyboardInterrupt:
        print("\n👋 monitoring stopped")

if __name__ == "__main__":
    main()
