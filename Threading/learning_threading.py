import time
import concurrent.futures



def timer(minutes):
    print(f"running {minutes}...")
    tim = 0
    while tim != minutes:
        time.sleep(60)
        tim +=1
    return tim


# def do_something(seconds):
#     print(f'Sleeping {seconds} second...')
#     time.sleep(seconds)
#     return f'Done Sleeping in {seconds}...'


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [10, 8, 6, 4, 2]
#     results = [executor.submit(do_something, sec) for sec in secs]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
#
# dur = time.time() - start
# print(f'Finished in {round(dur, 2)} second(s)')
start = time.time()

with concurrent.futures.ThreadPoolExecutor() as executor:
    mins = [10, 8, 6, 4, 2]
    results = [executor.submit(timer, min) for min in mins]
    for f in concurrent.futures.as_completed(results):
        print(f'{f.result()} is up')

dur = time.time() - start
print(f'Finished in {round(dur, 2)} minutes')