#!/usr/local/bin/python3.6

import speedtest, os, argparse

def csv_format_strings(*args):
    
    """ Dynamically format args as string csv items """
    
    if isinstance(args,dict):
        # ---- don't give me dicts, cba to program for it
        raise TypeError('Dict passed to csv_format_strings')
        
    elif isinstance(args,int) or isinstance(args,float) or isinstance(args,str):
        # ---- 'immutable' values passed (string isn't really immutable, but sort of is for this purpose)
        raise TypeError('Immutable type passed to csv_format_strings')
    
    elif isinstance(args,tuple) and isinstance(args[0],list) or isinstance(args[0],tuple):
        # ---- args have been passed without a * expansion
        args = tuple(args[0])
        
    else: pass
    
    return ','.join([str(arg) for arg in args])

def stats_calc(results_file='./results.csv'):
    pass

def run_speed_testing(servers = [] ):
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload(pre_allocate=False)
    s.results.share()
    
    return s.results.dict()
    
    
def run_test( results_output, results_path , servers = [], print_output = False ):
    
    # ---- create results file + headers (with server name)

    results_file = results_path + '/results.csv'
    
    if 'results.csv' not in os.listdir(results_path):
        with open(results_file, 'w') as tmp_f:
            tmp_f.write( csv_format_strings( results_output ) + '\n' )
    
    results_dict = run_speed_testing( servers )
    
    # ---- check keys exist
    
    for key in results_output:
        if key not in results_dict.keys(): raise KeyError('KEY ERROR')
        else: pass
    
    # ---- write results
    
    results_to_write = tuple( results_dict[key] for key in results_output )
    stdout_results = { key : results_dict[key] for key in results_output }
    results_string = csv_format_strings( *results_to_write )
    
    with open(results_file,'a+') as outfile: outfile.write(results_string + '\n' )
    
    if print_output is True:
        for key, value in stdout_results.items(): print(key, value)
    
    
if __name__ == '__main__':
    
    # TODO argparser
    
    # TODO test against multiple servers
    # - how to prepend server details to headers / results file
    
    #if len(servers) > 1:
    #    for server in servers:
    #        results_output = ['server'] + results_output 
    #        run_test(server)
    #else: run_test()
    
    # ---- simple run
    
    results_output, results_path, servers = ['timestamp','download','upload','ping'], '/Users/Mike/data/local-jobs/speedtesting', []
    
    run_test(results_output, results_path, servers = servers, print_output = False)
