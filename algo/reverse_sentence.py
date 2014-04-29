"""
Reverse a string in place
"""

ip = list("hello how are u")

def rev(ip, start, end):
    while start < end:
        ip[start], ip[end] = ip[end], ip[start]
        start += 1
        end -=1

def main():
    rev(ip, 0, len(ip)-1)

    start = 0
    end = len(ip)
    beg = 0

    while start < end:
        if ip[start] == ' ':
            rev(ip, beg, start-1)
            beg = start+1
        start+=1
  
    # reverse last word
    rev(ip, beg, start-1)
  
    print ''.join(ip)
  
if '__main__' == __name__:
    main()
