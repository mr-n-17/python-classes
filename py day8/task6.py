# 6. Handle KeyboardInterrupt Exception When Reading Input


try: n=input()
except KeyboardInterrupt as e:
    print(e)