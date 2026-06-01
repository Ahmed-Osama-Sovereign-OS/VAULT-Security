import psutil

class NetworkMonitor:
    @staticmethod
    def get_active_connections():
        """عرض جميع الاتصالات الشبكية النشطة حالياً"""
        connections = psutil.net_connections(kind='inet')
        active_list = []
        for conn in connections:
            if conn.status == 'ESTABLISHED':
                proc = psutil.Process(conn.pid)
                active_list.append({
                    "pid": conn.pid,
                    "process_name": proc.name(),
                    "remote_ip": conn.raddr.ip if conn.raddr else "Local"
                })
        return active_list
