from redis import Redis
from rq import Queue

q = Queue(connection=Redist(host='192.168.1.101', port='6379'))
