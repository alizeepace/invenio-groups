# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2014, 2015, 2016 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Group bundles."""

from __future__ import absolute_import, print_function

from invenio_assets import Bundle, RequireJSFilter

# FIXME from invenio_base.bundles import invenio as _i
# FIXME from invenio_base.bundles import jquery as _j

js = Bundle(
    'js/groups/init.js',
    filters=RequireJSFilter(),  # FIXME exclude=[_j, _i]),
    output="groups.js",
    weight=50
)

styles = Bundle(
    'css/groups/groups.less',
    filters='less,cleancss',
    output='groups.css',
    weight=50
)
