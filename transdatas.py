#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 2018-11-23 11:34:51
# 转换 数据格式

def func(*args, **kw):
    print(kw)
    print(args)
    print(len(kw))
    print(kw.items())

if __name__ == "__main__":

    func(3, x=1, y=2, z=3)
    dicts = {'x': 1, 'y': 2, 'z': 3}
    dlist = []
    for k, v in dicts.items():
        dlist.append({k: v})
    print(dlist)

    prodata = {
  "appendfsync": "everysec",
  "appendonly": "no",
  "hash-max-ziplist-entries": 512,
  "hash-max-ziplist-value": 64,
  "list-max-ziplist-entries": 512,
  "list-max-ziplist-value": 64,
  "maxclients": 100000,
  "maxmemory-policy": "allkeys-lru",
  "maxmemory-samples": 3,
  "no-appendfsync-on-rewrite": "no",
  "port": 20017,
  "repl-timeout": 60,
  "save": "900 1 300 10 60 1000",
  "set-max-intset-entries": 512,
  "slaveof": "0.0.0.0 6379",
  "slowlog-log-slower-than": 10000,
  "slowlog-max-len": 128,
  "tcp-keepalive": 0,
  "timeout": 300,
  "zset-max-ziplist-entries": 128,
  "zset-max-ziplist-value": 64
}
    result = []

    for k, v in prodata.items():
        rdic = {}
        rdic[k] = v
        result.append(rdic)
    print(len(result))
    print("转换成输入格式", result)
    rlist = []
    r1 = []
    for k in prodata:
        r1.append(k)
    print("ri:", r1)
    #
    # for k in prodata:
    #     rlist.append(k)
    #     print("params['%s'] = %s" % (k, k))
    # print(rlist)

    # for k in prodata:
    #     print("%s, " % k, end='')

    lists = [
            {'back_log': 65535},
            {'character_set_server': 'UTF8'},
            {'expire_logs_days': 30},
            {'ft_min_word_len': 30},
            {'gtid_mode': 'ON'},
            {'innodb_buffer_pool_instances': 1}, {'innodb_flush_log_at_trx_commit': 0}, {'innodb_flush_method': 'O_DIRECT'}, {'innodb_flush_neighbors': 1},
            {'innodb_io_capacity': 4096},
            {'innodb_max_dirty_pages_pct': '95'}, {'innodb_read_io_threads': 1},
            {'innodb_write_io_threads': 1},
            {'interactive_timeout': 86400}, {'log_bin_trust_function_creators': 'ON'}, {'log_queries_not_using_indexes': 'ON'},
            {'long_query_time': '1.000000'},
            {'lower_case_table_names': 1},
            {'max_allowed_packet': '1'},
            {'max_connect_errors': 0},
            {'max_connections': 65536},
            {'open_files_limit': 204800},
            {'query_cache_size': 0},
            {'query_cache_type': 'ON'},
            {'skip_name_resolve': 'OFF'},
            {'sql_mode': 'NO_PARAMS_SUBSTITUTION'},
            {'sync_binlog': 0},
            {'table_open_cache': 8096},
            {'thread_cache_size': 0},
            {'wait_timeout': 80644}
            ]
    for dt in lists:
        # print(dt)
        k = list(dt)[0]
        if type(dt[k]) == int:
            print("%s=%s, " % (k, dt[k]), end='')
        else:
            print("%s='%s', " % (k, dt[k]), end='')
    dicts = {'x': 1, "2": "y"}
    dlist = list(dicts)
    print("dlist", dlist)
        # print(eval(x))

    string = "back_log,character_set_server,expire_logs_days, ft_min_word_len,gtid_mode,innodb_buffer_pool_instances, innodb_flush_log_at_trx_commit, innodb_flush_method,innodb_flush_neighbors, innodb_io_capacity, innodb_max_dirty_pages_pct,innodb_read_io_threads, innodb_write_io_threads, interactive_timeout,log_bin_trust_function_creators, log_queries_not_using_indexes, long_query_time,lower_case_table_names, max_allowed_packet, max_connect_errors, max_connections,open_files_limit, query_cache_size, query_cache_type, skip_name_resolve, sql_mode,sync_binlog, table_open_cache, thread_cache_size, wait_timeout"

    x = string.split()
    xl = ''.join(x)
    x = xl.split(',')
    print(x)


