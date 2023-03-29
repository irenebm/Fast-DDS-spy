# Copyright 2023 Proyectos y Sistemas de Mantenimiento SL (eProsima).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Tests for the fastddsspy executable.

Contains a package of system test for fastddsspy tool

Usage: test.py -e <binary_path>

Arguments:

    Fast DDS Spy binary path          : -e | --exe binary_path

    Run test in Debug mode          : -d | --debug

"""

import logging
import subprocess

DESCRIPTION = """Script to execute Fast DDS Spy executable test"""
USAGE = ('python3 tests.py -e <path/to/fastddsspy-executable>'
         ' [-d]')


class TestCase():

    def __init__(self, name, one_shot, command, dds, arguments):
        self.name = name
        self.one_shot = one_shot
        self.command = command
        self.dds = dds
        self.arguments = arguments
        self.exec_spy = ''

        # Create a custom logger
        self.logger = logging.getLogger('SYS_TEST')
        # Create handlers
        l_handler = logging.StreamHandler()
        # Create formatters and add it to handlers
        l_format = '[%(asctime)s][%(name)s][%(levelname)s] %(message)s'
        l_format = logging.Formatter(l_format)
        l_handler.setFormatter(l_format)
        # Add handlers to the logger
        self.logger.addHandler(l_handler)

    def run(self):
        if (self.dds):
            self.run_dds()
        return self.run_tool()

    def run_tool(self):
        self.logger.info('Run tool')
        if (self.one_shot):
            self.command = [self.exec_spy, self.arguments]
        else:
            self.command = [self.exec_spy]

        self.logger.info('Executing command: ' + str(self.command))

        proc = subprocess.Popen(self.command,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

        if (self.one_shot):
            try:
                output_bytes, error_bytes = proc.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                output_bytes, error_bytes = proc.communicate()

        return proc

    def is_stop_tool(self, proc):
        return_code = proc.poll()

        if (return_code is None):
            return False
        return True

    def send_command_tool(self, proc):
        proc.stdin.write(('self.arguments'+'\n').encode('utf-8'))
        if self.dds:
            # proc.stdin.close()
            # proc.stdout.read()
            # proc.stderr.read()
            # proc.stdout.close()
            # proc.stderr.close()
            # output = proc.stdout.read()
            error = proc.stderr.read()
            self.valid_output_tool(error)

    def stop_tool(self, proc):
        try:
            output_bytes, error_bytes = proc.communicate(input=b'exit\n', timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
            output_bytes, error_bytes = proc.communicate()

    def run_dds(self):
        self.logger.info('Run dds')
        # proc = Popen(f"example {self.dds}")
        # proc.communicate(self.command)

    def valid_output_tool(self, returncode):
        # -9: corresponds to the SIGKILL signal
        # 0: Successful termination
        # 1: General error
        # 2: Misuse of shell builtins
        # 126: Command invoked cannot execute
        # 127: Command not found
        # 128: Invalid argument to exit
        # 130: Terminated by Ctrl-C
        # 255: Exit status out of range
        return (returncode == 0)
