# Copyright (C) 2010 Yaco Sistemas (http://www.yaco.es)
# Copyright (C) 2009 Lorenzo Gil Sanchez
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#            http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls.defaults import patterns, handler500

urlpatterns = patterns(
    'djangosaml2.views',
    (r'^login/$', 'login'),
    (r'^acs/$', 'assertion_consumer_service'),
    (r'^logout/$', 'logout'),
    (r'^ls/$', 'logout_service'),
    (r'^metadata/$', 'metadata'),
)

handler500 = handler500
