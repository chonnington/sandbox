
from time import sleep, strftime
from concurrent import futures
import os

def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s...'
    display(msg.format('\t'*n, n, n))
    sleep(n)
    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10


def main():

    display('Script starting.')

    executor = futures.ThreadPoolExecutor(max_workers=4)
    results = executor.map(loiter, range(20))
    display('results:', results)

    display('Waiting for individual results:')
    for i, result in enumerate(results):
        display('result {}: {}'.format(i, result))


if __name__ == '__main__':
    main()


'''
/usr/local/bin/python3.7 /Users/terrychon/Desktop/program_repo/py/practice/concurrency/demo_executor_map.py
[17:10:00] Script starting.
[17:10:00] loiter(0): doing nothing for 0s...
[17:10:00] loiter(0): done.
[17:10:00] 	loiter(1): doing nothing for 1s...
[17:10:00] 		loiter(2): doing nothing for 2s...
[17:10:00] 			loiter(3): doing nothing for 3s...
[17:10:00] results: <generator object Executor.map.<locals>.result_iterator at 0x104357a98>
[17:10:00] Waiting for individual results:[17:10:00]
[17:10:00] result 0: 0
 				loiter(4): doing nothing for 4s...
[17:10:01] 	loiter(1): done.
[17:10:01] 					loiter(5): doing nothing for 5s...
[17:10:01] result 1: 10
[17:10:02] 		loiter(2): done.
[17:10:02] 						loiter(6): doing nothing for 6s...
[17:10:02] result 2: 20
[17:10:03] 			loiter(3): done.
[17:10:03] 							loiter(7): doing nothing for 7s...
[17:10:03] result 3: 30
[17:10:04] 				loiter(4): done.
[17:10:04] 								loiter(8): doing nothing for 8s...
[17:10:04] result 4: 40
[17:10:06] 					loiter(5): done.
[17:10:06][17:10:06] result 5: 50
 									loiter(9): doing nothing for 9s...
[17:10:08] 						loiter(6): done.
[17:10:08] 										loiter(10): doing nothing for 10s...
[17:10:08] result 6: 60
[17:10:10] 							loiter(7): done.
[17:10:10] 											loiter(11): doing nothing for 11s...
[17:10:10] result 7: 70
[17:10:12] 								loiter(8): done.
[17:10:12] 												loiter(12): doing nothing for 12s...
[17:10:12] result 8: 80
[17:10:15] 									loiter(9): done.
[17:10:15] 													loiter(13): doing nothing for 13s...[17:10:15] result 9: 90

[17:10:18] 										loiter(10): done.
[17:10:18] 														loiter(14): doing nothing for 14s...
[17:10:18] result 10: 100
[17:10:21] 											loiter(11): done.
[17:10:21] 															loiter(15): doing nothing for 15s...
[17:10:21] result 11: 110
[17:10:24] 												loiter(12): done.
[17:10:24] [17:10:24] result 12: 120
																loiter(16): doing nothing for 16s...
[17:10:28] 													loiter(13): done.
[17:10:28] 																	loiter(17): doing nothing for 17s...
[17:10:28] result 13: 130
[17:10:32] 														loiter(14): done.
[17:10:32][17:10:32] result 14: 140
 																		loiter(18): doing nothing for 18s...
[17:10:36] 															loiter(15): done.
[17:10:36] [17:10:36] result 15: 150
																			loiter(19): doing nothing for 19s...
[17:10:40] 																loiter(16): done.
[17:10:40] result 16: 160
[17:10:45] 																	loiter(17): done.
[17:10:45] result 17: 170
[17:10:50] 																		loiter(18): done.
[17:10:50] result 18: 180
[17:10:55] 																			loiter(19): done.
[17:10:55] result 19: 190

Process finished with exit code 0
'''

'''
The Executor.map function is easy to use but it has a feature that may or may not be helpful, 
depending on your needs: it returns the results exactly in the same order as the calls are started: 
if the first call takes 10s to produce a result, and the others take 1s each, your code will block for 
10s as it tries to retrieve the first result of the generator returned by map. After that, you’ll get 
the remaining results without blocking because they will be done. That’s OK when you must have all the 
results before proceeding, but often it’s preferable to get the results as they are ready, regardless 
of the order they were submitted. To do that, you need a combination of the Executor.submit method 
and the futures.as_completed function
'''