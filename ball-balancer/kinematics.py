import math
import numpy as np

R, L1, L2 = 125.6, 44.94, 85 # R: ball joint radius, L1: length of the bottom arm, L2: length of the top arm
RS, H0 = 49.75, 83.0 # H0: Neutral height over servo shafts
AZ = [90, -30, -150] # Servo angles around center in degrees
SIGN = [1, 1, 1] # Servo directions
TRIM = [0, 0, 0] # Offset per servo in degrees

def servo_angles(tilt_deg, az_deg):
    t, a = math.radians(tilt_deg), math.radians(az_deg)
    n = np.array([math.sin(t)*math.cos(a), math.sin(t)*math.sin(a), math.cos(t)])
    k = np.cross([0, 0, 1], n); s = np.linalg.norm(k)
    
    if s < 1e-9: Rm = np.eye(3)
    else:
        k /= s
        K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
        Rm = np.eye(3) + s*K + (1 - n[2])*K@K
    
    out = []
    for i, phi in enumerate(AZ):
        ph = math.radians(phi)
        p = Rm @ np.array([R * math.cos(ph), R * math.sin(ph), 0])
        er = np.array([math.cos(ph), math.sin(ph)])
        et = np.array([-math.sin(ph), math.cos(ph)])
        
        d = p[:2] @ er - RS
        l = p[:2] @ et
        z = p[2] + H0
        
        L2p = math.sqrt(L2**2 - l**2)
        
        D = math.hypot(d, z)
        
        if not (abs(L2p - L1) < D < L2p + L1):
            raise ValueError("tilt out of reach")
        
        th = math.atan2(z, d) - math.acos((L1**2 + D**2 - L2p**2) / (2*L1*D))
        out.append(90 + SIGN[i]*math.degrees(th) + TRIM[i])
    
    return out