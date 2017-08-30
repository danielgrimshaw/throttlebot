import redis_client

'''
This is specifically for the storing and accessing of the redis data 
relating to the current resource allocation of a MR
'''

def generate_mr_key(mr_service, mr_resource):
    return '{},{}'.format(mr_service, mr_resource)

def write_mr_alloc(redis_db, mr, new_allocation):
    mr_name = 'mr_alloc'
    key = generate_mr_key(mr.service_name, mr.resource)
    redis_db.hset(mr_name, key, new_allocation)

def read_mr_alloc(redis_db, mr):
    mr_name = 'mr_alloc'
    key = generate_mr_key(mr.service_name, mr.resource)
    return redis_db.hget(mr_name, key)

'''
Machine Consumption index maps a particular VM (identified by IP address) to 
it's specific resource allocation: both in terms of the total maximal 
capacity to the full amount
'''

# machine_cap is a dict that stores the machine's maximum capacity
# machine_util is a tuple that stores the machine's current usage level
def write_machine_consumption(redis_db, machine_ip, machine_util):
    name = '{}machine_consumption'.format(machine_ip)
    redis_db.hset(name, 'CPU-CORE', machine_util['CPU-CORE'])
    redis_db.hset(name, 'CPU-QUOTA', machine_util['CPU-QUOTA'])
    redis_db.hset(name, 'DISK', machine_util['DISK'])
    redis_db.hset(name, 'NET', machine_util['NET'])

def read_machine_consumption(redis_db, machine_ip):
    machine_util = {}
    name = '{}machine_consumption'.format(machine_ip)
    machine_util['CPU_CORE'] = redis_db.hget(name, 'CPU-CORE')
    machine_util['CPU_QUOTA'] = redis_db.hget(name, 'CPU-QUOTA')
    machine_util['DISK'] = redis_db.hget(name, 'DISK')
    machine_util['NET'] = redis_db.hget(name, 'NET')

    return machine_util

def write_machine_capacity(redis_db, machine_ip, machine_cap):
    name = '{}machine_consumption'.format(machine_ip)
    redis_db.hset(name, 'CPU-CORE', machine_cap['CPU-CORE'])
    redis_db.hset(name, 'CPU-QUOTA', machine_cap['CPU-QUOTA'])
    redis_db.hset(name, 'DISK', machine_cap['DISK'])
    redis_db.hset(name, 'NET', machine_cap['NET'])

def read_machine_capacity(redis_db, machine_ip):
    machine_cap = {}
    name = '{}machine_capacity'.format(machine_ip)
    machine_cap['CPU_CORE'] = redis_db.hget(name, 'CPU-CORE')
    machine_cap['CPU_QUOTA'] = redis_db.hget(name, 'CPU-QUOTA')
    machine_cap['DISK'] = redis_db.hget(name, 'DISK')
    machine_cap['NET'] = redis_db.hget(name, 'NET')

    return machine_cap

    

