#!/usr/bin/env python3
"""
prometheus launcher script
run this to start the monitoring system
"""

import asyncio
import sys
from pathlib import Path

# add current directory to path for imports
sys.path.append(str(Path(__file__).parent))

from prometheus_monitoring_system import PrometheusMonitor
from prometheus_config import MONITORING_INTERVAL_MINUTES, DEBUG_MODE, DRY_RUN

def print_banner():
    """print prometheus startup banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    PROMETHEUS MONITORING                     ║
    ║              autonomous market intelligence system            ║
    ║                                                              ║
    ║  phase 0: free simulation mode                              ║
    ║  tracking: SPY, QQQ, BTC, ETH                               ║
    ║  interval: 30 minutes                                       ║
    ║  mode: dry run (no real trading)                           ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def print_status():
    """print current configuration status"""
    print(f"🔧 configuration:")
    print(f"   monitoring interval: {MONITORING_INTERVAL_MINUTES} minutes")
    print(f"   debug mode: {DEBUG_MODE}")
    print(f"   dry run: {DRY_RUN}")
    print(f"   simulation mode: enabled")
    print()

def main():
    """main entry point"""
    print_banner()
    print_status()
    
    # check if api keys are configured
    from prometheus_config import ALPHA_VANTAGE_API_KEY
    if ALPHA_VANTAGE_API_KEY == "YOUR_ALPHA_VANTAGE_KEY_HERE":
        print("⚠️  warning: alpha vantage api key not configured")
        print("   get your free key from: https://www.alphavantage.co/support/#api-key")
        print("   set ALPHA_VANTAGE_API_KEY environment variable")
        print()
    
    print("🚀 starting prometheus monitoring system...")
    print("   press ctrl+c to stop")
    print()
    
    # create monitor instance
    monitor = PrometheusMonitor()
    
    # run monitoring system
    try:
        asyncio.run(monitor.run(MONITORING_INTERVAL_MINUTES))
    except KeyboardInterrupt:
        print("\n🛑 prometheus monitoring stopped by user")
    except Exception as e:
        print(f"\n❌ error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
