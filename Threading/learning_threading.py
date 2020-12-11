import time
import concurrent.futures


def timer(minutes):
    print(f"running {minutes}...")
    tim = 0
    while tim != minutes:
        time.sleep(60)
        tim +=1
    return tim


def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return f'Done Sleeping in {seconds}...'

#
# with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#     secs = [8, 10, 6, 4, 2]
#     results = [executor.submit(do_something, sec) for sec in secs]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
#
# dur = time.time() - start
# print(f'Finished in {round(dur, 2)} second(s)')

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [10, 8, 6, 4, 2]
#     executor.map(do_something, secs)


mins = [1, 2, 3, 1, 2]


def queue_time(customers, tills):
    """
        Function that calculates the maximum amount of time it will take for all customers to be attended to.

      :param customers: the minutes each customer will take at the till
      :type customers: list

      :param tills: the number of tills available
      :type tills: int

      :return: None
    """

    with concurrent.futures.ThreadPoolExecutor(max_workers=tills) as executor:
        results = [executor.submit(timer, customer) for customer in customers]
        for f in concurrent.futures.as_completed(results):
            print(f'{f.result()} minutes is up')


start = time.time()
print(queue_time(mins, 4))
dur = time.time() - start
print(f'Finished in {round(dur, 2)} minutes')
