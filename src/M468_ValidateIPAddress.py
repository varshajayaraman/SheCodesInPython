class Solution:
    def validIPAddress(self, IP: str) -> str:

        def v4(ip):
            if len(ip) != 4:
                return False
            for sub in ip:
                if len(sub) == 0:
                    return False
                try:
                    if int(sub) < 0 or int(sub) > 255:
                        return False
                except:
                    return False
                if int(sub) == 0 and len(sub) == 1:
                    continue
                for i in range(len(sub)):
                    if i == 0 and sub[i] == '0':
                        return False
                    if not sub[i].isdigit():
                        return False
            return True

        def v6(ip):
            if len(ip) != 8:
                return False
            for sub in ip:
                if len(sub) == 0:
                    return False
                # if int(sub)<0 or innt(sub)>255:
                if len(sub) > 4:
                    return False
                for i in range(len(sub)):
                    if not sub[i].isdigit() and not sub[i].isalpha():
                        return False
                    if sub[i].lower() > 'f':
                        return False
            return True

        if ":" in IP:
            ip = IP.split(":")
            if v6(ip):
                return "IPv6"

        else:
            ip = IP.split(".")
            if v4(ip):
                return "IPv4"
        return "Neither"
