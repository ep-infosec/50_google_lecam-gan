# Copyright 2021 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import sys
sys.path.append("..")
from third_party import utils
from third_party.run_eval import run_eval

def main():
    # parse command line and run
    parser = utils.prepare_parser()
    config = vars(parser.parse_args())
    run_eval(config)

if __name__ == '__main__':
    main()
