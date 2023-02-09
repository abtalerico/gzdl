#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2022 Aidan Talerico <abtalerico@gmail.com>
#
# This file is part of GZDL.
#
# GZDL is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GZDL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GZDL.  If not, see <http://www.gnu.org/licenses/>.
import sys
from gzdl.main import GzdlApp

if __name__ == '__main__':
    app = GzdlApp(application_id="com.example.GtkApplication")
    app.run(sys.argv)
