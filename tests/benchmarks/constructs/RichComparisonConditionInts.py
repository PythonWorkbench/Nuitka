#     Copyright 2024, Kay Hayen, mailto:kay.hayen@gmail.com find license text at end of file


import itertools
import sys

module_value1 = "1000"
module_value2 = "2000"

loop_count = 50000 if len(sys.argv) < 2 else int(sys.argv[1])


def calledRepeatedly(cond, value):
    if cond:
        if value % 2 == 0:
            value = not value
    else:
        value = not value

    return value


for x in range(50000):
    # construct_begin
    calledRepeatedly(True, x)
    # construct_alternative
    calledRepeatedly(False, x)
    # construct_end


print("OK.")

#     Python test originally created or extracted from other peoples work. The
#     parts from me are licensed as below. It is at least Free Software where
#     it's copied from other people. In these cases, that will normally be
#     indicated.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.