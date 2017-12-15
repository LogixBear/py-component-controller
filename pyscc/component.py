# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from selenium.webdriver import Remote, Firefox, Chrome, Safari, Opera
from selenium.common.exceptions import WebDriverException, ElementNotVisibleException
from pyscc.resource import Resource


class Component(Resource):
    """
    :Description: Base resource for web components.
    :param controller: Parent controller reference.
    :type controller: Controller
    :return: Component
    """
    def __init__(self, controller, **kwargs):
        self.controller = controller
        super(Component, self).__init__(self, **kwargs)

    def register(name, selector):
        # TODO: Figure out how to instantiate new function wrapped with element
        setattr(self, name, )
