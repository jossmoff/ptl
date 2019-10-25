import psutil
import time
import math
import gitlab
import os
from argparse import ArgumentParser
import configparser

MODULE_NAME = "ptl: Automatically log time in GitLab issue tracker for COMP23311 at UoM."
__version__ = "0.1.0"

def print_config(token, project_id, issue_id):
  print("--:CONFIG:--\n" + "🎫 TOKEN:" + token + "\n🆔 PROJECT-ID:" + project_id  + "\n🆔 ISSUE-ID:" +  issue_id)

def record_time(token, project_id, issue_id, ide="eclipse"):
    eclipse_id = -1
    # Iterate over all running process
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            proc_name = proc.name()
            proc_id = proc.pid
            if ide in proc_name:
                eclipse_id = proc_id
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    if eclipse_id != -1:
        # Get start_time
        print("⏱️  Recording elapsed worktime for " + ide)
        start_time = time.time()
        while psutil.pid_exists(eclipse_id):
            time.sleep(1)
        end_time = time.time()
        elapsed_time = (end_time - start_time) / 3600
        elapsed_time = (math.ceil(elapsed_time))
        # private token or personal token authentication
        gl = gitlab.Gitlab('https://gitlab.cs.man.ac.uk', private_token=token)
        # Make an API request and authenticate in order to add issue.
        gl.auth()
        project = gl.projects.get(project_id)
        issue = project.issues.get(issue_id)
        issue.add_spent_time(str(elapsed_time)+'h')
        print("⏱️  " + str(elapsed_time) + "h of time recorded.")
    else:
      print("❌ IDE not running yet!")

def set_config(token, project_id, issue_id, config):
  config['SETTINGS']['token'] = token
  config['SETTINGS']['project_id'] = project_id
  config['SETTINGS']['issue_id'] = issue_id
  with open('config.ini', 'w') as configfile:
    config.write(configfile)
  return config

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if len(config) == 1 and 'DEFAULT' in config:
        config['SETTINGS'] = {}
        config = set_config("0", "0", "0", config)
        parser = ArgumentParser(description=MODULE_NAME)
        parser.add_argument('-c','--config',
                          action="store_true", dest="config", default=False,
                          help="Shows config of current ptl settings")
        parser.add_argument('-t','--token',
                          type=str, dest="token", default=config['SETTINGS']['token'],
                          help="Sets private token for GitLab user")
        parser.add_argument('-p','--projectid',
                          type=str, dest="project_id", default=config['SETTINGS']['project_id'],
                          help="Sets project id for a GitLab repository")
        parser.add_argument('-i','--issueid',
                          type=str, dest="issue_id", default=config['SETTINGS']['issue_id'],
                          help="Sets issue id for an issue in a GitLab repository")
        parser.add_argument('-s','--start',
                          action="store_true", dest="time", default=False,
                          help="Start timing IDE open time.")


        args = parser.parse_args()
        if args.config:
            print_config(args.token,args. project_id, args.issue_id)
        else:
            if (args.token != config['SETTINGS']['token'] or args.project_id != config['SETTINGS']['project_id']
                or args.issue_id != config['SETTINGS']['issue_id']):
                config = set_config(args.token, args.project_id, args.issue_id, config)
            elif args.time:
                record_time(args.token, int(args.project_id), int(args.issue_id))

if __name__ == "__main__":
  main()
