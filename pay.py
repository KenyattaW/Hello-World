def computepay(h, r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 * r)
    else: 
        p = h * r
    return p 

hrs = input("Enter Hours:")
fhrs = float(hrs)
rate = input ("Enter Rate:")
frate = float (rate)
p = computepay(fhrs, frate)
print("Pay", p)